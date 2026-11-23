"""V2: reason why each topic-model document is not cited in the synthesis (first pass by Claude, 2026-11-11).

Codes
  DUP      duplicate record of another corpus document
  SURVEY   review or survey; used as context or comparator, not as primary evidence
  OOS      out of scope: no physical-layer security contribution for FSO / hybrid RF-FSO
  GAP      primary study on a theme that none of the 42 questions addresses
  NOTUSED  primary study on a theme that at least one question addresses, but not cited in the answer
Judgements are based on title and main research question; a sample is to be reviewed by a second rater.
"""
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(sys.argv[1])
R = {
 6:("GAP","jamming attacks"),24:("NOTUSED","PLS ST1 Q16-17 spatial diversity"),25:("OOS","network architecture, no PLS analysis"),
 35:("NOTUSED","PLS ST1 Q18 dual-hop RF-FSO"),46:("NOTUSED","Hybrid Q2 friendly jammer"),52:("NOTUSED","PLS ST1 Q8-9 relaying"),
 112:("OOS","FSO-UWOC tracking, no PLS analysis"),134:("DUP","duplicate of 024"),144:("NOTUSED","PLS ST1 Q10 relay networks"),
 9:("OOS","channel prediction, no security"),34:("NOTUSED","PLS ST1 Q1 eavesdropper outside beam"),37:("SURVEY","jamming review (cited in Introduction)"),
 56:("OOS","MAC layer challenges"),58:("GAP","encryption-based security"),63:("NOTUSED","PLS ST1 Q1 secure transmission probability"),
 94:("SURVEY","OAM communications review"),99:("NOTUSED","PLS ST1 Q6 channel estimation / CSI"),100:("GAP","polarization multiplexing"),
 103:("SURVEY","general FSO survey (comparator in Table 1)"),105:("NOTUSED","PLS ST1 Q4/Q6 eavesdropper geometry"),108:("GAP","public-key encryption"),
 111:("SURVEY","OWC survey"),114:("NOTUSED","PLS ST1 Q1 MIR vs NIR"),115:("SURVEY","jamming survey"),120:("NOTUSED","PLS ST1 Q1 channel correlation"),
 127:("GAP","experimental interception attack (fog scattering)"),128:("DUP","duplicate of 063"),130:("DUP","duplicate of 101"),
 131:("SURVEY","PLS in OWC survey (comparator in Table 1)"),133:("DUP","duplicate of 100"),141:("SURVEY","FSO PLS survey (comparator in Table 1)"),
 145:("DUP","duplicate of 034"),
 15:("NOTUSED","QKD Q1 practical FSO-QKD"),30:("NOTUSED","QKD / 6G Q2 FSO-QKD in V2X"),36:("NOTUSED","QKD Q2 CV-QKD key rates"),
 40:("OOS","THz QCL link, no security"),70:("NOTUSED","QKD Q1 entanglement QKD UAV"),118:("NOTUSED","QKD Q1 protocol comparison"),
 119:("NOTUSED","QKD Q1 error reconciliation"),
 75:("NOTUSED","PLS ST1 Q8-9 cooperative relaying"),132:("NOTUSED","PLS ST1 Q8-9 relay-assisted FSO"),
 3:("NOTUSED","Hybrid Q4-5 selection combining"),12:("GAP","satellite with optical feeder link"),42:("GAP","spectrum sharing / cognitive"),
 66:("NOTUSED","Hybrid Q4-5 eavesdropping modes"),82:("GAP","FSO-VLC hybrid"),102:("NOTUSED","PLS ST1 Q8-9 two-way relaying"),
 110:("NOTUSED","Hybrid Q4-5 eavesdropping strategies"),121:("NOTUSED","Hybrid Q4-5 secrecy capacity"),
 4:("GAP","covert communication"),38:("NOTUSED","6G Q1 learning-based beamforming"),54:("GAP","HAP / SAGIN with FSO-THz"),
 68:("GAP","HAP / SAGIN hybrid FSO-RF"),87:("GAP","HAP / SAGIN FSO-RF downlink"),92:("NOTUSED","Hybrid Q1 RIS RF-FSO"),
 60:("NOTUSED","AdvMod Q1 chaos shift keying"),
 7:("GAP","hybrid FSO-mmWave"),11:("GAP","hybrid FSO-mmWave"),53:("GAP","hybrid FSO-mmWave"),67:("GAP","hybrid FSO-mmWave"),
 78:("GAP","hybrid FSO-mmWave with index modulation"),26:("GAP","CDMA wiretap"),29:("GAP","CDMA hybrid fiber-FSO"),57:("GAP","OCDMA hybrid FSO-fiber"),
 14:("OOS","quantum satellite network control"),27:("NOTUSED","QKD Q2 ground-to-satellite CV-QKD"),143:("NOTUSED","QKD Q2 satellite CV-QKD"),
 33:("GAP","channel correlation and pointing error"),43:("GAP","mmWave RF-assisted FSO"),44:("NOTUSED","PLS ST1 Q8 variable-gain relaying"),
 45:("GAP","detection techniques"),76:("GAP","detection techniques"),113:("NOTUSED","PLS ST1 Q8 variable-gain relaying"),
 84:("NOTUSED","PLS ST1 Q16 multiuser trade-off"),126:("SURVEY","security-reliability survey"),
 96:("GAP","NOMA in SAGIN"),48:("GAP","energy harvesting"),50:("GAP","SWIPT"),51:("GAP","SWIPT"),73:("GAP","SWIPT"),
 135:("GAP","post-quantum cryptography"),18:("NOTUSED","PLS ST1 Q1 Malaga channels"),47:("NOTUSED","PLS ST1 Q1 Malaga channels"),
 80:("NOTUSED","PLS ST1 Q1 correlated Malaga"),81:("NOTUSED","PLS ST1 Q18 diversity combining"),124:("NOTUSED","Hybrid Q4 multi-user mixed RF-FSO"),
}
m = pd.read_csv(ROOT / "validation/corpus_manifest.csv")
u = m[m.source.str.startswith("WoS") & (m.in_synthesis.astype(str) != "True")].copy()
assert set(u.file_id.astype(int)) == set(R), set(u.file_id.astype(int)) ^ set(R)
u["code"] = u.file_id.astype(int).map(lambda i: R[i][0])
u["note"] = u.file_id.astype(int).map(lambda i: R[i][1])
u[["file_id", "Topic", "title", "code", "note"]].to_csv(ROOT / "validation/v2_exclusion_reasons.csv", index=False)
print(u.code.value_counts().to_string())
print(pd.crosstab(u.Topic.astype(int), u.code).to_string())
print(u[u.code == "GAP"].note.value_counts().to_string())
