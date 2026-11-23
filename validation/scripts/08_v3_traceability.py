"""V3: traceability question -> topics (V1) -> studies cited in the per-question answer -> studies kept in v9.

Answers: summaries/Summaries_new_questions_(Sep_30)/summaries_new_questions_(Sep_30).docx (45 questions,
NotebookLM answers condensed with GPT). Questions are matched to the 42 of the v9 appendix by text similarity.
Author-year citations in each answer are matched to the corpus master list (first-author surname + year;
a +-1 year match is accepted and flagged). Output: validation/v3_traceability.csv, validation/v3_summary.txt
"""
import difflib, os, re, sys, unicodedata, zipfile
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1]); os.chdir(ROOT)
na = lambda s: unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
z = zipfile.ZipFile("summaries/Summaries_new_questions_(Sep_30)/summaries_new_questions_(Sep_30).docx")
x = z.read("word/document.xml").decode("utf8")
paras = ["".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p)) for p in re.findall(r"<w:p[ >].*?</w:p>", x, flags=re.S)]
answers, cur = [], None
for p in paras:
    m = re.match(r".*?Question \d+:\s*(.+)", p)
    if "Question" in p and m and "?" in p:
        cur = {"q_sep30": m.group(1).strip(), "text": ""}; answers.append(cur)
    elif cur is not None:
        cur["text"] += " " + p

M = pd.read_csv("validation/v1_matrix.csv", index_col=0)
tex = Path("FSO_v9_NatureSR/FSO_NatureSR_main.tex").read_text()
app = tex.split(r"\section*{Supplementary Information")[1]
blocks = re.split(r"\\caption\{\\textbf\{Query Protocol for Supertopic (\d)", app)[1:]
Q = [(f"ST{st}-Q{int(n):02d}", q.strip()) for st, body in zip(blocks[::2], blocks[1::2]) for n, q in re.findall(r"\n(\d+)\. (.+?) \\\\", body)]

master = pd.read_pickle("data3/df_summary_matches_no_duplicates.pkl")
master = master.dropna(subset=["file_number"])
master["sur"] = master.Authors.str.split(",").str[0].map(na).str.strip()
master["year"] = master["Publication Year"].astype(int)
man = pd.read_csv("validation/corpus_manifest.csv")
kept = set(man[man.in_synthesis.astype(str) == "True"].file_id.astype(int))

def cites(t):
    out = set()
    for a, y in re.findall(r"([A-Z][A-Za-z\u00C0-\u017F'\-]+)(?: et al\.?| and [A-Z][A-Za-z\-]+)?,? \(?((?:19|20)\d{2})\)?", t):
        out.add((na(a), int(y)))
    return out

rows = []
for qid, qt in Q:
    best = max(answers, key=lambda a: difflib.SequenceMatcher(None, na(qt), na(a["q_sep30"])).ratio())
    r = difflib.SequenceMatcher(None, na(qt), na(best["q_sep30"])).ratio()
    direct = [str(t) for t in M.columns if M.loc[qid, t] == 2]
    partial = [str(t) for t in M.columns if M.loc[qid, t] == 1]
    ids, offyear, unmatched = set(), 0, set()
    for sur, y in cites(best["text"]) if r > 0.6 else []:
        hit = master[(master.sur == sur) & (master.year == y)]
        if hit.empty:
            hit = master[(master.sur == sur) & ((master.year - y).abs() == 1)]
            offyear += int(not hit.empty)
        if hit.empty:
            unmatched.add(f"{sur} {y}")
        ids |= set(hit.file_number.astype(int))
    rows.append({"question_id": qid, "question": qt, "match_ratio": round(r, 2),
                 "direct_topics": ";".join(direct), "partial_topics": ";".join(partial),
                 "studies_in_answer": ";".join(f"{i:03d}" for i in sorted(ids)),
                 "n_in_answer": len(ids), "n_kept_in_v9": len(ids & kept),
                 "n_citations_off_by_one_year": offyear, "unmatched_citations": ";".join(sorted(unmatched))})
df = pd.DataFrame(rows); df.to_csv("validation/v3_traceability.csv", index=False)
ok = df[df.match_ratio > 0.6]
lines = [f"Questions matched to a Sep-30 answer (ratio > 0.6): {len(ok)}/42",
         f"Studies cited per answer: median {ok.n_in_answer.median():.0f}, range {ok.n_in_answer.min()}-{ok.n_in_answer.max()}",
         f"Distinct corpus studies cited across answers: {len(set(';'.join(ok.studies_in_answer).split(';')) - {''})}",
         f"Study-question links kept in v9: {int(ok.n_kept_in_v9.sum())}/{int(ok.n_in_answer.sum())}",
         f"Citations matched only with +-1 year: {int(ok.n_citations_off_by_one_year.sum())}",
         f"Questions with no matched study: {list(ok[ok.n_in_answer == 0].question_id)}",
         f"Unmatched questions: {list(df[df.match_ratio <= 0.6].question_id)}"]
Path("validation/v3_summary.txt").write_text("\n".join(lines) + "\n"); print("\n".join(lines))
print(df[["question_id", "match_ratio", "direct_topics", "n_in_answer", "n_kept_in_v9", "unmatched_citations"]].to_string())
