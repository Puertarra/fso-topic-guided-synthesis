"""T1: technique-by-assumption table for the studies cited in the synthesis (Claude, 2026-11-11).

Technique family and validation type are assigned by hand (validation checked against full-text cues:
own experimental setup / field trial vs OptiSystem-MATLAB simulation vs closed-form analysis).
Channel model, pointing error, CSI, metrics and reported costs come from keyword rules on the full PDF
body (references removed). Outputs: validation/t1_studies.csv, validation/t1_by_family.csv
"""
import json, os, re, subprocess, sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1]); os.chdir(ROOT)
raw = pd.read_csv("validation/t1_features_raw.csv")
cues = json.load(open("validation/t1_validation_cues.json"))
EXTRA = {"X-Investigation of Out": "Gupta2025NOMAFSO", "X-OAM-Based Optical Wi": "Dabiri2025",
         "X-OAM-Based_Hybrid_Fre": "Djordjevic2017", "X-OAM-based Physical-L": "Djordjevic2017a",
         "X-OFDM with Index Modu": "Amhoud2021VTC", "X-On the performance o": "Gupta2025ICTExpress",
         "X-Performance analysis": "Hung2024MixedRFFSO"}
raw["key"] = [EXTRA.get(i, k) for i, k in zip(raw.id, raw.key)]
raw["key"] = raw.key.str.split(";").str[0]

FAM = {
 "OAM / spatial modes": "Djordjevic2016 Djordjevic2017 Djordjevic2017a Amhoud2021VTC Dabiri2025",
 "Waveform, coding and chaos": "Wang2024 AbdElMottaleb2023 Narang2019 Elfiqi2019 Verma2024 Guo2024 Wu2024 Huang2018",
 "Beam control and RIS": "Eghbal2014 Tumma2024 Ahmed2023 Liu2021 Liu2024 Sun2024 Wang2023",
 "Relaying, jamming and hybrid RF-FSO": "Tonk2022 Tubail2020 Yang2018 Ai2019 Ai2020 Zhang2020 Odeyemi2019 Zhang2021 Erdogan2022 Hu2020 Lei2018 Lei2020 Saber2019 Pattanayak2022 Pattanayak2020a ElMalek2016 Islam2021 Zhang2024 Liu2022 Gupta2025NOMAFSO Hung2024MixedRFFSO Gupta2025ICTExpress",
 "Diversity, scheduling and artificial noise": "Monteiro2018 Sikri2021 Shakir2023 Shakir2021",
 "Quantum key distribution": "Kamran2020 Trinh2018 Vu2020 Vu2022 Vu2023 Nguyen2023 Alshaer2022 Ahmed2022 Zhao2019 Stathis2024 AlMohammed2024 Mahmud2021 Shaw2018",
 "Classical key agreement": "Endo2018 Wang2014 Sasaki2017",
 "6G and quantum-security outlooks": "Porambage2021 Gracia2022 Muheidat2022 Wang2022",
}
fam = {k: f for f, ks in FAM.items() for k in ks.split()}
EXPERIMENTAL = {"Stathis2024", "Endo2018", "Huang2018", "Sasaki2017", "Wu2024"}  # Wu2024: probable, to verify
OVERVIEW = {"Porambage2021", "Gracia2022", "Muheidat2022", "Wang2022", "Tumma2024"}
UNREADABLE = {"Dabiri2025"}  # one-page PDF

def pdfpath(i):
    if str(i).startswith("X-"):
        return [os.path.join("data_extra", f) for f in os.listdir("data_extra") if f.startswith(i[2:])][0]
    n = int(i); return f"data/{n:03d}.pdf" if n <= 125 else f"data2/{n:03d}.pdf"

PATS = {
 "gamma_gamma": r"gamma[- ]gamma", "malaga": r"m[aá]laga|m-distribut|\bm distribution", "log_normal": r"log[- ]?normal",
 "pointing_error": r"pointing error|misalignment|boresight",
 "imperfect_csi": r"imperfect csi|outdated csi|imperfect channel state|channel estimation error|outdated channel",
 "m_sop": r"secrecy outage", "m_asc": r"average secrecy capacity", "m_spsc": r"strictly positive secrecy",
 "m_ip": r"intercept(ion)? probability", "m_skr": r"secret key rate|key generation rate", "m_qber": r"\bqber\b|quantum bit error",
 "m_ber": r"\bber\b|bit error rate",
 "cost_complexity": r"computational complexity|complexity analysis|low[- ]complexity",
 "cost_energy": r"energy efficien|power consumption|energy consumption",
}
rows = []
for _, r in raw.iterrows():
    t = re.sub(r"\s+", " ", subprocess.run(["pdftotext", pdfpath(r.id), "-"], capture_output=True, text=True).stdout.lower())
    k = t.rfind(" references "); t = t[:k] if k > len(t) * 0.5 else t
    d = {"id": r.id, "key": r.key, "title": r.title, "family": fam.get(r.key, "UNASSIGNED")}
    c = cues[r.id]
    d["validation"] = ("unreadable" if r.key in UNREADABLE else "experimental" if r.key in EXPERIMENTAL
                       else "overview" if r.key in OVERVIEW else "analytical + numerical" if c["cf"] > 0
                       else "numerical simulation")
    for p, rx in PATS.items():
        d[p] = bool(re.search(rx, t))
    rows.append(d)
df = pd.DataFrame(rows)
assert (df.family != "UNASSIGNED").all(), df[df.family == "UNASSIGNED"].key.tolist()
df.to_csv("validation/t1_studies.csv", index=False)

prim = df[~df.validation.isin(["overview", "unreadable"])]
g = prim.groupby("family")
tab = pd.DataFrame({
 "studies": g.size(),
 "experimental": g.validation.apply(lambda s: (s == "experimental").sum()),
 "analytical+numerical": g.validation.apply(lambda s: (s == "analytical + numerical").sum()),
 "numerical only": g.validation.apply(lambda s: (s == "numerical simulation").sum()),
 "pointing error %": (g.pointing_error.mean() * 100).round(),
 "imperfect CSI %": (g.imperfect_csi.mean() * 100).round(),
 "Malaga %": (g.malaga.mean() * 100).round(), "Gamma-Gamma %": (g.gamma_gamma.mean() * 100).round(),
 "SOP %": (g.m_sop.mean() * 100).round(), "SKR/QBER %": ((g.m_skr.mean() + 0) * 100).round(),
 "complexity %": (g.cost_complexity.mean() * 100).round(), "energy %": (g.cost_energy.mean() * 100).round(),
})
tab.loc["All primary studies"] = [len(prim), (prim.validation == "experimental").sum(), (prim.validation == "analytical + numerical").sum(),
    (prim.validation == "numerical simulation").sum()] + [round(prim[c].mean() * 100) for c in
    ["pointing_error", "imperfect_csi", "malaga", "gamma_gamma", "m_sop", "m_skr", "cost_complexity", "cost_energy"]]
tab.to_csv("validation/t1_by_family.csv")
pd.set_option("display.width", 250)
print(tab.to_string())
print("\noverview:", df[df.validation == "overview"].key.tolist(), "| unreadable:", df[df.validation == "unreadable"].key.tolist())
