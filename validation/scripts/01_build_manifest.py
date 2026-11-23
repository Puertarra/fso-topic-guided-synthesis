"""Build the corpus manifest: one row per document with topic, supertopic and citation status.

Inputs (relative to the FSO folder):
  data3/df_summary_matches_no_duplicates.pkl  master WoS list (146 records)
  topics/topics_documents_0218.pkl            BERTopic output (145 documents)
  topics/df_docs_topics.xlsx                  supertopic assignment per document
  FSO_v9_NatureSR/FSO_NatureSR_main.tex       manuscript v9 (Table 3 citation keys)
  FSO_v9_NatureSR/cas-refs.bib                bibliography
  data_extra/*.pdf                            complementary search (8 PDFs)
Output:
  validation/corpus_manifest.csv
"""
import re, difflib, sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1])
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", re.sub(r"[{}\\]", "", str(s).lower()))).strip()

master = pd.read_pickle(ROOT / "data3/df_summary_matches_no_duplicates.pkl")
topics = pd.read_pickle(ROOT / "topics/topics_documents_0218.pkl")
st = pd.read_excel(ROOT / "topics/df_docs_topics.xlsx")
combined = pd.read_pickle(ROOT / "src/df_combined2.pkl")

# The topic model rows follow the order of df_combined2 (file ids 001..146 without 085)
assert len(topics) == len(combined) == len(st) == 145
topics = topics.reset_index(drop=True)
topics["file_id"] = [int(i) for i in combined.index]
topics["title"] = combined["Title"].values
topics["supertopic_1"] = st["ST-1"].values
topics["supertopic_2"] = st["ST-2"].values

m = master.dropna(subset=["file_number"]).copy()
m["file_id"] = m["file_number"].astype(int)
df = topics.merge(m[["file_id", "Publication Year", "Authors", "DOI"]], on="file_id", how="left")

# Citation keys used in Table 3 (supertopic table) and anywhere in the manuscript
tex = (ROOT / "FSO_v9_NatureSR/FSO_NatureSR_main.tex").read_text()
tex_nc = "\n".join(l for l in tex.splitlines() if not l.lstrip().startswith("%"))
tab = re.search(r"label\{tab:supertopics\}(.*?)\\end\{tabularx\}", tex_nc, re.S).group(1)
split = lambda s: [k.strip() for c in re.findall(r"\\cite\{([^}]*)\}", s) for k in c.split(",")]
synth_keys = list(dict.fromkeys(split(tab)))
all_keys = set(split(tex_nc))

bib = (ROOT / "FSO_v9_NatureSR/cas-refs.bib").read_text()
bibtitle = {}
for e in re.split(r"\n@", bib):
    km = re.match(r"\s*@?\w+\{([^,]+),", e)
    t = re.search(r"\btitle\s*=\s*[{\"](.+?)[}\"]\s*,?\s*\n", e, re.S)
    if km and t:
        bibtitle[km.group(1).strip()] = norm(t.group(1))

doc_norm = [norm(t) for t in df["title"]]
def match(key):
    t = bibtitle.get(key, "")
    if not t:
        return None
    hits = [i for i, d in enumerate(doc_norm) if t[:60] in d or d[:60] in t]
    if hits:
        return hits[0]
    r, i = max((difflib.SequenceMatcher(None, t, d).ratio(), i) for i, d in enumerate(doc_norm))
    return i if r > 0.85 else None

df["synthesis_key"] = ""
df["cited_anywhere_key"] = ""
for k in sorted(all_keys):
    i = match(k)
    if i is None:
        continue
    col = "synthesis_key" if k in synth_keys else "cited_anywhere_key"
    df.at[i, col] = ";".join(filter(None, [df.at[i, col], k]))
df["in_synthesis"] = df["synthesis_key"] != ""
df["source"] = "WoS corpus (topic model)"

unmatched = [k for k in synth_keys if match(k) is None]

# Complementary documents (not in the topic model)
extra = sorted((ROOT / "data_extra").glob("*.pdf"))
rows = [{"file_id": None, "Topic": None, "title": p.stem, "source": "complementary search", "pdf": str(p.relative_to(ROOT))} for p in extra]
df["pdf"] = [f"data/{i:03d}.pdf" if i <= 125 else f"data2/{i:03d}.pdf" for i in df["file_id"]]
out = pd.concat([df[["file_id", "Topic", "supertopic_1", "supertopic_2", "title", "Publication Year", "Authors", "DOI",
                     "in_synthesis", "synthesis_key", "cited_anywhere_key", "source", "pdf"]], pd.DataFrame(rows)], ignore_index=True)
out.to_csv(ROOT / "validation/corpus_manifest.csv", index=False)

print("topic-model documents:", len(df), "| in synthesis:", int(df.in_synthesis.sum()))
print("synthesis keys:", len(synth_keys), "| matched to corpus:", len(synth_keys) - len(unmatched))
print("unmatched synthesis keys:", unmatched)
print("complementary PDFs:", len(extra))
print(df.groupby("Topic").agg(n=("file_id", "size"), cited=("in_synthesis", "sum")).T.to_string())
