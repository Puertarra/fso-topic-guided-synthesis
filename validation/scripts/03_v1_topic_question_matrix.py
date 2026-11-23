"""V1: topic x question relevance matrix (first pass by Claude, 2026-11-11).

Score: 2 = the question targets the topic's central theme; 1 = it addresses a secondary aspect of the
topic's documents; 0 = unrelated. Topic descriptors: Mistral label, c-TF-IDF words, document titles.
Outputs: validation/v1_matrix.csv, validation/v1_summary.txt,
         validation/v1_rater_sample.xlsx (100 cells, blind, for the second rater) + v1_rater_key.csv
"""
import re, sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(sys.argv[1])
tex = (ROOT / "FSO_v9_NatureSR/FSO_NatureSR_main.tex").read_text()
app = tex.split(r"\section*{Supplementary Information")[1]
blocks = re.split(r"\\caption\{\\textbf\{Query Protocol for Supertopic (\d)", app)[1:]
Q = []
for st, body in zip(blocks[::2], blocks[1::2]):
    for n, q in re.findall(r"\n(\d+)\. (.+?) \\\\", body):
        Q.append((f"ST{st}-Q{int(n):02d}", q.strip()))
assert len(Q) == 42, len(Q)

S = {  # question -> {topic: score}; omitted topics score 0
 "ST1-Q01":{0:2,13:1,5:1}, "ST1-Q02":{0:2,13:1,5:1}, "ST1-Q03":{10:2,4:1}, "ST1-Q04":{0:1,4:1},
 "ST1-Q05":{3:1,4:1,14:1}, "ST1-Q06":{2:2,8:1}, "ST1-Q07":{0:1}, "ST1-Q08":{2:2,8:1,11:1,14:1},
 "ST1-Q09":{2:2,8:1,14:1}, "ST1-Q10":{2:2,4:1,9:1}, "ST1-Q11":{0:1}, "ST1-Q12":{0:1}, "ST1-Q13":{0:1},
 "ST1-Q14":{0:1}, "ST1-Q15":{0:1}, "ST1-Q16":{9:2,0:1,2:1}, "ST1-Q17":{3:1,9:1,14:1},
 "ST1-Q18":{2:2,8:1,14:1}, "ST1-Q19":{0:1,13:1},
 "ST2-Q01":{1:2,7:1,5:1}, "ST2-Q02":{7:2,1:1}, "ST2-Q03":{1:1}, "ST2-Q04":{1:1}, "ST2-Q05":{1:1,7:1},
 "ST2-Q06":{1:1}, "ST2-Q07":{1:1,7:1},
 "ST3-Q01":{10:2,4:1}, "ST3-Q02":{2:1,14:1}, "ST3-Q03":{4:2}, "ST3-Q04":{2:1,3:1,14:1}, "ST3-Q05":{3:2,6:1,0:1},
 "ST4-Q01":{5:2}, "ST4-Q02":{0:1}, "ST4-Q03":{0:1}, "ST4-Q04":{0:1}, "ST4-Q05":{10:2}, "ST4-Q06":{10:2},
 "ST4-Q07":{10:1}, "ST4-Q08":{10:1,4:1}, "ST4-Q09":{10:1},
 "ST5-Q01":{4:1,6:1,12:1}, "ST5-Q02":{12:2,1:1},
}
assert set(S) == {q for q, _ in Q}
M = pd.DataFrame(0, index=[q for q, _ in Q], columns=range(15))
for q, d in S.items():
    for t, s in d.items():
        M.loc[q, t] = s
M.to_csv(ROOT / "validation/v1_matrix.csv")

man = pd.read_csv(ROOT / "validation/corpus_manifest.csv")
wos = man[man.source.str.startswith("WoS") & (man.Topic >= 0)]
cit = wos.groupby("Topic").in_synthesis.agg(lambda s: (s.astype(str) == "True").sum())
n = wos.groupby("Topic").size()
direct = (M == 2).any(axis=0)
lines = [
 f"Topics with >=1 direct question: {int(direct.sum())}/15 -> {list(M.columns[direct])}",
 f"Topics with only partial questions: {list(M.columns[~direct & (M >= 1).any(axis=0)])}",
 f"Topics with no question: {list(M.columns[~(M >= 1).any(axis=0)])}",
 f"Questions anchored (>=1 direct topic): {int((M == 2).any(axis=1).sum())}/42",
 f"Questions with no direct topic: {list(M.index[~(M == 2).any(axis=1)])}",
 f"Cited share, topics with direct question: {int(cit[direct].sum())}/{int(n[direct].sum())}",
 f"Cited share, topics without direct question: {int(cit[~direct].sum())}/{int(n[~direct].sum())}",
 f"Non-zero cells: {int((M > 0).sum().sum())} (score 2: {int((M == 2).sum().sum())}, score 1: {int((M == 1).sum().sum())})",
]
(ROOT / "validation/v1_summary.txt").write_text("\n".join(lines) + "\n")
print("\n".join(lines))

# Blind sample for the second rater: all score-2 cells, 30 score-1 cells, rest score-0, stratified by topic
rng = np.random.default_rng(42)
cells = M.stack().rename("score").reset_index().rename(columns={"level_0": "question", "level_1": "topic"})
s2 = cells[cells.score == 2]
s1 = cells[cells.score == 1].sample(30, random_state=42)
k0 = 100 - len(s2) - len(s1)
s0 = cells[cells.score == 0].groupby("topic", group_keys=False).apply(lambda g: g.sample(min(len(g), 4), random_state=42))
s0 = s0.sample(k0, random_state=42)
samp = pd.concat([s2, s1, s0]).sample(frac=1, random_state=7).reset_index(drop=True)
samp["cell_id"] = range(1, len(samp) + 1)
samp[["cell_id", "question", "topic", "score"]].to_csv(ROOT / "validation/v1_rater_key.csv", index=False)

topics = pd.read_pickle(ROOT / "topics/topics_documents_0218.pkl")
comb = pd.read_pickle(ROOT / "src/df_combined2.pkl")
topics["title"] = comb.Title.values
desc = {}
for t, g in topics[topics.Topic >= 0].groupby("Topic"):
    lab = g.Mistral.iloc[0][0] if isinstance(g.Mistral.iloc[0], (list, tuple)) else str(g.Mistral.iloc[0])
    desc[t] = f"{lab} | e.g.: " + " ; ".join(g.title.head(4).str[:80])
qtext = dict(Q)
sheet = pd.DataFrame({"cell_id": samp.cell_id, "question_id": samp.question,
                      "question": samp.question.map(qtext), "topic_id": samp.topic,
                      "topic_description": samp.topic.map(desc), "your_score_0_1_2": ""})
with pd.ExcelWriter(ROOT / "validation/v1_rater_sample.xlsx") as w:
    pd.DataFrame({"instructions": [
        "Score how much the question targets the topic.",
        "2 = the question targets the topic's central theme",
        "1 = the question addresses a secondary aspect of the topic's documents",
        "0 = unrelated",
        "Work blind: do not open v1_matrix.csv or v1_rater_key.csv."]}).to_excel(w, "README", index=False)
    sheet.to_excel(w, "rate", index=False)
print("sample:", len(samp), "| score2", len(s2), "score1", len(s1), "score0", k0)
