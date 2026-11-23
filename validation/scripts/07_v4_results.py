"""V4 results: Claude's verdict for each (sentence, cited study) unit against the cited PDF (2026-11-11).

S = supported; P = partially supported (gist in source, but overgeneralised, intensified, or mixes content
from another cited study); U = unsupported, contradicted or misattributed.
Outputs: validation/v4_results.csv, validation/v4_summary.txt,
         validation/v4_rater_sample.xlsx (30 units, blind) + v4_rater_key.csv
"""
import math, os, sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1]); os.chdir(ROOT)
P_IDS = [1, 2, 3, 4, 6, 7, 10, 13, 17, 18, 21, 24, 26, 28, 29, 35, 37, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 62, 63, 64, 68, 73, 79, 82, 83, 86, 89, 99, 100, 102, 106, 109, 114, 115, 116, 117]
U_IDS = [5, 12, 16, 66, 75, 95, 96, 97]
L = "".join("U" if i in U_IDS else "P" if i in P_IDS else "S" for i in range(1, 121))
assert len(L) == 120, len(L)
NOTE = {
 5: "Sun2016 does not claim security is preserved under strong turbulence via mode decomposition",
 12: "Simulation in OptiSystem presented as practical demonstration over km-scale links",
 16: "Content belongs to Hu2020 (cooperative beamforming jamming vs zero forcing); Djordjevic2017a is OAM hybrid FSO-THz",
 66: "Nguyen2023 uses QPSK with DT/HD receivers, not OFDM",
 75: "Kamran2020 is a laboratory-style simulation; no turbulence or mobile platforms",
 95: "Narang2019: DCSK is non-coherent and needs no synchronization; claim contradicts source",
 96: "Verma2024: DCSK chosen precisely to avoid chaotic synchronization; claim contradicts source",
 97: "Guo2024: DCSK model; synchronization-based security mechanism not supported",
 2: "Djordjevic2016 duplicates Sun2016 (same title, different DOI)", 4: "Djordjevic2016 duplicates Sun2016", 7: "Djordjevic2016 duplicates Sun2016",
 17: "Hu2020 is mixed RF/FSO spectrum sharing, not hybrid optical-terahertz",
 21: "Misalignment-induced crosstalk at the eavesdropper comes from Dabiri2025, not Eghbal2014",
 45: "Overclaim 'one of the most effective'; correlation not in Zhang2020",
 54: "Gupta2025 studies outage, not secrecy", 55: "Hung2024 studies performance, not secrecy", 102: "Gupta2025 studies BER, not secrecy",
 62: "Nguyen2023 does not compare complexity with DV-QKD",
 82: "Energy conversion efficiency of jammers is Wang2023, not Ahmed2023",
 86: "Trajectory and delay-sensitive services are Zhang2024, not Liu2022",
}
fr = pd.read_csv("validation/v4_sample.csv")
fr["verdict"] = list(L)
fr["note"] = fr.claim_id.map(NOTE).fillna("")
fr.to_csv("validation/v4_results.csv", index=False)

def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d
n = len(fr); out = []
for lab, ks in [("supported (S)", "S"), ("partially supported (P)", "P"), ("unsupported (U)", "U"), ("S or P", "SP")]:
    k = fr.verdict.isin(list(ks)).sum(); lo, hi = wilson(k, n)
    out.append(f"{lab}: {k}/{n} = {k/n:.1%} (95% Wilson CI {lo:.1%}-{hi:.1%})")
out.append("\nBy section:\n" + pd.crosstab(fr.section, fr.verdict, margins=True).to_string())
out.append("\nExcluded from frame (no readable full text): Dabiri2025, Furqan2018WCMC, Huang2020JSAC, Khoshafa2025COMST, Lee2017IEEEAccess, Liu2018TCOM, Marzban2019TVT, Wu2025IEEE, Zeydan2025OJCOMS (10 units)")
Path("validation/v4_summary.txt").write_text("\n".join(out) + "\n"); print("\n".join(out))

u = fr[fr.verdict == "U"]; p = fr[fr.verdict == "P"].sample(10, random_state=42); s = fr[fr.verdict == "S"].sample(12, random_state=42)
r = pd.concat([u, p, s]).sample(frac=1, random_state=7).reset_index(drop=True)
r["rater_id"] = range(1, len(r) + 1)
r[["rater_id", "claim_id", "verdict"]].to_csv("validation/v4_rater_key.csv", index=False)
sheet = pd.DataFrame({"rater_id": r.rater_id, "claim": r.sentence.str.replace(r"\\cite\{[^}]*\}", "[cite]", regex=True),
                      "cited_study": r.key, "pdf": r.pdf, "your_verdict_S_P_U": "", "comment": ""})
with pd.ExcelWriter("validation/v4_rater_sample.xlsx") as w:
    pd.DataFrame({"instructions": ["Open the PDF of the cited study and judge the claim against that study only.",
        "S = supported: the study states it", "P = partially: gist present but overgeneralised, intensified, or mixed with another study",
        "U = unsupported, contradicted, or the content belongs to another study", "Work blind: do not open v4_results.csv or v4_rater_key.csv."]}).to_excel(w, sheet_name="README", index=False)
    sheet.to_excel(w, sheet_name="rate", index=False)
print("rater sample:", len(r))
