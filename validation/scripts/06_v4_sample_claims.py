"""V4: verify all cited claims (census; planned sample of 100 replaced because the frame has 120 readable units) from the Results synthesis of manuscript v9 and retrieve candidate passages.

Unit: one (sentence, cited study) pair. Sampling: stratified by supertopic subsection, proportional, seed 42.
Studies without a readable full text (RF-only external references, surveys outside the corpus,
one-page PDF of Dabiri2025) are excluded from the sampling frame and reported.
Outputs: validation/v4_frame.csv, validation/v4_sample.csv, validation/v4_passages.txt
"""
import os, re, subprocess, sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(sys.argv[1]); os.chdir(ROOT)
tex = Path("FSO_v9_NatureSR/FSO_NatureSR_main.tex").read_text()
tex = "\n".join(l for l in tex.splitlines() if not l.lstrip().startswith("%"))
res = tex.split(r"\subsection*{Physical Layer Security in FSO Communication}")[1].split(r"\section*{Discussion}")[0]
parts = re.split(r"\\subsection\*\{([^}]*)\}", r"\subsection*{Physical Layer Security in FSO Communication}" + res)[1:]

man = pd.read_csv("validation/corpus_manifest.csv")
pdf = {}
for _, r in man[man.synthesis_key.notna()].iterrows():
    for k in str(r.synthesis_key).split(";"):
        pdf[k] = r.pdf
EXTRA = {"Gupta2025NOMAFSO": "Investigation of Outage", "Djordjevic2017": "OAM-Based_Hybrid", "Djordjevic2017a": "OAM-based Physical-Layer",
         "Amhoud2021VTC": "OFDM with Index", "Gupta2025ICTExpress": "On the performance of a UAV", "Hung2024MixedRFFSO": "Performance analysis of dual-hop"}
for k, pre in EXTRA.items():
    pdf[k] = "data_extra/" + [f for f in os.listdir("data_extra") if f.startswith(pre)][0]

units = []
for title, body in zip(parts[::2], parts[1::2]):
    body = re.sub(r"\\begin\{(table|figure)\*?\}.*?\\end\{\1\*?\}", " ", body, flags=re.S)
    sents = re.split(r"(?<=[.])\s+(?=[A-Z])", re.sub(r"\s+", " ", body))
    for s in sents:
        for c in re.findall(r"\\cite\{([^}]*)\}", s):
            for k in [x.strip() for x in c.split(",")]:
                units.append({"section": title, "sentence": s.strip(), "key": k, "pdf": pdf.get(k, "")})
fr = pd.DataFrame(units).drop_duplicates(["sentence", "key"])
fr["readable"] = fr.pdf != ""
fr.to_csv("validation/v4_frame.csv", index=False)
print("units:", len(fr), "| readable:", int(fr.readable.sum()))
print("excluded keys:", sorted(fr[~fr.readable].key.unique()))
print(fr[fr.readable].groupby("section").size().to_string())

ok = fr[fr.readable].reset_index(drop=True)
alloc = (ok.groupby("section").size() / len(ok) * 100).round().astype(int)
while alloc.sum() != 100:
    alloc[alloc.idxmax() if alloc.sum() > 100 else alloc.idxmin()] += -1 if alloc.sum() > 100 else 1
samp = ok.copy()  # census: all 120 readable units (frame smaller than planned sample)
samp.insert(0, "claim_id", range(1, len(samp) + 1))
samp.to_csv("validation/v4_sample.csv", index=False)

STOP = set("the of and to in a an for with by on is are be as that this which from or at its their these can under than more".split())
def words(s): return [w for w in re.findall(r"[a-z0-9.%-]+", re.sub(r"\\cite\{[^}]*\}", "", s.lower())) if w not in STOP and len(w) > 2]
cache = {}
with open("validation/v4_passages.txt", "w") as f:
    for _, r in samp.iterrows():
        if r.pdf not in cache:
            t = re.sub(r"\s+", " ", subprocess.run(["pdftotext", r.pdf, "-"], capture_output=True, text=True).stdout)
            k = t.lower().rfind(" references "); cache[r.pdf] = t[:k] if k > len(t) * 0.5 else t
        t = cache[r.pdf]; q = set(words(r.sentence))
        wins = [t[i:i + 450] for i in range(0, max(1, len(t) - 450), 225)]
        top = sorted(wins, key=lambda w: -len(q & set(words(w))))[:2]
        claim = re.sub(r"\\cite\{[^}]*\}", "[c]", r.sentence)
        f.write(f"### C{r.claim_id} [{r.key}] ({r.section[:30]})\nCLAIM: {claim}\n")
        for w in top: f.write(f"  > {w}\n")
print("sample:", len(samp)); print(alloc.to_string())
