# Q1 — Practical constraints of quantum integration in FSO (responds to IEEE Access R1.2)

Prepared by Claude, 2026-11-11. Sources: PDFs of the cited studies (key figures checked against the full text) and the structured extraction records. Draft for author review.

## Evidence table

| Study | Scheme | Link scenario | Validation | Reported figures | Main constraint stated or evident |
|---|---|---|---|---|---|
| Stathis2024 | DS-BB84, polarisation, COTS components | 40 m indoor and 100 m outdoor FSO; 2.2 km campus fibre | Experimental (measured noise and loss fed to a semi-empirical model) | QBER < 3.2 % on FSO; expected SKR up to 600 bps (FSO) and 300 bps (fibre coexistence) | Raman and background noise; SKR is an expected value, not a measured key |
| Alshaer2022 | CV-QKD, DP-QPSK, UAV-to-ground | UAV FSO link | Analytical + Monte Carlo | Design target QBER 10^-3 and outage 10^-2; tolerates boresight displacement up to 7 cm | Alignment, angle-of-arrival fluctuation, UAV position jitter |
| Vu2020 | QKD via HAP relay to moving vehicle | Satellite–HAP–vehicle | Analytical + simulation | QBER and ergodic key rate acceptable under moderate turbulence | Misalignment, receiver mobility, amplifier settings at the relay |
| Vu2022 | Entanglement-based BBM92 with dual-threshold direct detection | LEO satellite to ground (Japan case study) | Analytical | Lower receiver complexity than coherent detection | Channel loss, turbulence-induced fading |
| Vu2023 | CV-QKD with DT/DD, GEO source and LEO relays | Global network (Japan case study) | Analytical + Monte Carlo | Robust to untrusted-relay and beam-splitting attacks by design | Spreading loss, turbulence, relay trust |
| Nguyen2023 | Entanglement-based CV-QKD, QPSK, DT/heterodyne detection | Satellite to ground, Fisher–Snedecor F turbulence | Analytical + numerical | Optimal aperture, threshold and divergence settings | Receiver design, turbulence |
| Trinh2018 | SIM-BPSK QKD with dual-threshold direct detection | Terrestrial FSO | Closed form + Monte Carlo | Closed-form QBER and key rates | Modulation depth and threshold selection |
| Ahmed2022 | CV-QKD with local local oscillator, Gaussian vs discrete modulation | Terrestrial, weak turbulence | Numerical | Gaussian modulation reaches longer distance; phase attacks degrade SKR faster than amplitude attacks | Phase-reference vulnerability |
| Zhao2019 | OFDM-based CV-QKD | Satellite to ground | Monte Carlo | Higher SKR within a range of subcarrier numbers | Device limits on symbols per subcarrier break asymptotic assumptions |
| Kamran2020 | KMB09, high-order Gaussian spatial modes | Terrestrial FSO | Simulation | Efficiency 0.25 (2-D) and 0.368 (4-D) | Requires SLMs and mode sorting |
| AlMohammed2024 | QKD integrated with FSO for high-speed trains | Ground-to-train | Simulation (MATLAB) | Key exchange with small throughput penalty | Alignment to moving trains, visibility |
| Mahmud2021 / Shaw2018 | QKD to exchange chaotic-system parameters | AWGN channel model | Simulation (MATLAB) | Error-free image recovery at low SNR | No turbulent FSO channel modelled |
| Endo2018 (classical) | Secret key agreement with wiretap-channel certification | 7.8 km Tokyo FSO testbed | Experimental | Final key rates 100 kbps–7.77 Mbps with total losses above 55 dB | Security rests on estimated eavesdropper channel (probing station) |
| Sasaki2017 (classical) | Physical-layer security in a quantum photonic network | 7.8 km FSO wiretap testbed | Experimental | Mbps-scale secure rates at −60 dB channel attenuation; secrecy rate fluctuates with turbulence | Same assumption on the eavesdropper's channel |

## Counts
- Quantum key distribution studies: 13; with own experiment: 1 (Stathis2024). Two of the 13 (Mahmud2021, Shaw2018) model an AWGN channel rather than a turbulent FSO channel.
- No study in the corpus demonstrates OAM-based or high-dimensional QKD experimentally; Kamran2020 is simulation only.
- Note for the methods: the LLM-extracted records describe AlMohammed2024, Mahmud2021 and Shaw2018 as "experiments"; the PDFs show MATLAB simulations. This is an extraction error that the verification step must catch.

## Draft paragraph (for Results or Discussion, replaces the qualitative QKD limitations text)

The practical maturity of quantum integration in FSO is markedly lower than its analytical treatment suggests. Of the 13 QKD studies in the synthesis, only one reports its own measurements: a polarisation-encoded decoy-state BB84 system built from commercial components, operated over 40 m indoor and 100 m outdoor links, with QBER below 3.2% and an expected secret-key rate of up to 600 bps \cite{Stathis2024}. The remaining studies are analytical or simulation-based, and two of them model an additive white Gaussian noise channel rather than a turbulent optical link \cite{Mahmud2021,Shaw2018}. By contrast, classical secret-key agreement over a 7.8 km terrestrial testbed reached final key rates of 100 kbps to 7.77 Mbps under total losses above 55 dB \cite{Endo2018,Sasaki2017}, at the cost of security guarantees that depend on an estimate of the eavesdropper's channel rather than on quantum principles. Satellite and aerial designs shift the difficulty to the receiver and the pointing subsystem: dual-threshold direct detection is proposed to avoid the complexity of coherent receivers \cite{Vu2022,Vu2023}, and UAV-based CV-QKD tolerates boresight displacement only up to about 7 cm \cite{Alshaer2022}. Security analyses remain largely asymptotic, and device-level threats such as phase attacks on the local oscillator reference degrade the key rate faster than amplitude attacks \cite{Ahmed2022}. Finally, no study in the corpus demonstrates OAM-based or high-dimensional QKD over a real link; the only spatial-mode implementation is a simulation that assumes spatial light modulators and mode sorting \cite{Kamran2020}. Closing the gap between hundreds of bits per second over short quantum links and megabits per second over kilometre-scale classical key agreement is therefore the central practical challenge for quantum-secured FSO.
