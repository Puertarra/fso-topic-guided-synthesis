"""T1: extract assumption features for the studies cited in the synthesis.

Sources: structured records (Methods and Experiments, Results, Conclusions) for corpus studies;
first 2 and last 2 pages of the PDF for the complementary studies in data_extra/.
Keyword rules give a first pass; technique and validation type are then reviewed by hand.
Output: validation/t1_features_raw.csv
"""
import re, subprocess, sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1])
man = pd.read_csv(ROOT / "validation/corpus_manifest.csv")
comb = pd.read_pickle(ROOT / "src/df_combined2.pkl")

RULES = {
 "turbulence": {"gamma-gamma": r"gamma[- ]?gamma|\bgg\b", "malaga": r"m[aá]laga|\bm[- ]distribut", "log-normal": r"log[- ]?normal",
                "exp-weibull": r"exponentiated weibull", "F-dist": r"f[- ]distribution", "double GG/other": r"double generalized|gamma[- ]gamma.*?pointing"},
 "pointing_error": {"yes": r"pointing error|misalignment|boresight|jitter"},
 "csi": {"imperfect/outdated": r"imperfect csi|outdated csi|imperfect channel|channel estimation error|outdated channel",
         "perfect": r"perfect csi|full csi|instantaneous csi"},
 "eavesdropper": {"RF-link Eve": r"eavesdropper.{0,40}rf|rf.{0,40}eavesdrop", "FSO-link Eve": r"eavesdropper.{0,60}(fso|optical|beam)",
                  "multiple Eves": r"multiple eavesdroppers|multi-eavesdropper|colluding"},
 "metric": {"SOP": r"secrecy outage|\bsop\b", "ASC": r"average secrecy capacity|\basc\b", "SPSC": r"strictly positive|\bspsc\b",
            "secrecy rate/capacity": r"secrecy (rate|capacity)", "EST": r"effective secrecy throughput", "intercept prob.": r"intercept(ion)? probability",
            "BER": r"\bber\b|bit error", "SKR": r"secret key rate|key rate|\bskr\b", "QBER": r"\bqber\b|quantum bit error"},
 "validation": {"experimental": r"\bexperiment(al|ally)? (setup|test|demonstrat|result|investigat)|testbed|field trial|measured|laboratory|prototype",
                "simulation": r"monte[- ]carlo|simulat", "analytical": r"closed[- ]form|analytical(ly)? (expression|derivation|framework|model)|derive"},
 "cost_reported": {"complexity": r"complexit", "energy/power": r"energy efficien|power consumption|energy consumption", "hardware": r"hardware|spatial light modulator|slm\b|detector"},
}

def text_pdf(p):
    out = []
    for args in (["-l", "2"], ["-f", "-2"]):
        pass
    n = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout
    pages = int(re.search(r"Pages:\s+(\d+)", n).group(1)) if "Pages" in n else 4
    t1 = subprocess.run(["pdftotext", "-l", "2", str(p), "-"], capture_output=True, text=True).stdout
    t2 = subprocess.run(["pdftotext", "-f", str(max(1, pages - 1)), str(p), "-"], capture_output=True, text=True).stdout
    return t1 + " " + t2

rows = []
syn = man[man.in_synthesis.astype(str) == "True"]
for _, r in syn.iterrows():
    k = f"{int(r.file_id):03d}"
    c = comb.loc[k]
    txt = " ".join(str(c[f]) for f in ["Methods and Experiments", "Results", "Conclusions"])
    rows.append({"id": k, "key": r.synthesis_key, "topic": int(r.Topic), "title": r.title, "text": txt})
for p in sorted((ROOT / "data_extra").glob("*.pdf")):
    if "Friendly Jammer" in p.name:
        continue
    rows.append({"id": "X-" + p.stem[:20], "key": "", "topic": None, "title": p.stem, "text": text_pdf(p)})

out = []
for r in rows:
    t = re.sub(r"\s+", " ", r["text"].lower())
    d = {k: r[k] for k in ("id", "key", "topic", "title")}
    for field, pats in RULES.items():
        d[field] = ";".join(lab for lab, pat in pats.items() if re.search(pat, t))
    out.append(d)
df = pd.DataFrame(out)
df.to_csv(ROOT / "validation/t1_features_raw.csv", index=False)
pd.set_option("display.width", 250)
for _, d in df.iterrows():
    print(f"{d.id[:12]:12}|{str(d.key)[:16]:16}|{d.title[:60]:60}|V:{d.validation}|T:{d.turbulence}|PE:{d.pointing_error}|CSI:{d.csi}|M:{d.metric}")
