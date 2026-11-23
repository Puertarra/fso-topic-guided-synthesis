## Supertopic 1: Physical Layer Security in FSO Communication

❓ **Question 1: Which optical modulation schemes (e.g., DPSK, PPM, OAM)
provide the highest secrecy capacity against eavesdropping under weak
and strong atmospheric turbulence?**

IMPROVED SUMMARY: In their seminal work, Sun et al. (2016) delve into
the realm of enhancing physical-layer security in Free-Space Optical
(FSO) communications via Orbital Angular Momentum (OAM) multiplexing.
This study rigorously examines how atmospheric turbulence influences the
propagation dynamics of OAM-multiplexed beams. Through detailed
numerical simulations that employ modified Kolmogorov phase screens,
various atmospheric turbulence conditions are modeled to assess their
impact on beam orthogonality and inter-channel crosstalk. The research
highlights that while OAM multiplexing can substantially elevate the
secrecy capacity in FSO communications under weak to medium turbulence
scenarios, strong turbulence significantly disrupts the orthogonality of
OAM modes. This disruption results in heightened crosstalk which
detrimentally affects the secrecy capacity.

Furthermore, Sun et al. (2016) explore different power allocation
strategies within these communication systems—specifically comparing
fixed system power and equal channel power allocations. Their findings
indicate that a fixed system power strategy tends to mitigate some of
the adverse effects seen under strong turbulence conditions better than
an equal channel power strategy does. This aspect of power allocation
emerges as a critical factor in maintaining optimal performance and
enhancing security capabilities in turbulent atmospheric conditions.

The numerical simulations detailed in this study are pivotal for
understanding the specific behaviors and interactions of OAM-multiplexed
beams under varied environmental influences. These simulations provide a
quantitative foundation for assessing how different power allocations
influence both crosstalk levels and overall system performance.

Complementing this, Lopez-Martinez et al. (2015) provide insights into
the vulnerabilities inherent in FSO communications due to atmospheric
turbulence and eavesdropping risks. Their analysis reveals that
physical-layer security can be significantly compromised by an
eavesdropper, especially when located near the transmitter where signal
attenuation is more pronounced \[Lopez-Martinez et al., 2015\]. The
study uses stochastic models like log-normal and Gamma-Gamma
distributions to represent weak to strong turbulence conditions,
offering novel closed-form expressions for the probability of strictly
positive secrecy capacity across common FSO propagation models.

Lopez-Martinez et al. (2015) also emphasize the critical impact of
eavesdropper proximity and intercepted power on secure communication
probabilities, highlighting that even minimal power capture by an
eavesdropper can lead to substantial security breaches \[Lopez-Martinez
et al., 2015\]. This underscores the necessity for robust security
measures that consider both atmospheric turbulence and beam divergence
characteristics.

Building on these insights, Wang et al. (2014) introduce a novel
approach to enhance FSO communication security through secret sharing
and key agreement protocols based on subcarrier intensity-modulated
air-to-ground FSO system models. Their study confirms scintillation
reciprocity under practical assumptions and develops key management
strategies that leverage statistics from atmospheric-turbulence-induced
fading channels measured under gamma-gamma models \[Wang et al., 2014\].
Notably, their findings demonstrate that the secret key rate is
primarily influenced by per-symbol signal-to-noise ratio and training
sequence length rather than atmospheric turbulence strength \[Wang et
al., 2014\]. This suggests that optimizing these parameters could
significantly enhance security performance in FSO systems, providing
resilience against eavesdropping without solely focusing on mitigating
atmospheric effects.

Ai et al. (2020) further expand our understanding by analyzing physical
layer security over Málaga channels in FSO communications under various
eavesdropping scenarios using intensity modulation/direct detection
methods \[Ai et al., 2020\]. Their comprehensive study reveals that
proximity of an eavesdropper to the transmitter has a less significant
impact on secrecy performance compared to other positions due to
specific channel correlations \[Ai et al., 2020\]. They also find that
correlation between channels can either enhance or deteriorate secrecy
performance depending on its level, showing a non-monotonic relationship
with performance metrics \[Ai et al., 2020\]. Moreover, Ai et al. (2020)
highlight that managing these parameters effectively can significantly
influence the effectiveness of security measures in FSO systems.

Endo et al. (2016) contribute valuable experimental data from a
metropolitan terrestrial FSO link testbed used to emulate typical
satellite-to-ground laser communications scenarios \[Endo et al.,
2016\]. Their findings emphasize how varying atmospheric conditions,
particularly fading effects due to turbulence, significantly affect
secrecy rates and secure transmission probabilities \[Endo et al.,
2016\]. Under stable conditions, effective message transmission with
reasonable code lengths is achievable; however, under strong fading
conditions, significant fluctuations in secrecy rates necessitate
adaptive strategies or long-span codes for maintaining security \[Endo
et al., 2016\]. The study underscores the importance of integrating
physical layer security with upper-layer algorithmic measures within a
multi-layer security architecture to combat sophisticated attacks
effectively \[Endo et al., 2016\].

Together, these studies underscore the complexity of maintaining high
secrecy capacity in FSO communications under varying environmental and
adversarial conditions, advocating for advanced techniques such as
dynamic beam shaping and adaptive modulation schemes to counteract these
challenges effectively.

❓ **Question 2: Provide comparative performance metrics (BER, secrecy
capacity, symbol error rate, SNR thresholds) for DPSK, PPM, and OAM
modulation schemes under different turbulence regimes.**

IMPROVED SUMMARY: The comprehensive study by Saber et al. (2017)
explores secure Free-Space Optical (FSO) communications through an
analytical lens, focusing on how Málaga (M) turbulence impacts key
security metrics such as secrecy capacity, secrecy outage probability,
and strictly positive secrecy capacity. By integrating theoretical
analysis with Monte-Carlo simulations, the research derives essential
closed-form expressions considering factors like intensity
modulation/direct detection (IM/DD) and pointing errors. The utilization
of the Málaga model, which integrates features from both log-normal and
Generalized-K distributions, effectively represents atmospheric
turbulence in their analysis. Results from this study reveal that
improvements in average SNR of the main channel significantly enhance
security performance metrics. Additionally, enhanced pointing accuracy
directly correlates with a reduced secrecy outage probability, while
lower turbulence intensity boosts strictly positive secrecy capacity
\[Saber et al., 2017\].

Building upon these findings, Abd El-Mottaleb et al. (2023) introduce a
novel approach to FSO transmission that incorporates an identity column
shift matrix (ICSM) code with a 4-level quadrature amplitude modulation
(4-QAM) scheme and orthogonal frequency division multiplexing (OFDM)
modulator to enhance both security and capacity. This system is tested
under various atmospheric conditions including turbulence and
attenuation, using real meteorological data from Alexandria, Jeddah, and
Hyderabad. The results demonstrate that increased atmospheric turbulence
leads to higher bit error rates (BER) and lower received optical power
(ROP), significantly affecting data reception quality. Under clear sky
conditions, the system achieved a maximum FSO range of 12.5 km with a
log (BER) of approximately -2.5 and an ROP of -9.5 dBm; however, under
strong turbulence at a distance of 0.8375 km, the log (BER) deteriorates
to -0.5 \[Abd El-Mottaleb et al., 2023\].

Monteiro et al. (2019) further enrich our understanding by analyzing the
effective secrecy throughput (EST) in relay-assisted FSO communications
under different weather conditions and eavesdropping scenarios. Their
study employs a theoretical analysis and simulation of a relay-assisted
FSO system featuring multiple paths between Alice and Bob, each with
multiple relays. Two transmission schemes are analyzed: an adaptive
scheme with selective relaying utilizing instantaneous CSI for optimal
path selection, and a fixed-rate scheme with all-active relaying without
access to instantaneous CSI. The results indicate that both transmission
schemes benefit from the use of multiple hops; however, the adaptive
scheme shows additional benefits from the use of multiple paths as it
reduces the likelihood of eavesdroppers being on the optimal path
\[Monteiro et al., 2019\].

Expanding on these insights into multiuser configurations in FSO
systems, Shakir et al. (2023) investigate the impact of opportunistic
transmit aperture selection (TAS) on the security-reliability trade-off
in MU-MIMO systems under generalized Malaga-M turbulence channels. Their
statistical analysis reveals that TAS significantly enhances security
metrics such as average bit error rate and intercept probability by
selecting the kth best user based on SNR distributions derived for
MU-MIMO channels experiencing atmospheric turbulence and nonzero
boresight pointing errors. This approach not only improves performance
metrics but also effectively manages the security-reliability trade-off
\[Shakir et al., 2023\].

Incorporating findings from Boluda-Ruiz et al. (2019), we delve into how
external eavesdroppers with generic locations and orientations impact
FSO communication systems' secrecy performance under gamma-gamma
turbulence conditions compounded by pointing errors. The introduction of
a new misalignment error model accounts for non-orthogonal optical beams
at eavesdroppers' receivers characterized by rotated ellipse effective
areas. This model provides new insights into how higher SNR at
eavesdropper's channels and larger normalized beamwidths at
receiver-side adversely affect secrecy performance \[Boluda-Ruiz et al.,
2019\].

These studies collectively highlight advanced strategies for enhancing
FSO communication systems' performance across diverse environmental
conditions while managing security risks effectively. Future research
directions might include integrating advanced modulation techniques like
OAM multiplexing and adaptive optics to further bolster both security
and reliability under diverse atmospheric conditions \[Saber et al.,
2017; Abd El-Mottaleb et al., 2023; Monteiro et al., 2019; Shakir et
al., 2023; Boluda-Ruiz et al., 2019\].

❓ **Question 3: How do RIS-assisted FSO systems improve secrecy
capacity compared to conventional reflectors, and what phase-shift
optimization methods are most effective?**

IMPROVED SUMMARY: Monteiro et al. (2019) provide a detailed analysis of
relay-assisted free-space optical (FSO) communications, focusing on how
multiple relays and paths can enhance effective secrecy throughput (EST)
under various atmospheric conditions. They compare two transmission
schemes: an adaptive scheme that utilizes selective relaying based on
real-time channel state information (CSI), and a fixed-rate scheme that
operates without CSI. The adaptive scheme significantly improves EST by
dynamically selecting the most secure paths, thus effectively minimizing
eavesdropper access compared to the fixed-rate scheme. This comparison
highlights the importance of adaptive transmission methods in
maintaining operational efficacy under diverse environmental conditions.

Additionally, Monteiro et al. (2019) explore the secrecy outage
probability (SOP), which measures the likelihood that the secrecy
capacity falls below a threshold, thereby compromising secure
communication. Their findings reveal that adverse weather conditions,
such as light fog with strong turbulence, increase SOP rates, especially
over extended distances. However, the use of multiple relays can
mitigate this risk by providing alternative transmission routes that
avoid heavily eavesdropped paths.

Incorporating insights from Ai et al. (2019), the study extends to
hybrid satellite-FSO cooperative systems where physical layer security
is critically examined. Ai et al. (2019) model the satellite link using
a shadowed-Rician fading distribution and the terrestrial FSO link with
a gamma-gamma fading distribution. They analyze the impact of different
detection techniques—heterodyne detection and intensity modulation with
direct detection—and pointing errors on secrecy performance. Their
research derives analytical expressions for average secrecy capacity and
SOP for both amplify-and-forward (AF) and decode-and-forward (DF)
relaying strategies. Notably, they find that in an AF scheme with fixed
gain, the secrecy diversity order is solely dependent on the FSO link's
channel characteristics and the detection technique used, whereas it is
zero when employing DF or AF with variable-gain schemes.

Erdogan et al. (2022) further contribute to this field by examining
mixed RF-FSO relay networks, emphasizing how physical characteristics
such as photo-aperture size and placement are crucial for enhancing
secrecy performance under harsh weather conditions. They integrate
Nakagami-m fading for RF channels and exponentiated Weibull distribution
for FSO channels to provide a deeper understanding of channel behavior
essential for optimizing network design against eavesdropping attacks.

Zhong et al. (2024) add to this body of knowledge by comparing
mid-infrared (MIR) and near-infrared (NIR) FSO systems in terms of
physical-layer security under varying atmospheric conditions including
turbulence, attenuation, and visibility. Their theoretical analysis
demonstrates that MIR systems offer superior physical-layer security
compared to NIR systems due to their higher secrecy capacity and
significantly lower interception probability.

Lei et al. (2018) delve into mixed RF-FSO systems with imperfect CSI
using a single-input multiple-output wiretap model where maximal ratio
combining is employed to enhance SNR despite channel imperfections such
as misalignment and imperfect CSI on both RF and FSO links. Their study
reveals significant degradation in secrecy outage performance due to
these imperfections, highlighting the sensitivity of system performance
to detection schemes and relaying strategies \[Lei et al., 2018\].
Theoretical derivations include CDFs and PDFs for FSO links with
pointing errors under different detection technologies, providing
closed-form expressions for SOP's lower bounds in both fixed-gain and
variable-gain relaying schemes \[Lei et al., 2018\]. Asymptotic
behaviors of SOP are explored using Meijer<span dir="rtl">’</span>s
G-function as electrical SNR approaches infinity \[Lei et al., 2018\].

\[Zhang et al., 2020\] enrich this discourse by analyzing an asymmetric
dual-hop RF-FSO communication system enhanced by multi-aperture
techniques against eavesdropping threats. Employing partial relay
selection based on maximum instantaneous channel gain for RF links and
equal gain combining at destinations significantly boosts system
robustness under diverse atmospheric disturbances. This study provides
critical insights into how advanced relay selection mechanisms can be
integrated into existing systems to fortify physical layer security
effectively.

This comprehensive examination underscores the critical role of advanced
transmission schemes and system configurations in optimizing FSO systems
for performance and security across various operational conditions.
Future studies should focus on exploring adaptive relaying strategies
that dynamically adjust based on channel state information from both
satellite and FSO links, as well as integrating advanced detection
techniques and mitigating pointing errors to further enhance the secrecy
performance of hybrid satellite-FSO systems.

❓ **Question 4: What adaptive beamforming algorithms are currently used
to steer FSO beams securely toward legitimate receivers in turbulent
channels?**

IMPROVED SUMMARY: In their comprehensive analysis, Hu et al. (2020)
delve into optimizing secrecy rates within mixed RF/FSO spectrum sharing
networks under the threat of eavesdropping activities. The study
introduces three innovative schemes designed to bolster physical-layer
security: direct transmission, single-user cooperative jamming, and
multi-user cooperative beamforming jamming. Each scheme is tailored to
mitigate potential security breaches effectively. The channel behavior
is meticulously modeled using Rayleigh distributions for RF links and
Gamma-Gamma distributions for FSO links, incorporating pointing errors
which significantly influence system performance under various
atmospheric conditions. These channel models are critical as they
directly impact the design and efficacy of security measures in wireless
communication systems.

To address complex nonconvex optimization challenges presented by these
scenarios, different mathematical approaches are employed. The
Dinkelbach method is applied to simpler schemes such as direct
transmission and single-user cooperative jamming, facilitating an
efficient resolution of optimization issues. For more complex scenarios
involving multi-user settings, a two-level optimization strategy
enhanced by semi-definite relaxation (SDR) is adopted. This advanced
method not only solves the optimization problems effectively but also
proves its optimality through rigorous Karush-Kuhn-Tucker conditions
analysis.

The validity and performance of these proposed schemes are further
corroborated through detailed simulation studies. These simulations are
crucial as they provide empirical evidence supporting theoretical
predictions regarding the superiority of multi-user cooperative
beamforming jamming over other techniques like zero-forcing beamforming
in terms of achieving higher secrecy rates.

Adding to this framework, Eghbal et al. (2014) introduce a novel
approach using acousto-optic deflectors (AODs) with synthetic
holographic gratings for manipulating beam paths in FSO systems to
enhance security dynamically based on atmospheric conditions. By varying
the AOD parameters, the Gaussian beam is transformed into a secondary
Gaussian Schell-model (GSM) beam with adjustable characteristics such as
radius and intensity, which are crucial for maintaining secure
communication under varying atmospheric turbulence. This method
effectively reduces the probability of eavesdropping by controlling
these parameters, thereby enhancing link security.

Boluda-Ruiz et al. (2019) contribute significantly by introducing a new
misalignment error model that accounts for non-orthogonal optical beams
at the eavesdropper's receiver, characterized by a rotated ellipse
effective area. This model is essential for analyzing the secrecy outage
probability (SOP) under gamma-gamma turbulence conditions with pointing
errors. Their findings reveal that the secrecy performance deteriorates
significantly when the eavesdropper's receiver aligns such that the
optical beam becomes orthogonal to the photodetector plane. Moreover,
higher SNR at the eavesdropper's channel and larger normalized beamwidth
at the receiver-side adversely affect the secrecy performance,
emphasizing the critical role of eavesdropper<span dir="rtl">’</span>s
location and orientation in determining FSO system security.

Incorporating insights from Saber et al. (2017), we further understand
how Málaga turbulence model impacts secure FSO communications. Their
study provides closed-form expressions for average secrecy capacity,
secrecy outage probability, and strictly positive secrecy capacity over
Málaga turbulence channels considering intensity modulation/direct
detection (IM/DD) and pointing errors \[Saber et al., 2017\]. The
results demonstrate that improved pointing accuracy and reduced
turbulence intensity significantly enhance these metrics, confirming
that Málaga model is an effective tool for predicting secure FSO link
performance under various atmospheric conditions \[Saber et al., 2017\].

The recent study by Shakir et al. (2023) introduces opportunistic
transmit aperture selection (TAS) in multiuser MIMO FSO communications
under generalized Malaga-M turbulence channels \[Shakir et al., 2023\].
This approach significantly enhances security and reliability while
managing the trade-off between them effectively \[Shakir et al., 2023\].
By selecting the kth best user with the highest SNR through statistical
analysis of TAS combined SNR distributions, this method not only
improves performance metrics such as outage probability and bit error
rate but also effectively mitigates risks associated with eavesdropping
and signal degradation due to turbulence \[Shakir et al., 2023\]. The
integration of TAS with MU-MIMO configurations shows potential in
addressing existing challenges in FSO communications \[Shakir et al.,
2023\].

Overall, this research by Hu et al. (2020), alongside contributions from
Eghbal et al. (2014), Boluda-Ruiz et al. (2019), Saber et al. (2017),
Shakir et al. (2023), highlights the critical role of advanced
optimization techniques, robust channel modeling, innovative
misalignment error models, effective turbulence modeling in securing
free-space optical communications against eavesdropping threats while
enhancing system capacity through sophisticated coding and modulation
strategies (\[Hu et al., 2020\]; \[Eghbal et al., 2014\]; \[Boluda-Ruiz
et al., 2019\]; \[Saber et al., 2017\]; \[Shakir et al., 2023\]).

❓ **Question 5: In hybrid RF-FSO systems, how does adaptive beamforming
reduce interception risk and improve secrecy capacity under
eavesdropping attacks?**

IMPROVED SUMMARY: In their detailed investigation, Erdogan et al. (2022)
delve into the intricacies of enhancing secrecy performance in mixed
RF-FSO communication systems, particularly under the threat of
eavesdropping attacks. The study utilizes a dual-hop relaying
configuration with decode-and-forward techniques, where the RF channel
is characterized by Nakagami-m fading and the FSO channel by an
exponentiated Weibull distribution. This research underscores the
critical role of physical characteristics such as the size and strategic
placement of photo-apertures in bolstering resistance against
eavesdropping attempts. Analytical models are developed to compute
secrecy outage probability and probability of positive secrecy capacity,
which are substantiated through Monte-Carlo simulations. These
simulations confirm that larger apertures and higher placements of relay
nodes significantly enhance secrecy performance under diverse
environmental conditions.

Building on these findings, Juel et al. (2021) explore additional
dimensions of secrecy performance in mixed RF-FSO systems employing an
amplify-and-forward (AF) relaying scheme with α−µ fading for RF links
and exponentiated Weibull fading for the FSO link. Their study
emphasizes the effectiveness of aperture averaging in mitigating the
effects of atmospheric turbulence on secrecy metrics. They provide
closed-form analytical expressions for average secrecy capacity, secrecy
outage probability, and non-zero secrecy capacity probability using
Meijer<span dir="rtl">’</span>s G and Fox<span dir="rtl">’</span>s H
functions, demonstrating that larger aperture sizes at the receiver lead
to improved performance. The superiority of heterodyne detection over
intensity modulation/direct detection in enhancing these metrics is also
established \[Juel et al., 2021\].

Furthermore, Ai et al. (2019) contribute to understanding the physical
layer security in hybrid satellite-FSO systems by analyzing how
different relaying strategies and channel conditions affect secrecy
performance. They model satellite links with shadowed-Rician fading and
terrestrial FSO links with gamma-gamma fading, examining both
amplify-and-forward (AF) and decode-and-forward (DF) strategies. Their
findings reveal that AF with fixed gain significantly depends on the FSO
link's channel characteristics and detection technique used, whereas DF
or AF with variable-gain schemes show no improvement in secrecy
performance at high SNR levels \[Ai et al., 2019\]. This highlights how
adaptive beamforming in AF schemes can reduce interception risk by
optimizing gain based on channel state information.

Zhang et al. (2020) further enrich this discourse by addressing physical
layer security enhancements in asymmetric dual-hop RF-FSO systems with
multi-aperture destinations and eavesdroppers. They employ a partial
relay selection scheme based on maximum instantaneous channel gain for
the RF link and an equal gain combining scheme for processing signals at
both destination and eavesdropper points. Their analysis demonstrates
that these strategies significantly mitigate interception risks under
various atmospheric conditions due to turbulence-induced fading \[Zhang
et al., 2020\]. The integration of multi-aperture techniques is shown to
robustly improve system security against sophisticated eavesdropping
scenarios.

Tonk et al. (2022) extend this discussion by analyzing a mixed RF/FSO
cooperative relaying system affected by both atmospheric turbulence and
pointing errors modeled using Malaga distribution, alongside hardware
impairments at source and relay nodes quantified as aggregated hardware
impairment. They derive closed-form expressions for average secrecy rate
(ASR) using extended generalized bivariate Fox H-function (EGBFHF),
providing both exact and asymptotic expressions under high SNR
conditions on both RF and FSO links \[Tonk et al., 2022\]. Their results
indicate that hardware impairments and eavesdropping significantly
compromise the ASR, emphasizing the need for robust security measures.

Hu et al. (2020) propose advanced cooperative jamming techniques in a
mixed RF/FSO spectrum sharing network aimed at enhancing physical-layer
security against eavesdropping threats through direct transmission,
single-user cooperative jamming, and multi-user cooperative beamforming
jamming schemes. Employing sophisticated optimization methods like the
Dinkelbach method and semi-definite relaxation (SDR), they tackle
nonconvex challenges inherent in power optimization for enhanced
security \[Hu et al., 2020\].

Both studies highlight the influence of environmental factors such as
atmospheric turbulence and weather variations on FSO link performance,
which critically affect transmission quality and system vulnerability to
security breaches. Erdogan et al. (2022) suggest strategies for
optimizing relay node placement to effectively counteract these
environmental challenges.

Additionally, while physical layer security measures form a substantial
part of securing data transmission in mixed RF-FSO systems, integrating
advanced cryptographic techniques is proposed to bolster overall system
confidentiality. This dual approach ensures a robust defense mechanism
against both passive and active eavesdropping threats.

Overall, these comprehensive analyses not only illuminate various
technical strategies to enhance physical layer security but also
underscore the necessity for a holistic approach incorporating both
environmental adaptability and advanced encryption methods to safeguard
information in mixed RF-FSO networks. Future research should explore the
impact of advanced modulation techniques and adaptive relaying
strategies on the secrecy performance of mixed RF-FSO systems \[Juel et
al., 2021\]. Additionally, investigating machine learning applications
for dynamic optimization of system parameters could further enhance
adaptability to changing environmental conditions and threat levels.

❓ **Question 6: What is the role of accurate channel state information
(CSI) in implementing secure beamforming for FSO links under fading
turbulence?**

IMPROVED SUMMARY: In their detailed study, Lei et al. (2018) investigate
the secrecy outage performance of mixed Radio-Frequency (RF) and
Free-Space Optical (FSO) communication systems under conditions of
imperfect Channel State Information (CSI). The research is centered
around a dual-hop relay system that integrates
multiple-input-multiple-output (MIMO) RF links and an FSO link, where
both types of CSI (RF and FSO) are considered outdated and imprecise,
respectively. This analysis introduces four innovative Transmit Antenna
Selection (TAS) schemes aimed at enhancing the secrecy performance in
these challenging environments.

The authors provide analytical derivations for the probability density
function (PDF) and cumulative distribution function (CDF) over Malaga
channels with imperfect CSI, as well as calculations for the equivalent
signal-to-noise ratio (SNR) at the legitimate receiver over Nakagami-m
and Malaga channels. These mathematical formulations are substantiated
through Monte-Carlo simulations, which confirm that outdated CSI
significantly impairs secrecy outcomes in these hybrid systems.

Furthermore, the study explores how misalignment between transmitting
and receiving elements affects system performance, demonstrating that
even minor deviations can significantly degrade communication efficacy.
The impact of detection technology—specifically its ability to discern
legitimate signals from potential eavesdropping attempts—is scrutinized,
revealing its pivotal role in maintaining robust security protocols.

Lei et al. also evaluate the effectiveness of various TAS schemes in
light of different system parameters such as electrical SNR levels and
antenna configurations. These schemes are shown to effectively mitigate
some negative effects brought about by imperfect CSI, thereby enhancing
overall system security.

Additionally, the research delves into the effects of different relaying
schemes—fixed-gain and variable-gain—on the secrecy outage probability
(SOP), providing closed-form expressions for these calculations.
Asymptotic behavior of SOP is explored using
Meijer<span dir="rtl">’</span>s G-function, revealing that the impact of
electrical SNR of the FSO link becomes negligible as it approaches
infinity.

Zhang et al. (2021) further expand on this topic by evaluating
physical-layer security in underlay cognitive multi-relaying
MISO-RF/SIMO-FSO networks with outdated CSI. Their study employs a
multi-antenna secondary source and multi-aperture secondary destination
communicating via multiple relays, each equipped with both a single
antenna and a single aperture. A transmit antenna selection scheme with
channel feedback delay is used, and an equal gain combining protocol is
performed at the destination \[Zhang et al., 2021\]. The RF links are
modeled with Nakagami-m fading, and the FSO channels with Gamma-Gamma
distributions \[Zhang et al., 2021\]. Analytical and asymptotic
expressions for the lower bound of secrecy outage probability are
derived, highlighting how outdated CSI and atmospheric turbulence
challenge secure communications in hybrid RF-FSO systems \[Zhang et al.,
2021\].

Song et al. (2021) contribute to this field by establishing a FSO
transmission testbed to collect received signal strength indication
(RSSI) data under simulated weather conditions using an environmental
chamber. They employ expanded gated recurrent unit (GRU) neural networks
to predict FSO channel conditions based on RSSI data integrated with
real meteorological datasets \[Song et al., 2021\]. Their findings
demonstrate that GRU-based models can predict channel fading with high
precision—achieving absolute percentage error values lower than 6.9% for
up to 90% of predictions—and effectively handle various transmission
distances and weather scenarios \[Song et al., 2021\]. This capability
significantly enhances the adaptability and reliability of FSO
communication systems under varying weather conditions, supporting
intelligent beamforming strategies that dynamically adjust to changing
environmental factors.

Odeyemi et al. (2019) add further depth by analyzing partial relay
selection in an AF mixed RF/FSO system with outdated CSI. Their findings
underscore that variable gain relaying protocols substantially
outperform fixed gain ones in terms of maintaining secrecy under
Gamma-Gamma fading conditions influenced by atmospheric turbulence and
pointing errors \[Odeyemi et al., 2019\]. This study also quantitatively
assesses how outdated CSI impacts system performance, emphasizing that
variable gain relaying offers a robust method for enhancing secrecy in
mixed RF/FSO systems \[Odeyemi et al., 2019\].

Boluda-Ruiz et al. (2019) introduce a new misalignment error model to
account for non-orthogonal optical beams at an eavesdropper's receiver,
characterized by a rotated ellipse effective area under gamma-gamma
turbulence conditions with pointing errors \[Boluda-Ruiz et al., 2019\].
This model provides more accurate predictions on how eavesdropper's
location and orientation affect SOP, highlighting vulnerabilities when
optical beams become orthogonal to photodetector planes \[Boluda-Ruiz et
al., 2019\]. The study emphasizes that higher SNR at the eavesdropper's
channel and larger normalized beamwidths at the receiver-side adversely
affect secrecy performance \[Boluda-Ruiz et al., 2019\].

The findings from all studies underscore the critical role of precise
CSI in implementing secure beamforming strategies under fading
turbulence conditions within optical wireless networks. They emphasize
the importance of carefully selecting detection and relaying schemes to
mitigate adverse effects of channel imperfections, contributing to a
deeper understanding of dynamics under realistic conditions and
providing a foundation for future enhancements in secure optical
wireless communications.

❓ **Question 7: Which simulation studies demonstrate secrecy rate
improvements achieved by beam steering under weak vs. strong turbulence
conditions?**

IMPROVED SUMMARY: The comprehensive analysis conducted by Saber et al.
(2017) delves into the intricacies of secure Free-Space Optical (FSO)
communications under the influence of Málaga turbulence. This model is
pivotal as it encompasses features from both log-normal and
Generalized-K distributions, providing a robust framework for evaluating
FSO channel dynamics under various atmospheric disturbances. The study
meticulously derives closed-form expressions for key security metrics
such as average secrecy capacity, secrecy outage probability, and
strictly positive secrecy capacity, considering factors like intensity
modulation/direct detection (IM/DD) and pointing errors. These metrics
are crucial for understanding the physical layer security in FSO
communications.

Furthermore, the research highlights how the average Signal-to-Noise
Ratio (SNR) of the main channel significantly influences these security
metrics. Higher average SNRs generally lead to improved secrecy
capacities and reduced secrecy outage probabilities (\[Saber et al.,
2017\]). Additionally, the impact of turbulence intensity on these
security parameters is profound; lower turbulence intensities correlate
with higher values of strictly positive secrecy capacities, suggesting
that managing atmospheric conditions can substantially benefit secure
FSO communication systems.

Building on these insights, Boluda-Ruiz et al. (2019) introduce a novel
misalignment error model that accounts for non-orthogonal optical beams
at an eavesdropper's receiver, characterized by a rotated ellipse
effective area. This model is essential for analyzing the secrecy outage
probability (SOP) under gamma-gamma turbulence conditions with pointing
errors. The findings from this study indicate that the eavesdropper's
location and orientation critically influence SOP, particularly when the
receiver is aligned such that the optical beam becomes orthogonal to the
photodetector plane. Higher SNR at the eavesdropper's channel and larger
normalized beamwidth at the receiver-side were found to adversely affect
the secrecy performance (\[Boluda-Ruiz et al., 2019\]).

Monteiro et al. (2019) further expand our understanding by examining
relay-assisted FSO communications under varying weather
conditions—specifically comparing clear weather with weak turbulence
against light fog with strong turbulence. Their study employs an
adaptive transmission scheme utilizing selective relaying and
instantaneous Channel State Information (CSI), which proves superior in
enhancing effective secrecy throughput (EST), especially under
challenging environmental conditions. This adaptive approach allows for
dynamic adaptation to changing conditions and eavesdropper presence,
significantly reducing the likelihood of eavesdroppers intercepting the
optimal path (\[Monteiro et al., 2019\]). The use of multiple relays and
paths in their system model not only mitigates negative effects caused
by strong turbulence but also enhances overall system performance by
providing alternative routes for data transmission.

Wang et al. (2014) contribute to this body of knowledge by exploring
secret sharing and key agreement protocols within FSO systems under
gamma-gamma turbulence models. Their findings underscore that while
atmospheric turbulence strength does not significantly impact secret key
rates, optimizing per-symbol signal-to-noise ratio and training sequence
length are crucial for enhancing security performance (\[Wang et al.,
2014\]). This insight complements existing studies by confirming that
system parameter optimization can effectively bolster FSO communication
security against potential eavesdropping threats.

Juel et al. (2021) extend this discourse by analyzing a mixed RF-FSO
system employing an amplify-and-forward (AF) relaying scheme under
alpha-mu fading for RF links and exponentiated Weibull fading for FSO
links. They derive mathematical formulations including unified
probability density function and cumulative distribution function for
signal-to-noise ratio, developing closed-form analytical expressions
using Meijer<span dir="rtl">’</span>s G and Fox<span dir="rtl">’</span>s
H functions to quantify average secrecy capacity, secrecy outage
probability, and non-zero secrecy capacity probabilities (\[Juel et al.,
2021\]). Their results demonstrate that aperture averaging significantly
enhances secrecy performance by mitigating effects of atmospheric
turbulence, particularly noting that larger aperture sizes at the
receiver lead to better performance in terms of reduced secrecy outage
probability and increased average secrecy capacity. The superiority of
heterodyne detection over intensity modulation/direct detection in
enhancing secrecy metrics was also established (\[Juel et al., 2021\]).
These findings validate theoretical models through empirical Monte Carlo
simulations and suggest further enhancements in secrecy metrics could be
achieved by optimizing system parameters based on channel conditions and
external impairments.

Lei et al. (2020) explore mixed RF-FSO systems with transmit antenna
selection (TAS) schemes under outdated and imprecise CSI conditions
affecting both RF and FSO links respectively. They propose four TAS
schemes aimed at enhancing system security despite CSI imperfections,
which are validated through Monte-Carlo simulations demonstrating
significant impacts on system performance due to outdated CSI (\[Lei et
al., 2020\]). The study also highlights how increasing antenna numbers
at the source does not substantially improve secrecy performance but
emphasizes how TAS schemes can mitigate challenges posed by imperfect
CSI (\[Lei et al., 2020\]).

Overall, this detailed examination not only underscores the
effectiveness of using various models in predicting performance under
varied environmental conditions but also stresses the critical nature of
pointing accuracy and channel optimization in designing state-of-the-art
secure FSO systems. The additional insights provided enhance our
understanding of how system parameters like SNR and training sequence
length can further complicate or facilitate security measures in FSO
systems, emphasizing a more nuanced approach to physical layer security
against sophisticated eavesdropping techniques. Future research should
focus on extending these models to include more complex eavesdropping
scenarios and exploring adaptive security mechanisms that dynamically
adjust based on perceived threat levels while also seeking experimental
validation under real-world conditions.

❓ **Question 8: What types of relays (amplify-and-forward,
decode-and-forward) are most effective for enhancing secrecy in FSO
communication systems under interception threats?**

IMPROVED SUMMARY: In their comprehensive analysis, Ai et al. (2019)
delve into the intricacies of physical layer security within hybrid
satellite-FSO communication systems. The study models satellite links
through a shadowed-Rician fading distribution and terrestrial links via
gamma-gamma fading, providing a robust framework for evaluating secrecy
metrics under various channel conditions. The research emphasizes two
primary relaying strategies: amplify-and-forward (AF) and
decode-and-forward (DF). Analytical expressions for average secrecy
capacity and secrecy outage probability are derived for both strategies,
highlighting how these metrics are influenced by the choice of relaying
method. Notably, in an AF scheme with fixed gain, the secrecy diversity
order is determined exclusively by the characteristics of the FSO link
and the detection technique used. This contrasts sharply with DF or AF
schemes employing variable gain, where a zero secrecy diversity order
suggests no enhancement in secrecy performance as SNR increases \[Ai et
al., 2019\].

Furthermore, Ai et al. (2019) conduct an asymptotic analysis of SOP
under high SNR conditions to assess how increased signal clarity impacts
security measures. This aspect is crucial as it elucidates that while
certain configurations may benefit from higher SNRs, others may not
yield any significant improvement in terms of confidentiality against
interception threats. Additionally, the role of detection
techniques—specifically heterodyne detection and intensity modulation
with direct detection—is critically examined. These techniques
significantly affect the system's ability to maintain secrecy by
influencing how effectively signals can be transmitted without
interception under varying atmospheric conditions \[Ai et al., 2019\].

Expanding on these findings, Odeyemi et al. (2019) investigate the
impact of partial relay selection in an AF mixed RF/FSO system with
outdated channel state information on secrecy outage performance. Their
study models RF links with Rayleigh fading and FSO links with
Gamma-Gamma fading, considering both heterodyyne and intensity
modulation with direct detection techniques. They employ fixed gain and
variable gain amplified-and-forward (AF) relaying protocols and derive
unified cumulative distribution functions for the equivalent end-to-end
signal-to-noise ratio for both relaying schemes. Monte Carlo simulations
validate their theoretical analysis, demonstrating that variable gain
relaying significantly outperforms fixed gain in terms of secrecy
performance \[Odeyemi et al., 2019\]. The study also highlights how
atmospheric turbulence and pointing errors severely degrade system
performance, emphasizing the superiority of variable gain relaying in
maintaining secrecy under outdated channel state information.

Monteiro et al. (2019) explore relay-assisted FSO communications,
focusing on effective secrecy throughput (EST) under different weather
conditions and eavesdropping scenarios. Their study employs a
theoretical analysis and simulation of a system model that includes
multiple paths between Alice and Bob, each with multiple relays. Two
transmission schemes are analyzed: an adaptive scheme with selective
relaying that utilizes instantaneous CSI for optimal path selection, and
a fixed-rate scheme with all-active relaying without access to
instantaneous CSI. The results demonstrate that both transmission
schemes benefit from the use of multiple hops; however, the adaptive
scheme shows additional benefits from the use of multiple paths as it
reduces the likelihood of eavesdroppers being on the optimal path
\[Monteiro et al., 2019\].

Erdogan et al. (2022) further enrich this discourse by examining mixed
RF-FSO relay networks under both RF and FSO eavesdropping attacks. They
employ a dual-hop mixed RF-FSO relaying configuration with
decode-and-forward (DF) techniques to derive critical metrics such as
secrecy outage probability (SOP) and probability of positive secrecy
capacity (PPSC). Their findings underscore that physical parameters like
photo-aperture size and placement are pivotal in enhancing network
security against eavesdropping threats \[Erdogan et al., 2022\].
Specifically, larger photo-apertures and higher placement of relay nodes
significantly bolster resistance to eavesdropping, especially under
harsh weather conditions.

Zhang et al. (2020) contribute significantly to this field by
investigating an asymmetric dual-hop RF-FSO communication system
threatened by a multi-aperture eavesdropper. They implement a partial
relay selection scheme based on maximum instantaneous channel gain for
the RF link combined with an equal gain combining scheme at both
destination and eavesdropper sites. The study models RF channels using
Nakagami-m fading and FSO channels through Gamma-Gamma distributions,
analyzing metrics like secrecy outage probability and strictly positive
secrecy capacity \[Zhang et al., 2020\]. Their findings validate that
advanced relay selection and signal combining techniques markedly
improve security against sophisticated eavesdropping tactics under
diverse atmospheric conditions.

Juel et al. (2021) extend this discussion by analyzing a mixed RF-FSO
system employing an amplify-and-forward (AF) relaying scheme with
variable gain under alpha-mu fading for RF links and exponentiated
Weibull fading for FSO links. They focus on heterodyne detection and
intensity modulation/direct detection techniques while considering
pointing error impairments. Mathematical formulations involve deriving
unified probability density function and cumulative distribution
function for signal-to-noise ratio, leading to closed-form analytical
expressions for average secrecy capacity, secrecy outage probability,
and non-zero secrecy capacity using Meijer's G and Fox's H functions
\[Juel et al., 2021\]. The study demonstrates that aperture averaging
can significantly enhance secrecy performance by mitigating effects of
atmospheric turbulence, suggesting larger aperture sizes at the receiver
lead to better performance in terms of reduced SOP

❓ **Question 9: How does cooperative relaying (AF vs. DF) improve
physical layer security in FSO links subject to eavesdropping?**

IMPROVED SUMMARY: In their comprehensive analysis, Ai et al. (2019)
delve into the intricacies of physical layer security within hybrid
satellite-FSO communication systems, emphasizing how cooperative
relaying strategies—amplify-and-forward (AF) and decode-and-forward
(DF)—influence secrecy metrics such as average secrecy capacity and
secrecy outage probability (SOP). The study models satellite links using
a shadowed-Rician fading distribution and terrestrial FSO links with
gamma-gamma fading, providing a robust framework for evaluating the
impact of various channel conditions on system performance. The research
highlights that in an AF scheme with fixed gain, the secrecy diversity
order is significantly affected by the characteristics of the FSO link
and the type of detection technique implemented. This contrasts starkly
with scenarios employing DF or variable-gain AF strategies, where a zero
secrecy diversity order suggests no enhancement in secrecy performance
at higher SNR levels.

Furthermore, Ai et al. (2019) explore how pointing errors—a common
challenge in FSO systems due to alignment issues between
transceivers—affect the overall security metrics. The analysis indicates
that pointing errors can severely degrade system performance unless
adequately mitigated through precise system design and alignment
strategies. Additionally, the role of detection techniques such as
heterodyne detection and intensity modulation with direct detection is
critically examined. These techniques are pivotal in determining how
effectively the system can maintain confidentiality against potential
eavesdroppers under varying atmospheric conditions.

Expanding on these findings, Tonk et al. (2022) provide new insights
into mixed RF/FSO cooperative relaying systems where both RF and FSO
links are considered under different fading models—Nakagami-m for RF and
Malaga distribution for FSO, influenced by atmospheric turbulence and
pointing errors. Their study introduces an advanced analytical approach
using the extended generalized bivariate Fox H-function (EGBFHF) to
derive closed-form expressions for average secrecy rate (ASR), which are
further validated through asymptotic expressions at high SNR conditions.
This analysis reveals that hardware impairments at relay nodes and the
presence of eavesdroppers significantly compromise ASR, highlighting
vulnerabilities that necessitate robust security measures.

Building upon these discussions, Zhang et al. (2020) investigate an
asymmetric dual-hop RF-FSO communication system enhanced by a partial
relay selection scheme based on maximum instantaneous channel gain for
the RF link and an equal gain combining scheme for processing signals at
both destination and eavesdropper points. Their study employs Nakagami-m
fading for RF channels and Gamma-Gamma distributions for FSO channels,
analyzing metrics like secrecy outage probability and strictly positive
secrecy capacity. The results demonstrate that these configurations
significantly enhance the physical layer security against multi-aperture
eavesdroppers \[Zhang et al., 2020\]. Moreover, their findings
underscore the effectiveness of integrating multi-aperture techniques to
mitigate turbulence-induced fading's effects, thereby enhancing
robustness under various atmospheric conditions.

Yang et al. (2018) further enrich this discourse by examining
physical-layer security in mixed RF/FSO dual-hop communication systems
under η–μ and M-distributed fading conditions. They focus on both fixed
and variable gain relaying schemes where only the RF link is vulnerable
to eavesdropping due to its lower inherent security compared to the
optical link. Their findings reveal that while fixed gain relaying is
highly sensitive to changes in average SNR at the RF link, variable gain
relaying can adapt more effectively to instantaneous channel conditions,
potentially offering superior secrecy performance \[Yang et al., 2018\].
This detailed exploration into hybrid satellite-FSO systems underscores
not only the pivotal role of relaying strategies and channel
characteristics but also emphasizes how ancillary factors like pointing
errors, detection methods, hardware impairments, and eavesdropping
crucially mold the system's ability to safeguard data transmission
against interception \[Ai et al., 2019; Tonk et al., 2022; Zhang et al.,
2020; Yang et al., 2018\].

Lopez-Martinez et al. (2015) contribute significantly to understanding
how atmospheric turbulence impacts physical-layer security in free-space
optical communications by analyzing different stochastic models such as
log-normal and Gamma-Gamma distributions representing weak to strong
turbulence conditions. They provide novel closed-form expressions for
strictly positive secrecy capacity across common FSO propagation models
\[Lopez-Martinez et al., 2015\]. Their findings highlight that even
small amounts of power intercepted by an eavesdropper can lead to
substantial security breaches, especially when eavesdroppers are
positioned near transmitters where signal attenuation is greatest due to
larger distances covered \[Lopez-Martinez et al., 2015\]. This
underscores the need for dynamic beam shaping and adaptive modulation
schemes as potential countermeasures against such vulnerabilities.

Erdogan et al. (2022) extend this discussion by examining mixed RF-FSO
relay networks under both RF and FSO eavesdropping attacks using a
dual-hop configuration with DF techniques \[Erdogan et al., 2022\]. They
emphasize that physical parameters like photo-aperture size and
placement are critical in enhancing network security against
eavesdropping threats under harsh weather conditions \[Erdogan et al.,
2022\]. By integrating Nakagami-m fading for RF channels with
exponentiated Weibull distribution modeling for FSO channels, they
provide a comprehensive understanding of channel behavior which supports
strategic enhancements in network design aimed at improving
confidentiality \[Erdogan et al., 2022\].

❓ **Question 10: What relay selection algorithms maximize secrecy
capacity in mixed RF-FSO networks, and how do they perform under
mobility scenarios?**

IMPROVED SUMMARY: In their comprehensive analysis, Erdogan et al. (2022)
delve into the intricacies of securing mixed RF-FSO relay networks
against eavesdropping attacks. Utilizing a dual-hop relaying
configuration with decode-and-forward techniques, they model the RF
channel using Nakagami-m fading and the FSO channel with an
exponentiated Weibull distribution. This choice of models is pivotal as
it reflects a realistic approximation of channel behaviors under
different atmospheric conditions, which is crucial for designing robust
communication systems (\[Erdogan et al., 2022\]). The study meticulously
derives and validates through Monte-Carlo simulations two critical
secrecy performance metrics: secrecy outage probability (SOP) and
probability of positive secrecy capacity (PPSC). These metrics are
essential for assessing the effectiveness of security measures in
communication networks.

Zhang et al. (2020) further enhance our understanding by investigating
an asymmetric dual-hop RF-FSO system where a source transmits to a
multi-aperture destination through the best relay, selected based on
maximum instantaneous channel gain for the RF link. They employ a
partial relay selection scheme and an equal gain combining scheme to
process signals at both the destination and eavesdropper, modeled under
Nakagami-m fading for RF and Gamma-Gamma distributions for FSO channels.
Their findings underscore that such configurations significantly boost
the system's secrecy performance, particularly under varying atmospheric
conditions (\[Zhang et al., 2020\]).

Tonk et al. (2022) contribute significantly by analyzing the impact of
hardware impairments and eavesdropping on mixed RF/FSO systems. They
model both RF and FSO links under Nakagami-m and Malaga distributions
respectively, considering atmospheric turbulence and pointing errors.
Their research highlights how these factors reduce average secrecy rate
(ASR), especially in high SNR scenarios where their effects are
pronounced (\[Tonk et al., 2022\]). The use of extended generalized
bivariate Fox H-function (EGBFHF) in deriving ASR expressions provides a
comprehensive analytical tool for evaluating system performance under
these adverse conditions.

Zhang et al. (2021) evaluate physical-layer security in underlay
cognitive multi-relaying MISO-RF/SIMO-FSO networks with outdated CSI,
employing multiple antennas and apertures to enhance security robustness
against eavesdropping. Their study introduces a Kth relay selection
criterion that significantly improves communication system robustness by
carefully selecting relays based on their ability to handle outdated CSI
effectively (\[Zhang et al., 2021\]). This approach is validated through
Monte-Carlo simulations that confirm its efficacy in maintaining secure
communications despite challenges posed by outdated CSI and atmospheric
turbulence.

Odeyemi et al. (2019) explore the impact of partial relay selection in
an AF mixed RF/FSO system with outdated channel state information on
secrecy outage performance under different relaying protocols and
atmospheric conditions. They demonstrate that variable gain relaying
protocols significantly outperform fixed gain protocols in terms of
maintaining secrecy, especially when considering Rayleigh fading for RF
links and Gamma-Gamma fading with potential pointing errors for FSO
links (\[Odeyemi et al., 2019\]). The study also emphasizes the critical
role of atmospheric turbulence and pointing errors in degrading system
performance, suggesting that variable gain relaying offers a robust
method for enhancing secrecy in mixed RF/FSO systems under such
challenging conditions.

The research by Erdogan et al. (2022) emphasizes the importance of
sophisticated channel modeling in designing secure networks. By
integrating Nakagami-m and exponentiated Weibull distributions into
their analysis, they provide a nuanced understanding that aids in
anticipating how varying channel conditions affect transmission
security. Additionally, their work suggests practical strategies for
optimizing relay node placement to maximize secrecy capacity
effectively. These strategies are crucial for maintaining high levels of
security in dynamic environments where network configurations might need
frequent adjustments due to changing external conditions or mobility
scenarios.

Building on these insights, Juel et al. (2021) further explore the
secrecy performance of mixed RF-FSO systems employing an
amplify-and-forward (AF) relaying scheme with variable gain under
alpha-mu fading for RF links and exponentiated Weibull fading for FSO
links. They focus on heterodyne detection and intensity
modulation/direct detection techniques while considering pointing error
impairments. Juel et al. develop closed-form analytical expressions for
average secrecy capacity, secrecy outage probability, and the
probability of non-zero secrecy capacity using
Meijer<span dir="rtl">’</span>s G and Fox<span dir="rtl">’</span>s H
functions (\[Juel et al., 2021\]). Their results demonstrate that
aperture averaging significantly enhances the secrecy performance by
mitigating the effects of atmospheric turbulence, with larger aperture
sizes at the receiver leading to better performance in terms of reduced
secrecy outage probability and increased average secrecy capacity.

Both studies underscore the necessity of leveraging detailed channel
models and strategic design considerations influenced by both physical
and environmental parameters to enhance the confidentiality and
integrity of data transmitted over mixed RF-FSO networks.

❓ **Question 11: Which channel coding techniques (e.g., LDPC, Polar
codes) are most suitable for achieving physical-layer secrecy in
turbulent FSO channels?**

IMPROVED SUMMARY: The comprehensive study by Endo et al. (2016) delves
into the nuances of implementing physical layer security within
Free-Space Optical (FSO) communications, particularly focusing on the
challenges posed by atmospheric turbulence and its resultant impact on
signal fading. Utilizing a metropolitan terrestrial FSO link testbed in
Tokyo, which mimics real-world FSO scenarios such as satellite-to-ground
laser communications, the research involves transmitting pseudorandom
binary sequences via on-off keying modulation to analyze secrecy rates
under varying atmospheric conditions. The experiments reveal that
secrecy rates are highly susceptible to changes in atmospheric
conditions, highlighting the necessity for adaptive coding strategies
that can respond dynamically to such fluctuations to maintain secure
communications.

Further expanding on the topic of physical layer security in FSO
systems, Ai et al. (2020) explore the performance of FSO communications
over Málaga channels under different eavesdropping scenarios. The study
employs intensity modulation/direct detection (IM/DD) based FSO systems,
analyzing the fading behaviors characterized by the generalized Málaga
model. Theoretical models and expressions are derived for average
secrecy capacity (ASC) and secrecy outage probability (SOP),
incorporating factors such as correlation between channels and
atmospheric conditions. The results indicate that proximity of the
eavesdropper to the transmitter less significantly impacts secrecy
performance compared to other positions. Correlation between the
channels can enhance or deteriorate the secrecy performance depending on
its level, showing a non-monotonic relationship with performance
metrics.

Zhong et al. (2024) introduce significant advancements in understanding
the impact of atmospheric channel correlation on physical layer security
for FSO systems. Their research utilizes a Gamma-Gamma distribution
model to derive a new closed-form expression for interception
probability, emphasizing how this metric is influenced by turbulence
intensity, channel correlation, and radial displacement attenuation of
eavesdroppers. The study demonstrates that under correlated channel
conditions, interception probability increases with turbulence intensity
but decreases with increased channel correlation; conversely, for
uncorrelated channels, interception probability rises with turbulence
intensity and diminishes with larger aperture intervals.

Shakir et al. (2022) contribute further insights into enhancing physical
layer security in FSO communication systems by examining various
techniques such as noise randomization and CSI utilization alongside
multiantenna and cooperative nodes strategies. They emphasize employing
advanced modulation schemes like orbital angular momentum multiplexing
and acousto-optic deflectors to improve secrecy performance under
diverse atmospheric turbulence conditions. Their review underscores the
advantages of physical layer security techniques over traditional
cryptographic methods due to computational efficiency and independence
from shared keys.

Incorporating findings from López-Martínez et al. (2015), it is evident
that physical-layer security in FSO communications can be significantly
compromised by an eavesdropper, especially when located near the
transmitter due to larger attenuation suffered by the signal during
propagation through turbulent FSO links. This study provides critical
insights into how optical irradiance fluctuations and beam divergence
affect secure transmission probabilities, emphasizing that even small
amounts of power intercepted by an eavesdropper can lead to substantial
security breaches.

Both studies underscore the importance of channel estimation techniques
for accurately assessing the state of the FSO channel, thereby enabling
effective adjustments to coding strategies in response to eavesdropping
threats and atmospheric instabilities. The presence of an eavesdropper
in these setups allows for an evaluation of the impact of potential
security breaches, emphasizing robust multi-layer security architectures
that combine physical layer measures with algorithmic strategies to
safeguard against sophisticated attacks.

This layered approach ensures a comprehensive defense mechanism for FSO
communications, making it imperative to integrate both physical layer
security enhancements and resilient upper-layer protocols. Future work
should explore more adaptive and robust relaying strategies that can
dynamically adjust based on the channel state information of both
satellite and FSO links \[Endo et al., 2016; Ai et al., 2020; Zhong et
al., 2024; Shakir et al., 2022; López-Martínez et al., 2015\].
Additionally, investigating the integration of advanced detection
techniques and mitigation of pointing errors could further enhance the
secrecy performance of hybrid satellite-FSO systems.

❓ **Question 12: How do LDPC-based secrecy codes perform in terms of
BER and secrecy throughput under strong turbulence fading conditions?**

IMPROVED SUMMARY: Monteiro et al. (2019) provide a detailed exploration
of relay-assisted Free-Space Optical (FSO) communications, focusing on
how multiple relays and diverse paths can enhance effective secrecy
throughput (EST) under various atmospheric conditions. The study
contrasts two transmission schemes: an adaptive scheme that leverages
selective relaying based on instantaneous CSI for optimal path
selection, and a fixed-rate scheme that does not incorporate such
dynamic adjustments. The adaptive scheme proves particularly adept at
mitigating the adverse effects of atmospheric turbulence on
communication links, a critical consideration given the sensitivity of
FSO systems to environmental factors (\[Monteiro et al., 2019\]).

Further, the research delves into the secrecy outage probability (SOP),
a crucial metric for assessing the robustness of FSO systems against
eavesdropping under conditions such as strong turbulence induced by
light fog. Findings indicate that strategic relay placement and path
diversity can substantially reduce SOP, thereby enhancing both system
security and reliability (\[Monteiro et al., 2019\]).

The study also examines how eavesdropping scenarios are intricately
linked with atmospheric conditions, impacting both EST and SOP. The
significant role of atmospheric turbulence is highlighted as it
influences not only signal degradation but also the strategic deployment
of transmission schemes designed to counter such challenges effectively.
By integrating considerations related to eavesdropping into their
analysis, Monteiro et al. (2019) present a comprehensive view of
security dynamics in FSO communications, emphasizing the necessity for
adaptive strategies that respond to environmental changes and potential
security threats.

Expanding upon these insights, Saber et al. (2017) investigate secure
FSO communications over Málaga turbulence channels from a physical layer
perspective. They introduce closed-form expressions for average secrecy
capacity, secrecy outage probability, and strictly positive secrecy
capacity while considering intensity modulation/direct detection (IM/DD)
and pointing errors in Málaga modeled turbulence conditions. This model
effectively captures complex dynamics under various atmospheric
disturbances and provides insights into how improvements in pointing
accuracy and turbulence condition optimizations can significantly
enhance FSO link security (\[Saber et al., 2017\]).

Building on this foundation, Juel et al. (2021) explore the performance
of mixed RF-FSO systems employing an amplify-and-forward (AF) relaying
scheme under alpha-mu fading for RF links and exponentiated Weibull
fading for the FSO link. Their analysis reveals that aperture averaging
can significantly enhance secrecy performance by mitigating effects of
atmospheric turbulence on signal integrity. They demonstrate that larger
aperture sizes at the receiver lead to better performance in terms of
reduced secrecy outage probability and increased average secrecy
capacity. Furthermore, they establish the superiority of heterodyne
detection over intensity modulation/direct detection in enhancing
secrecy metrics under these complex channel conditions (\[Juel et al.,
2021\]). The integration of mathematical models with empirical Monte
Carlo simulations validates these theoretical findings, suggesting
further enhancements in secrecy metrics could be achieved by optimizing
system parameters based on channel conditions and external impairments.

Lei et al. (2018) contribute to this discussion by analyzing the impact
of imperfect channel state information (CSI) on the secrecy outage
performance of mixed RF-FSO systems using a single-input multiple-output
wiretap model. Their study highlights how imperfect CSI significantly
degrades SOP and demonstrates that system performance is sensitive to
detection schemes and relaying schemes employed. Closed-form expressions
for the lower bound of SOP with fixed-gain and variable-gain relaying
schemes are derived, providing valuable insights into how different
system parameters like misalignment affect security outcomes (\[Lei et
al., 2018\]). Asymptotic behavior analysis using
Meijer<span dir="rtl">’</span>s G-function reveals that the impact of
electrical SNR of the FSO link becomes negligible as it approaches
infinity, underscoring the importance of carefully selecting detection
and relaying schemes to mitigate adverse effects from channel
imperfections.

Ai et al. (2021) further analyze how channel correlation affects SOP in
FSO communications modeled by the Málaga distribution, discovering that
increased correlation between main and wiretap links initially degrades
SOP but improves it significantly beyond a certain threshold due to
non-monotonic behavior (\[Ai et al., 2021\]). This counterintuitive
finding suggests that under specific conditions, strategically
exploiting increased correlation can enhance FSO system security against
eavesdroppers even under strong turbulence fading conditions.

Tonk et al. (2022) extend this discussion by examining mixed RF/FSO
cooperative relaying systems where both RF and FSO links are subjected
to Nakagami-m fading and Malaga distribution respectively, compounded by
hardware impairments at relay nodes which significantly affect average
secrecy rate (ASR). They derive closed-form expressions for ASR using
extended generalized bivariate Fox H-function (EGBFHF), providing a
robust analytical framework for assessing system performance under these
compounded adversities (\[Tonk et al., 2022\]). Their findings
underscore the critical impact of eavesdroppers and hardware impairments
on ASR in high SNR scenarios, highlighting vulnerabilities in mixed
RF/FSO systems that necessitate advanced mitigation strategies.

Future research should explore advanced modulation techniques and
machine learning applications for dynamic optimization of system
parameters to adapt to changing environmental conditions and threat
levels.

❓ **Question 13: What design parameters define
secrecy-capacity-achieving codes in fading optical channels, and how can
they be optimized?**

IMPROVED SUMMARY: In their pivotal study, Endo et al. (2016) delve into
the complexities of implementing physical layer security in free-space
optical communications through an experimental approach using the Tokyo
FSO Testbed. This testbed configuration involved a sender and two
receivers spaced 7.8 km apart, designed to emulate realistic FSO
communication scenarios such as satellite-to-ground transmissions. The
experiments conducted transmitted pseudorandom binary sequences via
on-off keying modulation, focusing on analyzing output signal statistics
to derive secrecy rates and other pertinent security metrics under
various atmospheric conditions.

The research highlighted that physical layer security could
substantially bolster the security framework of FSO communications;
however, its effectiveness is significantly compromised by atmospheric
turbulence-induced fading effects. Under stable atmospheric conditions,
it was demonstrated that secure message transmission with reasonably
sized code lengths is achievable. Conversely, in scenarios characterized
by strong fading conditions due to atmospheric turbulence, there was a
notable fluctuation in secrecy rates which posed challenges to
maintaining consistent security levels.

The study further emphasized the critical impact of atmospheric
turbulence on signal degradation, which directly affects the reliability
of secure transmissions in FSO systems. To address these challenges
posed by atmospheric variability, Endo et al. (2016) suggested the
necessity for adaptive coding strategies that can dynamically adjust to
changing environmental conditions to optimize secrecy rates and enhance
overall communication security.

Moreover, recognizing the limitations of relying solely on PHY security
measures under diverse operational scenarios, the researchers advocated
for a comprehensive multi-layer security architecture. This architecture
would integrate physical layer security with conventional encryption
methods to provide a robust defense against more sophisticated forms of
eavesdropping and other cyber threats.

Adding insights from Lei et al. (2018), the integration of RF-FSO
technologies with advanced relay selection and signal combining
techniques is highlighted as a potent strategy to enhance physical layer
security against eavesdropping threats. Lei et al.'s study introduces a
mixed RF-FSO system employing both fixed-gain and variable-gain relaying
schemes and models the impact of imperfect channel state information
(CSI) on secrecy outage probability (SOP). Their findings underscore
that imperfect CSI significantly degrades the secrecy outage performance
of mixed RF-FSO systems \[Lei et al., 2018\]. The study also shows that
system performance is sensitive to detection schemes and relaying
schemes employed \[Lei et al., 2018\]. Asymptotic analysis reveals that
the impact of the electrical SNR of the FSO link becomes negligible as
it approaches infinity \[Lei et al., 2018\].

Lei et al.'s research also reveals that both misalignment and detection
technologies play crucial roles in enhancing or impairing the secrecy
performance in mixed RF-FSO networks \[Lei et al., 2018\]. Specifically,
pointing errors and different detection technologies affect the
cumulative distribution function (CDF) and probability density function
(PDF) for FSO links, which are critical for assessing SOP under varying
channel conditions \[Lei et al., 2018\]. This study highlights the
importance of considering both RF and FSO eavesdropping attacks in
designing secure relay networks and suggests that effective design
requires careful consideration of physical parameters and channel
modeling \[Lei et al., 2018\].

Building upon these insights, Ai et al. (2019) explore physical layer
security within hybrid satellite-FSO cooperative systems, where
satellite links follow a shadowed-Rician fading distribution and
terrestrial links experience gamma-gamma fading. The study meticulously
analyzes how different relaying strategies—specifically
amplify-and-forward (AF) with fixed gain versus decode-and-forward
(DF)—and detection techniques like heterodyne detection influence
secrecy metrics such as average secrecy capacity and SOP \[Ai et al.,
2019\]. Notably, Ai et al. find that while AF with fixed gain can
maintain a positive secrecy diversity order dependent solely on FSO link
characteristics and detection type used, DF or AF with variable-gain
schemes result in zero secrecy diversity order at high SNR levels \[Ai
et al., 2019\]. This underscores how critical the choice of relaying
strategy and channel characteristics are in optimizing physical layer
security in such hybrid systems.

Zhang et al. (2021) further enrich our understanding by evaluating
physical-layer security for an underlay cognitive radio-based RF-FSO
network employing multi-antenna sources and multi-aperture destinations
communicating via multiple relays equipped with both antenna and
aperture capabilities \[Zhang et al., 2021\]. Their findings emphasize
how outdated CSI impacts system performance significantly when combined
with Nakagami-m fading for RF links and Gamma-Gamma distributions for
FSO channels \[Zhang et al., 2021\]. The study provides analytical
expressions for lower bounds on secrecy outage probability while
demonstrating how multiple antennas, apertures, relay selection
criteria, and effective management of outdated CSI can enhance system
robustness against eavesdropping threats \[Zhang et al., 2021\].

Together, these studies underscore the critical role of innovative relay
selection methods, dynamic coding strategies, integrated system
architectures, meticulous consideration of channel imperfections,
specific system configurations in advancing state-of-the-art physical
layer security for RF-FSO communication systems under diverse
operational conditions. Future work should explore more adaptive
relaying strategies that can dynamically adjust based on channel state
information from both satellite and terrestrial links while integrating
advanced detection techniques to mitigate pointing errors further
enhancing hybrid system's secrecy performance \[Ai et al., 2019; Zhang
et al., 2021\].

❓ **Question 14: Can multilevel coding architectures be applied to
separate confidential and non-confidential data streams in secure FSO
transmitters?**

IMPROVED SUMMARY: In their comprehensive analysis, Zhang et al. (2021)
delve into the intricacies of enhancing physical layer security within
an asymmetric dual-hop RF-FSO communication system, particularly when
confronted by a multi-aperture eavesdropper. The study introduces a
partial relay selection strategy that optimizes for maximum
instantaneous channel gain on the RF link, coupled with an equal gain
combining scheme to process signals at both destination and eavesdropper
points. This approach is critical in managing the Nakagami-m fading
characteristics of RF channels and Gamma-Gamma fading in FSO channels.
Theoretical evaluations focus on key secrecy performance metrics such as
secrecy outage probability and strictly positive secrecy capacity, with
empirical support from Monte-Carlo simulations confirming theoretical
predictions.

Zhang et al. (2021) further investigate how atmospheric turbulence
impacts signal integrity within these systems, demonstrating that
multi-aperture techniques can effectively mitigate turbulence-induced
fading effects. This aspect is crucial for maintaining robust
communication links under varying environmental conditions, thereby
enhancing system resilience against potential security breaches.

Additionally, Zhang et al. (2021) explore various relay selection
strategies that contribute to optimizing system performance while
ensuring secure data transmission. These strategies are pivotal in
adapting to dynamic channel conditions and in thwarting potential
eavesdropping attempts. The study also addresses potential eavesdropping
scenarios and proposes countermeasures to safeguard against such
threats. By analyzing different eavesdropping techniques and their
impact on system security, Zhang et al. (2021) provide valuable insights
into designing more secure RF-FSO systems that can operate effectively
even under adverse conditions.

Tonk et al. (2022) extend this discussion by focusing on the mixed
RF/FSO cooperative relaying systems where the presence of eavesdroppers
and hardware impairments significantly reduce the average secrecy rate
(ASR). Their analysis employs a model with the RF link characterized by
Nakagami-m fading and the FSO link by Malaga distribution, considering
atmospheric turbulence and pointing errors. They derive closed-form
expressions for ASR using the extended generalized bivariate Fox
H-function (EGBFHF), as well as asymptotic expressions for high SNR
conditions on both links \[Tonk et al., 2022\]. This study highlights
the vulnerability of mixed RF/FSO systems to eavesdropping and hardware
impairments, emphasizing the need for robust security measures.

Endo et al. (2016) contribute significantly to this field by presenting
experimental data from a metropolitan terrestrial FSO link testbed used
to emulate typical FSO communication scenarios such as
satellite-to-ground laser communications. Their findings emphasize the
variability of the secrecy rate with atmospheric conditions,
particularly under strong fading conditions which necessitate the use of
long-span codes or adaptive strategies to maintain security.

Hu et al. (2020) propose advanced cooperative jamming techniques such as
single-user and multi-user cooperative beamforming jamming in mixed
RF/FSO spectrum sharing networks to enhance physical-layer information
security against single-antenna eavesdroppers. Employing sophisticated
nonconvex optimization techniques like the Dinkelbach method and
semi-definite relaxation (SDR), their simulation results demonstrate
that these advanced jamming schemes significantly outperform traditional
zero-forcing beamforming in terms of achieving higher secrecy rates \[Hu
et al., 2020\].

Hicks et al. (2023) introduce a novel approach to securing
non-terrestrial FSO communication links against UAVs and drones through
cryptographic encryption using GNU Radio platform and software-defined
radio hardware with Xsalsa20 encryption algorithm \[Hicks et al.,
2023\]. This method demonstrates significant resilience against
eavesdropping attacks due to its high-time complexity encryption, which
is challenging for power-limited flying objects to break. The lab-based
demonstration achieved a packet delivery rate of 92% and a transmission
rate of 10 Mbit/s at a distance of 250 mm with a laser output power of
10 mW \[Hicks et al., 2023\]. These findings underscore the
effectiveness of integrating cryptographic security into FSO systems,
suggesting further enhancements could be achieved by using less
sensitive SDR hardware for longer distances and higher data rates.

Overall, this detailed examination not only underscores the
effectiveness of integrating RF and FSO technologies with advanced relay
selection and signal combining techniques but also highlights the
importance of continuous adaptation to environmental challenges and
evolving security threats in maintaining high levels of data protection
in optical wireless networks.

❓ **Question 15: Which practical coding schemes achieve a tradeoff
between maximizing secrecy throughput and minimizing BER in turbulent
FSO environments?**

IMPROVED SUMMARY: In their comprehensive analysis, Monteiro et al.
(2019) delve into the dynamics of relay-assisted Free-Space Optical
(FSO) communications, focusing on how multiple relays and paths can
optimize effective secrecy throughput (EST) under diverse atmospheric
conditions. The study contrasts two transmission schemes: an adaptive
scheme that utilizes instantaneous channel state information (CSI) for
selective relaying and path optimization, and a fixed-rate scheme where
all relays are active without real-time CSI adaptation. The adaptive
scheme notably excels in environments with potential eavesdroppers, as
it minimizes risk by dynamically selecting paths less likely to be
intercepted.

The research by Wang et al. (2014) complements these findings by
introducing a private secret-key-based cryptosystem with key management
to enhance FSO security. Their study utilizes a subcarrier
intensity-modulated air-to-ground FSO system model to analyze the
coherence time and scintillation reciprocity of the FSO link. Key
management and agreement protocols are developed based on the statistics
of atmospheric-turbulence-induced fading, evaluated under the
gamma-gamma turbulence model. The findings demonstrate that the secret
key rate is primarily influenced by the per-symbol signal-to-noise ratio
and the length of the training sequence, rather than the strength of
atmospheric turbulence.

Lei et al. (2020) extend this discourse by analyzing mixed RF-FSO
systems employing transmit antenna selection (TAS) schemes under
conditions of outdated and imprecise CSI. Their study reveals that
outdated CSI significantly degrades secrecy performance, a finding
corroborated through Monte-Carlo simulations \[Lei et al., 2020\].
Despite increasing antenna numbers at the source, there is no
substantial improvement in secrecy performance, highlighting the limited
impact of antenna count under imperfect CSI conditions. The study also
derives closed-form expressions for PDF and CDF over Málaga channels,
providing insights into how misalignment and detection technology affect
system performance.

Both transmission schemes aim to maximize EST while managing a trade-off
with bit error rate (BER). The adaptive scheme tends to offer better
balance by reducing BER through optimal path selection during turbulent
conditions. This aspect is crucial for maintaining data integrity while
also ensuring confidentiality against potential security breaches.

Shakir et al. (2022) further enrich this discussion by emphasizing the
role of opportunistic scheduling schemes in managing the trade-off
between security and reliability in FSO communications. These schemes
leverage diversity gain under varying atmospheric conditions to enhance
both security and reliability without compromising one for the other.

Adding to this discourse, Hu et al. (2020) explore secrecy rate
optimization in mixed RF/FSO spectrum sharing networks where advanced
cooperative jamming techniques and sophisticated optimization methods
significantly enhance physical-layer security. They propose three
schemes—direct transmission, single-user cooperative jamming, and
multi-user cooperative beamforming jamming—to improve information
security against eavesdropping threats \[Hu et al., 2020\]. Employing
Rayleigh and Gamma-Gamma channel models with pointing errors considered,
they address nonconvex optimization challenges using Dinkelbach's method
and semi-definite relaxation (SDR), validated through Karush-Kuhn-Tucker
conditions.

Abd El-Mottaleb et al. (2023) introduce an innovative approach
integrating identity column shift matrix (ICSM) codes with OFDM and
4-QAM modulation techniques in FSO systems to enhance both security and
capacity \[Abd El-Mottaleb et al., 2023\]. This method is tested under
various atmospheric conditions using real meteorological data from
cities like Alexandria, Jeddah, and Hyderabad, demonstrating its
robustness across different environmental scenarios.

Overall, these studies provide valuable insights into optimizing
relay-assisted FSO systems through strategic relay placement and path
selection, emphasizing the critical role of atmospheric turbulence and
eavesdropping scenarios in shaping system performance. Future studies
could explore these dynamics through experimental validations and
advanced adaptive algorithms to enhance both secrecy throughput and
reliability under dynamically changing environmental conditions.

❓ **Question 16: How is spatial diversity implemented in secure FSO
systems using MISO/MIMO configurations, and what are the benefits for
secrecy capacity?**

IMPROVED SUMMARY: In their comprehensive analysis, Zhang et al. (2020)
delve into the complexities of securing hybrid RF-FSO communication
systems, particularly focusing on underlay cognitive multi-relaying
MISO-RF/SIMO-FSO networks operating under outdated CSI conditions. The
study meticulously models the RF links with Nakagami-m fading and FSO
channels with Gamma-Gamma distributions, providing a robust framework
for evaluating secrecy performance. A notable aspect of their
methodology includes the use of a transmit antenna selection scheme that
addresses channel feedback delays and an equal gain combining protocol
at the destination to optimize signal reception.

Zhang et al. (2020) further enhance the discussion by introducing a
partial relay selection scheme based on maximum instantaneous channel
gain for the RF link and employing an equal gain combining scheme for
processing signals at both the destination and eavesdropper. This
strategic approach significantly improves the physical layer security by
mitigating risks posed by multi-aperture eavesdroppers, as demonstrated
through Monte-Carlo simulations validating the theoretical analysis of
secrecy outage probability and strictly positive secrecy capacity.

The research also investigates how atmospheric turbulence adversely
affects signal integrity in FSO communications, which is critical given
the susceptibility of optical transmissions to environmental variations
\[Zhang et al., 2020\]. Moreover, Zhang et al. (2020) highlight
innovative techniques for managing outdated CSI, pivotal in maintaining
robust communication links despite delays in channel state information
updates. These techniques contribute significantly to sustaining high
levels of security against potential eavesdroppers by adapting to
dynamic channel conditions effectively.

Additionally, Ai et al. (2020) explore physical layer security in FSO
communications over Málaga channels, focusing on different eavesdropping
scenarios and atmospheric conditions. Their findings reveal that
proximity of the eavesdropper to the transmitter has a less significant
impact on secrecy performance compared to other positions \[Ai et al.,
2020\]. They also discover that correlation between channels can either
enhance or deteriorate secrecy performance depending on its level,
showing a non-monotonic relationship with performance metrics \[Ai et
al., 2020\]. This study provides foundational expressions and insights
that can guide future research and practical implementations in
enhancing FSO communication security.

Building on these insights, Ai et al. (2019) explore physical layer
security in hybrid satellite-FSO systems, emphasizing different relaying
strategies' impact on secrecy performance. The study models satellite
links using a shadowed-Rician fading distribution and terrestrial FSO
links with gamma-gamma fading. It assesses the effects of heterodyne
detection and intensity modulation with direct detection alongside
pointing errors on secrecy metrics such as average secrecy capacity and
secrecy outage probability \[Ai et al., 2019\].

Ai et al. (2019) find that the secrecy diversity order in an
amplify-and-forward (AF) scheme with fixed gain depends solely on the
FSO link's channel characteristics and the detection technique used. In
contrast, when employing decode-and-forward (DF) or AF with
variable-gain schemes, the secrecy diversity order is zero, indicating
no improvement in secrecy performance at high SNR levels \[Ai et al.,
2019\]. This highlights how specific relaying strategies and FSO link
characteristics critically influence hybrid satellite-FSO systems'
secrecy performance.

Yang et al. (2018) contribute to this discussion by investigating
physical-layer security in mixed RF/FSO dual-hop communication systems
under η–μ and M-distributed fading conditions. They focus on scenarios
where eavesdropping occurs primarily at the RF link due to its higher
vulnerability compared to the inherently secure optical link. By
modeling both fixed and variable gain relaying schemes, Yang et al.
(2018) derive analytical expressions for average secrecy rate (ASR) and
secrecy outage probability (SOP), demonstrating how fading conditions
and relaying schemes significantly influence secrecy performance \[Yang
et al., 2018\].

Hu et al. (2020) further enrich this discussion by addressing
optimization challenges in mixed RF/FSO spectrum sharing networks where
multiple single-antenna secondary users are connected through RF links
to a decode-and-forward relay which then connects via an FSO link to the
destination. They propose three schemes: direct transmission,
single-user cooperative jamming, and multi-user cooperative beamforming
jamming to enhance physical-layer security against eavesdropping threats
\[Hu et al., 2020\]. Their findings demonstrate that multi-user
cooperative beamforming jamming achieves higher secrecy rates than
zero-forcing beamforming and other suboptimal designs by effectively
managing mutual interference between primary and secondary networks
while considering both Rayleigh and Gamma-Gamma channel distributions
\[Hu et al., 2020\].

Overall, Zhang et al.'s (2020) work provides critical insights into
various strategies that can be employed to enhance physical-layer
security in complex hybrid communication networks. Their findings
advocate for a multifaceted approach involving strategic relay
selection, utilization of multiple antennas and apertures, advanced
management of outdated CSI to mitigate security risks posed by
eavesdroppers and environmental challenges \[Zhang et al., 2020\]. Ai et
al.'s studies further enrich this discussion by demonstrating how
different relaying strategies distinctly affect hybrid satellite-FSO
systems' physical layer security, suggesting future research directions
towards more adaptive relaying strategies that dynamically adjust based
on both satellite and FSO links' channel state information \[Ai et al.,
2019; Ai et al., 2020\]. Hu et al.'s work underscores the importance of
sophisticated optimization methods like Dinkelbach's method and
semi-definite relaxation for addressing nonconvex problems inherent in
power optimization for enhanced secrecy rates \[Hu et al., 2020\].

❓ **Question 17: Among diversity combining methods (selection
combining, maximal ratio combining, equal gain combining), which are
most effective for enhancing physical layer security in FSO systems?**

IMPROVED SUMMARY: In their comprehensive analysis, Ai et al. (2019)
explore the intricacies of physical layer security within hybrid
satellite-FSO systems, emphasizing the critical role played by channel
conditions and relaying strategies. The satellite link is modeled using
a shadowed-Rician fading distribution while the terrestrial FSO link
employs a gamma-gamma fading distribution, reflecting real-world
atmospheric challenges such as turbulence which can significantly affect
signal propagation and system reliability \[Ai et al., 2019\]. The study
meticulously evaluates how different detection techniques—heterodyne
detection and intensity modulation with direct detection—impact the
system's security metrics, particularly under varying atmospheric
conditions that introduce additional complexity to signal transmission
\[Ai et al., 2019\].

Furthermore, Ai et al. (2019) delve into the role of signal-to-noise
ratio (SNR) in shaping system performance, highlighting that higher SNR
does not necessarily translate to improved secrecy performance in
scenarios utilizing decode-and-forward or variable-gain
amplify-and-forward strategies. This counterintuitive finding
underscores the nuanced influence of SNR within different operational
contexts of hybrid FSO systems \[Ai et al., 2019\]. Additionally, a
comparative analysis of FSO detection techniques reveals differential
impacts on secrecy metrics, suggesting that choice of detection method
can be as pivotal as channel conditions or relaying strategy in securing
optical communications \[Ai et al., 2019\].

Expanding on these findings, Yang et al. (2018) investigate
physical-layer security in mixed RF/FSO dual-hop communication systems,
where the RF link is vulnerable to eavesdropping and experiences η–μ
fading, while the FSO link undergoes M-distribution fading known for its
high security \[Yang et al., 2018\]. The study provides analytical
expressions for average secrecy rate and secrecy outage probability,
demonstrating how both fixed and variable gain relaying schemes can be
optimized based on the specific fading conditions to enhance security
\[Yang et al., 2018\]. Particularly, variable gain relaying shows
potential for better adaptation to instantaneous channel conditions,
offering improved secrecy performance under certain scenarios \[Yang et
al., 2018\].

Building upon these insights, Zhang et al. (2020) further elucidate the
effectiveness of combining methods in enhancing physical layer security
for RF-FSO systems. Their research focuses on an asymmetric dual-hop
communication system where a partial relay selection scheme based on
maximum instantaneous channel gain for the RF link and an equal gain
combining scheme for processing signals at both destination and
eavesdropper are employed. This setup leverages multi-aperture
techniques to mitigate turbulence-induced fading effectively \[Zhang et
al., 2020\]. Theoretical analysis backed by Monte-Carlo simulations
confirms that these strategies significantly improve secrecy performance
metrics such as secrecy outage probability and strictly positive secrecy
capacity under various atmospheric conditions \[Zhang et al., 2020\].

El-Malek et al. (2016) contribute to this discussion by analyzing
multiuser SIMO mixed RF/FSO relay networks with opportunistic user
scheduling under Nakagami-m and gamma-gamma fading with pointing errors.
They employ maximum ratio combining and selection combining schemes to
optimize system performance metrics like outage probability, average
symbol error probability, and ergodic channel capacity. Their findings
demonstrate that opportunistic user scheduling enhances both security
and reliability by effectively managing trade-offs in complex channel
conditions \[El-Malek et al., 2016\]. Moreover, their proposed
cooperative jamming model significantly strengthens system security by
increasing intercept probability for potential eavesdroppers without
compromising quality of service \[El-Malek et al., 2016\].

Hu et al. (2020) address optimization problems in mixed RF/FSO spectrum
sharing networks aimed at enhancing physical-layer security through
advanced cooperative jamming techniques and sophisticated optimization
methods like the Dinkelbach method and semi-definite relaxation (SDR).
They propose three schemes: direct transmission, single-user cooperative
jamming, and multi-user cooperative beamforming jamming; each designed
to counteract eavesdropping threats effectively. Their findings
demonstrate that multi-user cooperative beamforming jamming achieves
higher secrecy rates compared to other strategies like zero-forcing
beamforming \[Hu et al., 2020\]. This research underscores the
importance of considering both RF and FSO channel characteristics and
mutual interference in designing security enhancements.

Shakir et al. (2022) add depth to this discourse by reviewing existing
literature on physical layer security in FSO systems, focusing on unique
challenges such as line-of-sight transmission susceptibility to
eavesdropping. They highlight effective techniques like noise
randomization, CSI utilization, multiantenna setups, acousto-optic
deflectors usage, advanced modulation schemes like orbital angular
momentum multiplexing under various atmospheric turbulence conditions
\[Shakir et al., 2022\]. These approaches offer computational efficiency
advantages over traditional cryptographic methods by securing data
without shared keys while addressing sophisticated eavesdropping
techniques.

By integrating these diverse factors—channel modeling, detection
techniques, atmospheric effects, SNR considerations, advanced relay
selection and signal combining strategies—both Ai et al. (2019), Yang et
al. (2018), Zhang et al. (2020), El-Malek et al. (2016), Hu et al.
(2020), and Shakir et al. (2022) provide a holistic view of the
challenges and considerations essential for optimizing physical layer
security in hybrid satellite-FSO communication systems and mixed RF/FSO
systems respectively. This research not only advances our understanding
of complex interdependencies within hybrid communication networks but
also sets a foundation for future investigations aimed at enhancing
robustness and security against diverse operational impairments \[Ai et
al., 2019; Yang et al., 2018; Zhang et al., 2020; El-Malek et al., 2016;
Hu et al., 2020; Shakir et al., 2022\].

❓ **Question 18: How does spatial diversity mitigate fading effects and
improve secrecy rates in dual-hop RF-FSO communication networks?**

IMPROVED SUMMARY: In their comprehensive analysis, Yang et al. (2018)
explore the enhancement of physical-layer security in mixed RF/FSO
dual-hop communication systems, focusing on the impact of η–μ and
M-distributed fading conditions. The study meticulously derives
analytical expressions for both average secrecy rate (ASR) and secrecy
outage probability (SOP), demonstrating that the system's secrecy
performance is significantly influenced by the fading environments and
the relaying strategies employed. The research highlights that while
fixed gain relaying schemes make the system's performance highly
sensitive to variations in average signal-to-noise ratio (SNR), variable
gain schemes adapt more dynamically to instantaneous channel conditions,
potentially enhancing secrecy under specific scenarios.

Building on these insights, Ai et al. (2019) delve into the physical
layer security of hybrid satellite-FSO cooperative systems, where
satellite links follow a shadowed-Rician fading distribution and
terrestrial links experience gamma-gamma fading. This study extends the
understanding of secrecy performance by incorporating different
detection techniques such as heterodyne detection and intensity
modulation with direct detection, as well as considering the impact of
pointing errors. The findings from Ai et al. reveal that in
amplify-and-forward (AF) schemes with fixed gain, the secrecy diversity
order is solely dependent on the FSO link's channel characteristics and
the detection technique used. In contrast, decode-and-forward (DF) or AF
with variable-gain schemes show no improvement in secrecy performance at
high SNR levels, indicating a zero secrecy diversity order.

Zhang et al. (2020) further enrich this discourse by analyzing an
asymmetric dual-hop RF-FSO communication system with a multi-aperture
destination and eavesdropper under Nakagami-m and Gamma-Gamma fading
conditions respectively. They employ a partial relay selection scheme
based on maximum instantaneous channel gain for the RF link and an equal
gain combining scheme for processing signals at both destination and
eavesdropper. Their study provides closed-form expressions for the lower
bound of secrecy outage probability and strictly positive secrecy
capacity, validated through Monte-Carlo simulations. The integration of
multi-aperture techniques is shown to significantly mitigate
turbulence-induced fading effects, enhancing physical layer security
even under challenging atmospheric conditions.

Hu et al. (2020) contribute to this evolving field by addressing
optimization problems in mixed RF/FSO spectrum sharing networks aimed at
maximizing secrecy rates in the presence of eavesdroppers. They propose
three innovative schemes: direct transmission, single-user cooperative
jamming, and multi-user cooperative beamforming jamming, which are
designed to counteract mutual interference between primary and secondary
networks while optimizing transmit and jamming power \[Hu et al.,
2020\]. Their approach utilizes advanced optimization techniques such as
the Dinkelbach method and semi-definite relaxation (SDR), proven
effective through Karush-Kuhn-Tucker conditions analysis. Notably, their
results demonstrate that multi-user cooperative beamforming jamming
achieves superior secrecy rates compared to traditional zero-forcing
beamforming methods \[Hu et al., 2020\].

Erdogan et al. (2022) enhance our understanding by focusing on mixed
RF-FSO relay networks under both RF and FSO eavesdropping attacks. They
emphasize the critical role of physical parameters like photo-aperture
size and placement in designing secure networks \[Erdogan et al.,
2022\]. By employing Nakagami-m fading for RF channels and exponentiated
Weibull distribution for FSO channels, they provide a detailed analysis
of how these factors influence secrecy metrics such as SOP and PPSC
\[Erdogan et al., 2022\]. Their findings underscore that larger
photo-apertures positioned higher enhance resistance to eavesdropping,
especially under adverse weather conditions \[Erdogan et al., 2022\].

Tonk et al. (2022) further investigate mixed RF/FSO cooperative relaying
systems where both hardware impairments at relay nodes and eavesdropping
threats are considered significant challenges \[Tonk et al., 2022\].
Utilizing Nakagami-m fading models for RF links and Malaga distribution
for FSO links affected by atmospheric turbulence and pointing errors,
they derive closed-form expressions for ASR using extended generalized
bivariate Fox H-function (EGBFHF). Their results highlight how hardware
impairments degrade ASR significantly, emphasizing the need for robust
security measures in high SNR scenarios \[Tonk et al., 2022\]. This
study underscores the vulnerability of these systems to both
eavesdropping attacks and hardware impairments, suggesting future
research directions towards advanced mitigation techniques.

Together, these studies provide a robust framework for understanding and
improving physical layer security across different types of dual-hop
communication systems under varying channel conditions and relaying
strategies. Yang et al., Ai et al., Zhang et al., Hu et al., Erdogan et
al., and Tonk et al collectively suggest future research could explore
more intricate channel models, advanced signal processing techniques,
adaptive relaying strategies based on dynamic channel state information,
integration of advanced detection techniques, mitigation of pointing
errors, development of countermeasures against complex eavesdropping
scenarios, and potential applications of machine learning for optimizing
system parameters under varying conditions.

❓ **Question 19: Can spatial diversity techniques be combined with
artificial noise generation to confuse eavesdroppers while preserving
secrecy in FSO links?**

IMPROVED SUMMARY: In their pivotal research, Sikri et al. (2021) delve
into the realm of enhancing secrecy in Free-Space Optical (FSO)
communications through artificial noise (AN) injection, focusing on
systems affected by Malaga (M) turbulence and pointing errors, employing
an intensity modulated direct detection (IM/DD) link. They successfully
derive closed-form expressions for key metrics such as secrecy outage
probability (SOP), strictly positive secrecy capacity (SPSC), and system
throughput, which serve as tools for evaluating the effectiveness of AN
injection in securing FSO communications against potential eavesdroppers
\[Sikri et al., 2021\].

Furthermore, Sikri et al. address the optimization of power allocation
between the information signal and AN. This optimization is crucial for
balancing throughput with enhanced security measures, indicating a
significant trade-off that must be managed to optimize both aspects
effectively \[Sikri et al., 2021\]. Additionally, this study sheds light
on broader environmental impacts on FSO performance, suggesting that
factors such as atmospheric conditions and physical obstructions play
critical roles in both system performance and security strategy
effectiveness.

Moreover, techniques for mitigating pointing errors—a common challenge
in FSO systems—are also discussed. Pointing errors can severely impact
the alignment between transmitting and receiving modules, thus degrading
both the signal quality received and the overall system's secure
communication capabilities. The integration of AN injection not only
compensates for some of these vulnerabilities but also prompts further
investigation into robust methods for error correction and system
stabilization in adverse conditions.

Building on this foundation, Boluda-Ruiz et al. (2019) introduce a new
misalignment error model to account for non-orthogonal optical beams at
the eavesdropper's receiver, characterized by a rotated ellipse
effective area. This model is essential for analyzing the secrecy outage
probability (SOP) under gamma-gamma turbulence conditions with pointing
errors. Their findings highlight how the eavesdropper's location and
orientation significantly influence SOP, particularly when the optical
beam becomes orthogonal to the photodetector plane \[Boluda-Ruiz et al.,
2019\]. The study emphasizes that higher SNR at the eavesdropper's
channel and larger normalized beamwidth at the receiver-side adversely
affect secrecy performance, underscoring the need for strategic design
considerations in high-risk environments.

Erdogan et al. (2022) analyze the secrecy performance of mixed RF/FSO
relay networks under both RF and FSO eavesdropping attacks. Their study
employs a dual-hop mixed RF-FSO relaying configuration with
decode-and-forward (DF) relaying techniques, where the RF channel is
modeled using Nakagami-m fading and the FSO channel using exponentiated
Weibull distribution. They highlight that both the location and size of
the photo-aperture significantly influence the secrecy performance in
mixed RF-FSO networks \[Erdogan et al., 2022\]. Specifically, a larger
photo-aperture and higher placement of the relay node enhance the
system's resistance to eavesdropping, particularly under harsh weather
conditions.

Ai et al. (2019) explore physical layer security within hybrid
satellite-FSO cooperative systems, where satellite links follow
shadowed-Rician fading distribution while terrestrial links experience
gamma-gamma fading. Their analysis reveals how different detection
techniques—heterodyne detection and intensity modulation with direct
detection—and pointing errors influence secrecy metrics like average
secrecy capacity and SOP \[Ai et al., 2019\]. Notably, they find that
amplify-and-forward (AF) relaying with fixed gain offers a unique
advantage by making secrecy diversity order solely dependent on FSO link
characteristics and detection type used.

Zhang et al. (2020) further enrich our understanding by investigating
physical layer security in asymmetric dual-hop RF-FSO communication
systems with multi-aperture destinations under multi-aperture
eavesdropping scenarios. They employ partial relay selection based on
maximum instantaneous channel gain for RF links alongside an equal gain
combining scheme to process signals at both destination and eavesdropper
points effectively \[Zhang et al., 2020\]. Their study demonstrates how
advanced relay selection techniques combined with robust signal
processing schemes can significantly enhance security against
sophisticated eavesdropping tactics under varying atmospheric
conditions.

This comprehensive approach not only advances our understanding of how
artificial noise can be used to fortify security in optical wireless
networks but also highlights essential considerations for deploying
these technologies in environments characterized by dynamic and
potentially disruptive atmospheric conditions. As such, Sikri et al.'s
work contributes significantly to both theoretical frameworks and
practical applications in securing FSO communications under complex
external influences \[Sikri et al., 2021\]. Future studies should
explore more advanced mitigation techniques for hardware impairments and
eavesdropping in mixed RF/FSO systems.

## Supertopic 2: Quantum Key Distribution (QKD) over FSO Systems

❓ **Question 1: Which quantum modulation protocols (BB84, DPS-QKD,
CVQKD) are most effective for secure key exchange over free-space
optical links?**

IMPROVED SUMMARY: In their comprehensive analysis, Sisodia et al. (2024)
delve into the efficacy of different Quantum Key Distribution (QKD)
protocols—specifically single-photon (BB84 and six-state) and
entangled-photon (Ekert91 and BBM92)—in the context of free-space
optical communication systems. The study meticulously evaluates how
these protocols fare in terms of quantum bit error rate (QBER) and
secure key rate (SKR), particularly under the influence of atmospheric
losses, geometrical losses, detector inefficiencies, and noise counts
including background radiation. It is highlighted that entangled-photon
based protocols exhibit superior resilience to noise impacts, thereby
offering enhanced security over their single-photon counterparts.
Moreover, the research underscores the critical influence of photon
collection efficiency on SKR, noting that effective photon capture
mechanisms are essential for maintaining high SKR despite adverse
conditions. Additionally, a comparative analysis reveals how varying
atmospheric conditions distinctly affect each protocol's performance,
with entangled-photon based protocols consistently outperforming
single-photon based ones across different scenarios.

Complementing this study, Stathis et al. (2024) introduce a novel
approach to QKD using cost-effective, commercially available components
in both fiber and free-space optical (FSO) links. Their research employs
a simplified single photon polarisation-encoded system that diverges
from traditional high-cost setups by focusing on practical
implementation aspects such as signal-to-noise ratio analysis and
semi-empirical theoretical frameworks simulating the DS-BB84 protocol.
This approach not only demonstrates feasible SKRs up to 600 bps in FSO
links but also highlights robust performance with QBER values below 3.7%
even in daylight operations.

Adding to these insights, Davidson et al. (2024) explore the integration
of Free-Space Optical communications with Quantum Key Distribution
within the AirQKD project, specifically employing the BB84 protocol in
real-world settings. This study involved deploying a system comprising
sophisticated subsystems for electronic/photonic and optical components
including single photon detectors and sources, quantum random number
generators, and dynamic alignment telescope systems. The experiments
conducted over distances up to 300 meters achieved a link loss of 12.3
dB initially, with subsequent tests predicting total losses up to 15.2
dB for QKD operations including detector losses. The controlled
background light levels around 5000 Hz per QKD channel facilitated
daylight operations while maintaining a security key rate of
approximately 453.8 kb/s based on the GLLP privacy amplification
equation for BB84 with infinite key transmission \[Davidson et al.,
2024\]. These results underscored the potential for FSO-QKD systems to
operate effectively under real-world conditions and highlighted the
importance of precise alignment and atmospheric considerations.

Further enriching this discourse, Kamran et al. (2020) propose a
practical implementation framework for the KMB09 protocol in Quantum Key
Distribution over free-space optical channels using higher order
Gaussian beam spatial modes encoded in higher dimensional photon states.
This innovative approach aims at enhancing secure communication over
long distances by utilizing complex beam spatial modes managed through
spatial light modulators (SLM). The simulation results confirm that this
method achieves theoretical efficiency values—0.25 for two-dimensional
states and 0.3683 for four-dimensional states—validating its
effectiveness in enhancing both security and communication distance
\[Kamran et al., 2020\].

Alshaer et al. (2020) contribute significantly to this field by
evaluating the performance of a ground-to-satellite FSO system employing
CV-QKD protocol under modulated gamma fading channels with bipolar pulse
amplitude modulation. Their findings include closed-form expressions for
joint probability, QBER, and quantum bit-discard rate (QBDR), optimized
through dual-threshold detection mechanisms \[Alshaer et al., 2020\].
This study not only validates these metrics through Monte Carlo
simulations but also optimizes them to enhance system security and
performance significantly under varying atmospheric conditions.

Trinh et al. (2018) introduce a novel QKD protocol designed for standard
FSO systems using subcarrier intensity modulation binary phase shift
keying combined with direct detection via a dual-threshold receiver
\[Trinh et al., 2018\]. This design allows implementation without
specialized quantum mechanics-based equipment while optimizing system
parameters like modulation depth under security constraints to achieve
robust performance even in dynamic atmospheric conditions.

These collective findings advance our understanding of how different QKD
protocols can be optimized under various environmental and technical
conditions to enhance secure communications in realistic settings. The
integration of cost-effective components as demonstrated by Stathis et
al. (2024), along with practical deployment insights from Davidson et
al. (2024), supports broader adoption and implementation of QKD systems.

❓ **Question 2: How does continuous-variable QKD (CVQKD) enhance
secrecy performance in satellite-based FSO quantum communication
networks?**

IMPROVED SUMMARY: In their groundbreaking study, Nguyen et al. (2023)
delve into the enhancement of satellite entanglement-based
continuous-variable quantum key distribution (EB/CV-QKD) within
free-space optical (FSO) communication networks. This research
introduces significant advancements such as optical phase-shift keying
(QPSK) signaling and dual-threshold/heterodyne detection (DT/HD)
receivers, which are designed to improve system reliability and
feasibility under a variety of channel impairments. The study employs
sophisticated channel modeling that accounts for atmospheric
attenuation, turbulence, and receiver noise across both tropospheric and
stratospheric layers, utilizing the Fisher-Snedecor F distribution to
accurately model turbulence-induced fading.

Further enhancing the robustness of satellite-to-ground quantum
communications, Zhao et al. (2019) propose an orthogonal frequency
division multiplexing (OFDM)-based CVQKD system specifically tailored
for mitigating the adverse effects of atmospheric turbulence on
satellite-to-ground FSO links. Their approach leverages multi-subcarrier
transmission to effectively suppress random fading and improve the
secret key rate, demonstrating a significant resilience compared to
traditional single-channel systems. The integration of OFDM in CVQKD
systems addresses critical challenges posed by atmospheric conditions,
highlighting the effectiveness of multi-subcarrier systems in enhancing
both the robustness and key generation rates of quantum communications.

Alshaer et al. (2022) contribute to this field by evaluating the
performance of a UAV-based FSO system employing a CV-QKD protocol with
Gaussian modulation of quantum coherent states (GMCS). They focus on
optimizing system parameters such as transmit power,
receiver<span dir="rtl">’</span>s field-of-view, and beam divergence
angle based on threshold values for QBER and outage probability. Their
findings demonstrate that by carefully adjusting these parameters,
UAV-based FSO systems can maintain a QBER below 10−3 and an outage
probability below 10−2 even under conditions of atmospheric turbulence
and excess noise. The study also highlights the system's resilience to
boresight displacement up to 7 cm, validated through Monte-Carlo
simulations \[Alshaer et al., 2022\].

Alshaer et al. (2020) further explore ground-to-satellite FSO
communication employing CV-QKD with bipolar pulse amplitude modulation
over a modulated gamma fading channel. They derive closed-form
expressions for joint probability, quantum bit-error-rate (QBER), and
quantum bit-discard rate (QBDR), optimizing dual-threshold detection
ranges to enhance security and performance under varying atmospheric
conditions.

The enhancements proposed by Nguyen et al. (2023) are shown to
effectively reduce QBER and improve sift probability, thereby optimizing
system performance in adverse conditions. The authors provide a detailed
comparative analysis with previous satellite QKD/FSO systems, including
those enhanced by Zhao et al. (2019) and Alshaer et al. (2020),
underscoring significant advancements over traditional methods used in
earlier systems through comprehensive channel modeling strategies.

Gyongyosi et al. (2019) enrich our understanding by deriving maximal
achievable secret key rates for CVQKD over FSO channels, particularly
under low-SNR scenarios prevalent in satellite communications due to
atmospheric disturbances and other environmental factors. Their
analytical focus on channel decomposition and SNR characteristics
provides crucial insights into optimizing CVQKD systems under
challenging conditions \[Gyongyosi et al., 2019\].

Looking forward, Nguyen et al. (2023) outline potential future research
directions for satellite EB/CV-QKD/FSO systems suggesting that further
improvements could be achieved through advanced encoding and decoding
techniques tailored for these high-demand applications. Additionally,
integrating sophisticated error correction methods and exploring new
quantum-resistant cryptographic algorithms are recommended to further
enhance system security and efficiency.

Overall, Nguyen et al. (2023) present a robust framework for optimizing
satellite EB/CV-QKD/FSO systems through strategic technological
enhancements and detailed performance analysis. Their work sets a
foundational basis for future innovations in global 6G networks'
security protocols, confirming that careful consideration of channel
impairments and system parameters supported by robust theoretical and
numerical analysis from studies like Zhao et al., Alshaer et al.,
Gyongyosi et al., is essential for advancing these sophisticated quantum
key distribution systems.

❓ **Question 3: What methods allow the integration of quantum key
distribution with orbital angular momentum (OAM) modes in FSO links, and
what benefits do they provide?**

IMPROVED SUMMARY: The comprehensive study by Vu et al. (2020) and
Davidson et al. (2024) delves into the optimization and practical
deployment of Free-Space Optical (FSO) Quantum Key Distribution (QKD)
systems, tailored for secure vehicular networks and metropolitan-scale
last-mile connectivity respectively. Vu et al. (2020) focus on
relay-assisted satellite FSO QKD systems, analyzing the impact of
transceiver misalignment, receiver velocity variations, inherent
receiver noises, and atmospheric turbulence on key performance metrics
such as quantum bit error rate and ergodic secret-key rate. Through
theoretical modeling and simulation, they demonstrate that optimal
system parameters, including modulation depth and optical amplifier gain
at High-Altitude Platforms (HAPs), can significantly mitigate
disturbances ensuring security within acceptable limits under moderate
atmospheric conditions \[Vu et al., 2020\].

Davidson et al. (2024) extend this discussion by detailing the design,
development, and real-world testing of an FSO system integrated with QKD
technology using the BB84 protocol. Their system includes sophisticated
subsystems such as single photon detectors, quantum random number
generators, and dynamic telescope alignment capabilities to address
real-life use cases over distances up to 300 meters. The study
highlights the importance of precise alignment and atmospheric
considerations in deploying FSO-QKD systems, achieving a link loss of
12.3 dB in initial tests with a security key rate estimated around 453.8
kb/s \[Davidson et al., 2024\].

Both studies emphasize the necessity of adaptive optics for real-time
alignment correction to maintain high fidelity in quantum key
distribution despite dynamic operational environments characterized by
movement and atmospheric variability \[Vu et al., 2020; Davidson et al.,
2024\]. Furthermore, Davidson et al. (2024) propose the integration of
machine learning techniques for predictive error correction as a
forward-thinking approach to preemptively address potential disruptions
in quantum key transmission.

Adding to these insights, Nguyen et al. (2023) introduce enhancements in
satellite entanglement-based continuous-variable quantum key
distribution (EB/CV-QKD) systems for global 6G networks. They propose
the use of optical phase-shift keying (QPSK) signaling and
dual-threshold/heterodyne detection (DT/HD) receivers to improve
reliability and feasibility under various channel impairments including
atmospheric attenuation and turbulence modeled by the Fisher-Snedecor F
distribution \[Nguyen et al., 2023\]. Their findings underscore
significant improvements in handling channel impairments through
comprehensive channel modeling, which optimizes system parameters like
receiver<span dir="rtl">’</span>s aperture radius,
detector<span dir="rtl">’</span>s threshold scale coefficient, and
transmit beam<span dir="rtl">’</span>s divergence angle for enhanced
performance.

Mallick et al. (2023) explore the implementation of QKD over an FSO
channel using the CASCADE protocol under various atmospheric conditions
such as haze, rain, and snow. Their simulation-based approach employs
continuous-wave lasers, optical attenuators, polarizers, and
polarization analyzers to model the transmission of quantum states
through these challenging conditions \[Mallick et al., 2023\]. The
CASCADE protocol's role in error reconciliation is highlighted by its
effectiveness in reducing transmission errors and improving signal
integrity across different atmospheric turbulences.

Kamran et al. (2020) introduce a novel framework for implementing the
KMB09 protocol in QKD systems using higher dimensional photon states
encoded in higher order Gaussian beam spatial modes. This approach is
designed to enhance secure communication over long distances by
utilizing spatial light modulators (SLM) to manage complex beam spatial
modes effectively \[Kamran et al., 2020\]. The simulation results
confirm that this method aligns with theoretical predictions,
demonstrating efficiencies of 0.25 for two-dimensional states and 0.3683
for four-dimensional states \[Kamran et al., 2020\].

Stathis et al. (2024) contribute significantly by demonstrating a
cost-effective approach to QKD using polarisation-encoded single photons
across both fiber and FSO links under realistic conditions. Their
research emphasizes practical implementations using commercial
off-the-shelf components while achieving Secure Key Rates up to 600 bps
\[Stathis et al., 2024\]. This study not only bridges high-end
technologies with economical solutions but also validates the robustness
of simplified setups in everyday scenarios within metropolitan networks.

Collectively, these studies advocate for a meticulously engineered
approach to enhance secure quantum communications across different
networks—vehicular or metropolitan—navigating through challenging
atmospheric landscapes. Future research will focus on optimizing system
components for reduced losses and improved alignment stability while
extending communication range and developing robust protocols for
varying atmospheric conditions \[Davidson et al., 2024; Mallick et al.,
2023; Kamran et al., 2020; Nguyen et al., 2023; Stathis et al., 2024\].
This integration presents a viable solution for enhancing secure
communications, particularly in environments where traditional fiber
optics are impractical, complementing existing technologies like 5G
\[Davidson et al., 2024\].

❓ **Question 4: What advantages does OAM encoding offer for
implementing high-dimensional quantum states in QKD protocols over FSO
channels?**

IMPROVED SUMMARY: The comprehensive study by Kamran et al. (2020) delves
into an advanced framework for implementing the KMB09 protocol within
quantum key distribution (QKD) systems, leveraging higher dimensional
photon states encoded through higher order Gaussian beam spatial modes.
This research meticulously constructs a simulation setup incorporating
elements such as a laser source, attenuators, beam expanders, spatial
light modulators (SLM), and single-photon detectors to evaluate the
efficiency of this protocol in both two and four-dimensional photon
state configurations. The results from these simulations are promising,
showing an efficiency rate of 0.25 for two-dimensional states and 0.3683
for four-dimensional states, which are consistent with prior numerical
and analytical evaluations of the KMB09 protocol.

This study not only confirms the practical viability of this
sophisticated quantum communication protocol but also underscores the
critical role played by spatial light modulators in managing intricate
beam spatial modes that are central to achieving high-dimensional
quantum state encoding over free-space optical (FSO) channels. Such
advancements are pivotal as they potentially enhance both the security
measures and transmission distances achievable in quantum key
distribution systems.

Moreover, while this research focuses on a novel QKD scheme distinct
from traditional protocols like BB84, it provides an essential
comparative insight that could influence future cryptographic strategies
in FSO communications. Additionally, it acknowledges the significant
impact atmospheric conditions can have on FSO communications—a factor
that must be rigorously accounted for to optimize system performance
under various environmental scenarios.

Further expanding on the challenges of atmospheric conditions, Mallick
et al. (2023) explore the implementation of QKD over FSO channels using
the CASCADE protocol under varying atmospheric disturbances such as
haze, rain, and snow. Their findings highlight how the CASCADE protocol
effectively reduces transmission errors and improves sequence recovery
rates across different atmospheric conditions \[Mallick et al., 2023\].
This enhancement in error reconciliation capabilities is quantitatively
demonstrated through improved optical spectrum analysis at both
transmitter and receiver ends, ensuring robust security for sensitive
information transmission across different sectors.

Incorporating insights from Nguyen et al. (2023), significant
advancements in satellite entanglement-based continuous-variable quantum
key distribution (EB/CV-QKD) systems are highlighted. These systems
utilize optical phase-shift keying (QPSK) signaling and
dual-threshold/heterodyne detection (DT/HD) receivers to enhance
reliability and feasibility under channel impairments such as
atmospheric attenuation, geometric spreading loss, and
turbulence-induced fading \[Nguyen et al., 2023\]. The integration of
these techniques significantly reduces quantum bit errors and enhances
system reliability by considering comprehensive channel models for
accurate performance analysis.

Additionally, Vu et al. (2020) demonstrate significant advancements in
relay-assisted satellite FSO QKD systems designed for secure vehicular
networks. The use of high-altitude platforms (HAPs) equipped with
optical amplify-and-forward nodes as relay stations addresses key
challenges such as transceiver misalignment, receiver's velocity
variation, receiver noises, and atmospheric turbulence \[Vu et al.,
2020\]. These systems demonstrate that with optimal modulation depth and
optical amplifier gain settings at the HAPs, quantum bit error rates and
ergodic secret-key rates remain within acceptable limits even under
moderate atmospheric turbulence.

Alshaer et al. (2021) further enrich this discourse by integrating a
time-bin entanglement protocol with a UAV-based FSO communication
platform for QKD. Their study evaluates performance under dynamic
conditions including UAV positional variances and atmospheric
impairments like turbulence and pointing errors \[Alshaer et al.,
2021\]. The use of a tracking system to adjust for UAV positional and
orientational variances significantly enhances system reliability under
these conditions. Moreover, their findings suggest that careful
optimization of system parameters such as field-of-view, signal-to-noise
ratio, and time-bin configuration is crucial for maximizing security and
performance in dynamic aerial environments \[Alshaer et al., 2021\].

Looking forward, both studies set a foundational basis for subsequent
investigations aimed at further refining these protocols under diverse
operational conditions and integrating additional quantum states and
dimensions into practical QKD systems. Future research directions
include exploring other advanced error reconciliation protocols like
LDPC and Winnow to enhance the efficiency and security of QKD systems
over FSO channels \[Mallick et al., 2023\]. Additionally, investigating
the system's performance under more extreme atmospheric conditions and
implementing Multi-Input-Multi-Output (MIMO) and Wavelength Division
Multiplexing (WDM) technologies could further optimize the system's
capabilities. These future research directions are crucial for advancing
our understanding and capabilities in secure quantum communications
across expansive distances.

❓ **Question 5: What experimental demonstrations exist for OAM-based
quantum communication over satellite or long-range free-space optical
links?**

IMPROVED SUMMARY: The research conducted by \[Stathis et al., 2024\] and
\[Davidson et al., 2024\] provides comprehensive insights into the
practical application of Quantum Key Distribution (QKD) using both fiber
optic and Free-Space Optical (FSO) communication systems, employing
economically viable, commercially available components. These studies
explore the integration of QKD in diverse environments, focusing on
metropolitan-scale networks and addressing the challenges posed by
atmospheric conditions and alignment requirements.

\[Stathis et al., 2024\] utilizes a polarization-encoded single photon
system within a semi-empirical theoretical framework simulating the
DS-BB84 protocol. The experiments assess feasibility over a 2.2 km
intra-campus fiber link and shorter-range FSO links (40 m indoor and 100
m outdoor). The study achieved an expected Secure Key Rate (SKR) of up
to 300 bps in fiber links by optimizing Wavelength-Division Multiplexing
allocations to minimize Raman noise. For FSO links, despite
environmental interferences, Quantum Bit Error Rates (QBER) were
maintained below 3.2%, with potential SKRs up to 600 bps, demonstrating
robust performance even in daylight operations.

In contrast, \[Davidson et al., 2024\] outlines the deployment of an FSO
system integrated with QKD technology using the BB84 protocol over
distances up to 300 meters. This setup included advanced components such
as single photon detectors and quantum random number generators,
achieving a link loss of 12.3 dB in initial tests with controlled
background light levels suitable for daylight operation. The security
key rate was estimated around 453.8 kb/s based on the GLLP privacy
amplification equation for BB84, considering infinite key transmission.

Adding to these advancements, \[Sorgi et al., 2024\] introduces a novel
cryogen-free THz FSO communication system that operates effectively
within the 1–5 THz range, demonstrating significant improvements in
terms of operational simplicity and cost-effectiveness. This system
employs a directly modulated 2.83 THz QCL transmitter within a
closed-cycle Stirling cryocooler and a room-temperature graphene-based
field-effect transistor as the receiver. The experimental setup includes
power-versus-distance measurements and communication tests to evaluate
the signal-to-noise ratio (SNR) and packet error rate (PER) at varying
distances and signal amplitudes. A propagation model is also developed
to estimate the performance of the THz link under optimized conditions,
achieving error-free communication over distances up to 128 cm at data
rates of 1 Mbps using binary on-off keying with Manchester encoding.

\[Vu et al., 2020\] extends this discussion to relay-assisted satellite
FSO QKD systems designed for secure vehicular networks. This study
emphasizes the use of high-altitude platforms (HAPs) equipped with
optical amplify-and-forward nodes as relay stations, which are crucial
under varying atmospheric turbulence and operational challenges such as
transceiver misalignment and receiver mobility. The analysis shows that
quantum bit error rates and ergodic secret-key rates remain within
acceptable limits under moderate atmospheric turbulence with optimal
system parameter settings like modulation depth and optical amplifier
gain at the HAPs.

\[Nguyen et al., 2023\] further enhances our understanding by focusing
on satellite entanglement-based continuous-variable quantum key
distribution (EB/CV-QKD) systems over free-space optical links between
satellites and ground stations. Their study employs advanced techniques
such as optical phase-shift keying (QPSK) signaling and
dual-threshold/heterodyne detection (DT/HD) receivers to improve
reliability and feasibility under various channel impairments including
atmospheric attenuation, geometric spreading loss, and
turbulence-induced fading modeled by the Fisher-Snedecor F distribution.
They provide detailed numerical results demonstrating how these
enhancements significantly reduce quantum bit errors and enhance system
reliability for global security applications in upcoming
sixth-generation (6G) wireless communications.

Future work will focus on optimizing system components and expanding the
range and stability of communication links across these platforms.
Enhancements in hardware integration for reduced losses and improved
alignment stability are crucial for extending communication ranges and
developing robust protocols that can withstand diverse operational
environments.

Together, these studies pave the way for broader adoption and
implementation of secure quantum communications using accessible
technologies across diverse and realistic environments, enhancing
network security and connectivity, particularly in last-mile
applications within metropolitan networks.

❓ **Question 6: How does mode fidelity degradation in OAM channels
affect the security and key generation rate of OAM-QKD systems?**

IMPROVED SUMMARY: In their pivotal study, Ahmed et al. (2022) delve into
the intricacies of security in Continuous Variable Quantum Key
Distribution (CV-QKD) systems that utilize a local-local oscillator
(LLO), specifically within Free-Space Optical (FSO) channels. The
research employs a log-negative Weibull distribution to accurately model
channel transmittance, which is crucial under varying environmental
conditions that typically affect FSO communications. Furthermore, a
trusted noise model is meticulously analyzed to account for excess
noise, which plays a significant role in determining system robustness
against external disturbances and potential eavesdropping activities.

The performance evaluation of Gaussian modulation (GM) versus discrete
modulation (DM) under scenarios of weak turbulence showcases that GM not
only sustains higher secret key rates (SKRs) over extended distances but
also demonstrates resilience when faced with optimal modulation variance
settings. This finding is particularly relevant when considering the
impact of phase and amplitude attacks on the system's integrity. Phase
attacks are highlighted as more detrimental compared to amplitude
attacks, leading to a more rapid degradation of the communication link.

Moreover, the study emphasizes the importance of evaluating system
performance through various attack scenarios to better understand
vulnerabilities and enhance security protocols in CV-QKD systems. Such
evaluations help in developing strategic approaches to mitigate risks
associated with phase and amplitude manipulations by potential
adversaries.

Expanding on the theme of quantum key distribution, Kamran et al. (2020)
introduce an innovative framework for implementing the KMB09 protocol in
QKD systems using higher dimensional photon states encoded in higher
order Gaussian beam spatial modes. This protocol aims to enhance secure
communication over long distances by utilizing complex beam spatial
modes managed by spatial light modulators (SLM). The simulation results
confirm the feasibility of this approach, demonstrating efficiencies
that align with theoretical predictions for two and four-dimensional
photon states. These findings underscore the potential of integrating
advanced quantum states and spatial mode controls to improve both the
security and efficiency of QKD systems over long distances.

Building on these insights, Sisodia et al. (2024) provide a comparative
analysis of single-photon and entangled-photon based QKD protocols under
free-space losses and device imperfections. Their study reveals that
entangled-photon protocols like BBM92 and Ekert91 exhibit superior noise
tolerance and enhanced security over single-photon protocols such as
BB84 and six-state, especially under conditions of high channel losses
and detector inefficiencies \[Sisodia et al., 2024\]. This underscores
the critical role of minimizing free-space losses and optimizing device
performance to achieve low QBER and high SKR in practical QKD
implementations.

Adding to this body of knowledge, Mallick et al. (2023) explore the
implementation of quantum key distribution over FSO channels using the
CASCADE protocol under various atmospheric conditions such as haze,
rain, and snow. Their study utilizes MATLAB and OptiSystem software to
simulate a QKD system incorporating continuous-wave lasers, optical
attenuators, polarizers, and polarization analyzers. The CASCADE
protocol effectively reduces transmission errors across these
challenging conditions, enhancing both error correction rates and
original sequence recovery \[Mallick et al., 2023\]. This integration
highlights how atmospheric turbulence can be mitigated through advanced
error reconciliation techniques in FSO-based QKD systems.

Alshaer et al. (2021) further enrich this discourse by analyzing an
entanglement-based QKD protocol within a dynamic ground-to-UAV FSO
communication system. They focus on optimizing system parameters such as
field-of-view, signal-to-noise ratio, and time-bin configuration to
maximize raw and secret key rates while maintaining robust performance
metrics under practical operational conditions including UAV positional
variances \[Alshaer et al., 2021\]. Their findings suggest that careful
optimization is crucial for maximizing security and performance in
dynamic UAV applications.

Gyongyosi et al. (2019) contribute significantly by deriving maximal
achievable secret key rates for CVQKD over FSO channels under low-SNR
conditions \[Gyongyosi et al., 2019\]. Their research provides essential
insights into channel decomposition and SNR characteristics crucial for
practical implementations in wireless quantum key distribution networks
aimed at supporting the quantum Internet infrastructure.

The comprehensive analysis provided by Ahmed et al., Kamran et al.,
Sisodia et al., Mallick et al., Alshaer et al., and Gyongyosi et al.,
underscores the necessity for ongoing advancements in modulation
techniques, photon management, error reconciliation protocols, and
security measures to bolster the reliability and safety of quantum key
distribution in free-space optical channels (\[Ahmed et al., 2022\];
\[Kamran et al., 2020\]; \[Sisodia et al., 2024\]; \[Mallick et al.,
2023\]; \[Alshaer et al., 2021\]; \[Gyongyosi et al., 2019\]). Future
research will explore further optimization and testing under various
environmental conditions, including more severe atmospheric disturbances
while investigating other advanced error reconciliation protocols like
LDPC and Winnow to enhance efficiency and security (\[Mallick et al.,
2023\]).

❓ **Question 7: What are the main technical limitations in combining
CVQKD with OAM in practical FSO deployments?**

IMPROVED SUMMARY: The integration of Continuous Variable Quantum Key
Distribution (CV-QKD) with UAV-based Free-Space Optical (FSO)
communication systems, as explored by \[Alshaer et al., 2022\], presents
a novel approach to secure optical communications under practical
conditions. This research delves into performance optimization amidst
challenges such as atmospheric turbulence and excess noise, employing
theoretical modeling and Monte-Carlo simulations to optimize key
parameters including transmit power, receiver<span dir="rtl">’</span>s
field-of-view, and beam divergence angle. These parameters are
meticulously adjusted to maintain a Quantum Bit Error Rate (QBER) below
10^(-3) and an outage probability below 10^(-2), crucial for reliable
communication under varying atmospheric conditions.

Further enhancing the robustness of CV-QKD systems, the study by \[Zhao
et al., 2019\] introduces an OFDM-based CVQKD system for
satellite-to-ground FSO links, focusing on overcoming atmospheric
turbulence effects. The system utilizes multi-subcarrier transmission to
mitigate fading effects and improve the secret key rate. The performance
analysis involves Monte Carlo simulations to estimate transmittance
distributions of fluctuating quantum channels and examines the impact of
scintillation index, atmospheric transmittance, and phase noise on
system performance. The OFDM-based CVQKD system demonstrated improved
resilience to atmospheric turbulence compared to single-channel systems.
The use of multiple subcarriers allowed for a higher secret key rate
within a specific range of subcarrier numbers. However, limitations in
technology and device capabilities restrict the reduction of symbols per
channel, impacting the asymptotic performance assumptions.

Additionally, the study by \[Alshaer et al., 2020\] evaluates the
performance of a ground-to-satellite FSO system using bipolar pulse
amplitude modulation over modulated gamma fading channels. It introduces
dual-threshold detection in the CV-QKD protocol, optimizing the
dual-threshold range based on derived metrics such as QBER and quantum
bit-discard rate (QBDR). The research validates these metrics through
Monte Carlo simulations and numerical analysis, ensuring robust system
security and maximizing information capacity at a scaling coefficient of
0.3 × 10^(-6). This highlights the effectiveness of optimized
dual-threshold detection and scaling coefficients in enhancing security
and performance in ground-to-satellite communications.

Building upon these advancements, \[Nguyen et al., 2023\] introduces
enhancements in satellite entanglement-based CV-QKD systems using
optical phase-shift keying (QPSK) signaling and
dual-threshold/heterodyne detection (DT/HD) receivers. This approach
addresses channel impairments more effectively by incorporating
comprehensive channel models that include atmospheric attenuation,
geometric spreading loss, and turbulence-induced fading modeled by the
Fisher-Snedecor F distribution. The study provides closed-form
expressions for key system performance metrics such as QBER, sift
probability, and Eve's error probability, demonstrating significant
improvements in handling channel impairments and system feasibility.

The application of Gaussian Modulation of Quantum Coherent States (GMCS)
in the CV-QKD setup is instrumental in enhancing security against
collective attacks over FSO links. The integration of GMCS with CV-QKD
significantly bolsters the security framework, providing robust defense
mechanisms against potential eavesdroppers due to the line-of-sight
nature of FSO communications.

Furthermore, both studies emphasize the necessity of precise parameter
selection to combat the implications of atmospheric conditions on system
behavior. The resilience to UAV positional deviations is particularly
noted in \[Alshaer et al., 2022\], where a boresight displacement up to
7 cm can be tolerated without compromising communication integrity.

Incorporating insights from \[Yuan et al., 2023\], this summary also
explores how Free-Space Optical Quantum Key Distribution (FSO-QKD) can
be effectively integrated into a 6G-V2X communication architecture to
enhance security while addressing line-of-sight challenges. The study
utilized theoretical modeling and simulations to analyze LOS
requirements essential for effective quantum key distribution within
urban environments. A Poisson Point Process model was employed to
simulate the distribution and density of Road Side Units (RSUs) and
their connectivity to Quantum Key Base Stations (QKBSs). The simulation
results indicated significant challenges in maintaining LOS connections
in dense urban environments, which are critical for effective quantum
key distribution. The research highlighted that increasing RSU density
could partially mitigate LOS issues but emphasized strategic placement
for optimal key distribution pathways.

This comprehensive examination not only advances our understanding of
secure UAV-based FSO communications but also sets a benchmark for future
research in this area by addressing both performance optimization and
security enhancements within UAV-based CV-QKD-enabled FSO systems.
Future research should focus on experimental validation of these
protocols in real-world FSO systems to confirm theoretical predictions
and explore adaptive modulation techniques under dynamic atmospheric
conditions. Additionally, further enhancements in encoding and decoding
techniques should be explored along with the integration of adaptive
optics to mitigate atmospheric turbulence effects \[Nguyen et al.,
2023\].

## Supertopic 3: Hybrid RF-FSO Security Strategies

❓ **Question 1: What performance metrics (BER, secrecy rate, outage
probability) characterize RIS-assisted dual-hop RF-FSO networks under
eavesdropping scenarios?**

IMPROVED SUMMARY: In their comprehensive analysis, Ahmed et al. (2023)
delve into the enhancement of physical layer security within a dual-hop
RIS-assisted RF-FSO communication system under various eavesdropping
scenarios. The study meticulously derives and validates closed-form
expressions for key secrecy metrics such as average secrecy capacity,
secrecy outage probability, and effective secrecy throughput. These
metrics are crucial in assessing the robustness of the communication
system against potential security breaches.

The research highlights the significant role of Reconfigurable
Intelligent Surfaces (RIS) in improving physical layer security.
Specifically, RIS technology facilitates dynamic phase adjustment of
signals, which is pivotal in countering eavesdropping attempts across
both RF and FSO links. This capability is particularly beneficial in
environments subjected to complex interference and fading scenarios.

Furthermore, the study addresses the impact of pointing errors on the
performance of the FSO link. Pointing errors, often caused by alignment
inaccuracies between transceiver elements, can significantly degrade the
optical link's effectiveness. The inclusion of RIS helps mitigate these
effects by enhancing signal alignment through adaptive phase
adjustments.

Additionally, Ahmed et al. (2023) explore various techniques to optimize
RIS performance which include strategic placement and orientation of
reflective elements to maximize signal integrity and minimize potential
security loopholes. These techniques are essential for maintaining high
levels of secrecy performance under diverse atmospheric conditions that
typically affect RF-FSO systems.

Building on these findings, Wang et al. (2024) further investigate the
physical layer security in mixed RF/FSO systems enhanced by RIS-aided
jamming to thwart eavesdroppers. Their study confirms that using a
wireless-powered jammer to transmit signals reflected by an RIS
significantly reduces secrecy outage probability and enhances average
secrecy capacity. They provide detailed analysis on how system
parameters like time switching factor, energy conversion efficiency, and
average interference noise ratio influence these security metrics.

Wang et al. (2024) also demonstrate that increasing the number of RIS
reflecting elements and optimizing link distances can substantially
improve system security against eavesdropping. Their comparative
analysis with RIS-free systems underscores the transformative impact of
RIS technology on enhancing physical layer security.

Liu et al. (2024) extend this exploration within a NOMA-enabled dual-hop
FSO-RF network, where they analyze different user scenarios including
those without direct paths from relay to user, relying solely on
RIS-reflected paths or a combination of both direct and reflected paths.
Their findings reveal that configurations combining both path types
generally yield superior secrecy outcomes due to enhanced signal
manipulation capabilities provided by RIS under Gamma-Gamma distributed
FSO links and Nakagami-m faded RF channels. The study emphasizes that
strategic placement of RIS elements along with optimal transmission
power and beam direction adjustments are critical for maximizing system
security.

Sun et al. (2024) contribute significantly by analyzing how atmospheric
turbulence, pointing errors, detection technology, path loss, and energy
harvesting affect the secrecy performance in mixed RF-FSO downlink SWIPT
systems \[Sun et al., 2024\]. They highlight that improvements in
pointing accuracy and adopting heterodyne detection can notably enhance
secrecy performance \[Sun et al., 2024\]. Moreover, their findings
underscore that path loss and energy harvesting parameters critically
influence the system's secrecy capacity \[Sun et al., 2024\],
emphasizing practical trade-offs in system design.

Both studies collectively underscore the efficacy of RIS in securing
wireless communications and provide a robust framework for future
enhancements in physical layer security technologies within RF-FSO
systems. They suggest that future research should explore optimization
of RIS configurations under various environmental conditions and
consider integrating advanced machine learning techniques for dynamic
configuration to further enhance system security.

❓ **Question 2: Can intermediate relays in RF-FSO dual-hop systems act
as friendly jammers, and how does this strategy improve secrecy
capacity?**

IMPROVED SUMMARY: In their detailed investigation, Mandira et al. (2023)
delve into optimizing secrecy performance in mixed RF-FSO communication
systems under challenging fading conditions, specifically α−η−μ and
Málaga turbulence. The research meticulously develops a mathematical
framework using univariate and bivariate Meijer<span dir="rtl">’</span>s
G and Fox<span dir="rtl">’</span>s H functions to derive critical
secrecy metrics such as average secrecy capacity, secrecy outage
probability, and probability of non-zero secrecy capacity. These metrics
are validated through Monte-Carlo simulations, highlighting that
heterodyne detection (HD) significantly outperforms intensity modulation
with direct detection (IM/DD) in maintaining secrecy.

Expanding on this foundation, Pattanayak et al. (2020) explore the
physical layer security (PLS) of a dual-hop two-way relaying (TWR) based
mixed FSO/RF system in the presence of multiple eavesdroppers. This
study employs a system configuration involving two legitimate nodes and
three eavesdroppers, with RF links modeled using Nakagami-m fading
distribution and FSO links characterized by Málaga distribution. The
research emphasizes the impact of pointing errors and compares different
detection techniques—IM/DD and HD—on system reliability and security
performance. Closed-form expressions for secrecy outage probability
(SOP) and secrecy throughput (ST) are derived using
Meijer<span dir="rtl">’</span>s G-function, with results validated
through Monte Carlo simulations \[Pattanayak et al., 2020\].

Both studies underscore the importance of considering atmospheric
turbulence and pointing errors in assessing system performance. Mandira
et al. (2023) focus on the variable gain relaying channel where precise
alignment is crucial for optimal operation and robustness against
eavesdropping attempts. Meanwhile, Pattanayak et al. (2020) provide a
comparative analysis of detection techniques, advocating for HD due to
its enhanced resilience against both atmospheric turbulence and pointing
inaccuracies.

Lei et al. (2018) further enrich this discussion by analyzing a secure
dual-hop mixed RF-FSO downlink SWIPT system where both the FSO link
experiences Gamma-Gamma fading and RF links undergo Nakagami-m fading.
Their study reveals that the interdependence of these links
significantly complicates the analysis of secrecy performance,
particularly under conditions of atmospheric turbulence, pointing
errors, path loss, and energy harvesting \[Lei et al., 2018\]. They
derive a closed-form expression for SOP and demonstrate through
Monte-Carlo simulations that the secrecy diversity order (SDO) is
influenced by various factors including the fading parameters of both
links, the number of destination antennas, pointing accuracy, and
detection technology used.

Saber et al. (2020) contribute to this body of knowledge by examining a
mixed RF-FSO decode-and-forward relaying system integrated with energy
harvesting technology. They provide analytical closed-form expressions
for average secrecy capacity (ASC) and secrecy outage probability (SOP),
demonstrating how these metrics are influenced by system parameters such
as power splitting ratio, turbulence conditions, and pointing errors
\[Saber et al., 2020\]. Their findings highlight how physical-layer
security performance improves with increasing SNR at the relay and
destination while deteriorating with higher SNR at the eavesdropper.

Sharma et al. (2024) extend these analyses by focusing on hybrid FSO-RF
systems employing Gamma-Gamma distributed channel gain for FSO links and
Nakagami-m fading for RF links in a two-hop communication model. They
derive closed-form expressions for end-to-end secrecy capacity using
Meijer<span dir="rtl">’</span>s G-function to represent incomplete gamma
functions under various LOS and non-LOS conditions \[Sharma et al.,
2024\]. Their results demonstrate that increasing SNR values initially
boost secrecy capacity but then saturate due to fixed FSO channel SNR
values.

Wang et al. (2023) introduce an innovative approach by integrating
Reconfigurable Intelligent Surfaces (RIS) into these systems to act as
friendly jammers enhancing physical layer security \[Wang et al.,
2023\]. By reflecting jamming signals towards potential eavesdroppers
using RIS technology, they significantly reduce the secrecy outage
probability while boosting average secrecy capacity in environments
characterized by Nakagami-m fading for RF links and Málaga turbulence
for FSO links.

Future research should explore more complex eavesdropping scenarios and
additional mixed communication models while investigating the impact of
adaptive control over system parameters such as energy harvesting
efficiency and pointing accuracy on security performance \[Lei et al.,
2018; Mandira et al., 2023; Pattanayak et al., 2020; Saber et al., 2020;
Wang et al., 2023\]. Additionally, integrating advanced machine learning
techniques to predict and mitigate potential security threats in
real-time could offer significant advancements in protecting these
sophisticated communication systems.

❓ **Question 3: How do relay placement and UAV-based relay mobility
affect secrecy performance in hybrid RF-FSO secure networks?**

IMPROVED SUMMARY: In their comprehensive analysis, Song et al. (2025)
delve into the utilization of a hybrid RF/FSO system to significantly
enhance the security dimensions of UAV communications. The study
meticulously formulates an approach where data is transmitted
simultaneously through both RF and FSO links to tackle secure and covert
communication challenges effectively. This dual-link strategy is
particularly advantageous in scenarios involving active eavesdroppers,
where traditional single-channel systems might falter. To quantitatively
assess the security performance, Song et al. derive closed-form
expressions for secrecy outage probability (SOP) and effective secrecy
throughput (EST), which serve as critical metrics in evaluating the
robustness of communication systems against potential breaches.

Furthermore, the research proposes a novel two-stage gradient-based
iterative solution algorithm aimed at optimizing EST while adhering to
constraints like transmit power limits and acceptable detection error
probabilities. This optimization is crucial in maintaining covert
communications, where minimizing detectability by hostile entities is
paramount. The numerical validations presented confirm the efficacy of
this hybrid system in enhancing UAV communication security, showcasing
significant improvements in SOP and EST metrics.

Additionally, Saber et al. (2024) explore the integration of
high-altitude platform (HAP)-assisted FSO communications with
UAV-enabled RF links, focusing on physical-layer security mechanisms to
enhance control signaling resilience during emergencies \[Saber et al.,
2024\]. Their study employs a dual-hop integrated HAP-based FSO and
UAV-enabled RF downlink communication system using the
decode-and-forward relaying scheme. They derive analytical and
asymptotic closed-form expressions for SOP and the probability of
strictly positive secrecy capacity (PSPSC), considering factors such as
atmospheric turbulence, pointing errors, and RF fading \[Saber et al.,
2024\]. Their findings indicate that reducing pointing errors and
employing advanced detection techniques like heterodyne detection can
significantly enhance system security \[Saber et al., 2024\].

Building on these insights, Zhang et al. (2024) explore similar themes
within a space-air-ground integrated network (SAGIN), emphasizing the
role of UAV trajectory and power allocation in maximizing the average
secrecy rate under physical-layer security constraints. Their study
employs a two-phase transmission approach using hybrid FSO/RF links,
where UAV's trajectory and power allocation are optimized using block
coordinate descent and successive convex approximation techniques to
solve nonconvex optimization problems. They introduce two tailored
transmission schemes: a slot-based scheme for delay-sensitive data and a
period-based scheme for delay-insensitive data, both designed to enhance
secrecy rates significantly compared to benchmark schemes.

Lei et al. (2018) contribute further by analyzing a secure dual-hop
mixed RF-FSO downlink SWIPT system under conditions of Gamma-Gamma
fading for FSO links and Nakagami-m fading for RF links. Their findings
underscore how atmospheric turbulence, pointing errors, detection
technology, path loss, and energy harvesting intricately influence
secrecy performance \[Lei et al., 2018\]. Specifically, they demonstrate
that improvements in pointing accuracy and adoption of heterodyne
detection can substantially enhance secrecy performance by mitigating
adverse effects caused by these factors \[Lei et al., 2018\]. Moreover,
their study reveals that path loss and energy harvesting parameters play
significant roles in shaping the system's secrecy capacity, highlighting
essential trade-offs in practical system design \[Lei et al., 2018\].

Pattanayak et al. (2020) extend this discourse by examining a two-way
relay based mixed FSO/RF network under multiple eavesdropping threats
\[Pattanayak et al., 2020\]. They model RF links with Nakagami-m fading
distribution while characterizing FSO channels by Málaga distribution to
analyze physical layer security performance effectively. The study
highlights how different detection techniques such as intensity
modulation/direct detection (IM/DD) and heterodyne detection (HD), along
with pointing errors impact the system's security metrics like SOP and
secrecy throughput (ST), derived using Meijer<span dir="rtl">’</span>s
G-function \[Pattanayak et al., 2020\]. These insights emphasize the
critical need for robust security measures against sophisticated
eavesdropping scenarios.

Ibrahim et al. (2023) further enrich our understanding by focusing on
underlay spectrum-sharing hybrid RF/FSO systems under α-μ fading and
Málaga turbulence conditions \[Ibrahim et al., 2023\]. They address how
transmit power limitations at secondary users and permissible
interference at primary users affect secrecy performance while
incorporating link blockage and pointing errors into their models. Their
findings provide crucial insights into managing power constraints
effectively to optimize secrecy throughput under complex channel
conditions \[Ibrahim et al., 2023\].

Overall, these studies underscore the critical need for integrating
sophisticated technologies such as machine learning with hybrid RF/FSO
systems to ensure high levels of security in UAV communications within
challenging environments marked by high RF interference and dynamic
atmospheric conditions. Future research should explore more
sophisticated models for atmospheric turbulence and eavesdropping
scenarios, as well as further integration of machine learning techniques
for dynamic adaptation of UAV trajectories and power settings to enhance
system performance under varying environmental conditions and threat
levels.

❓ **Question 4: How does spatial diversity improve secrecy rate and
mitigate fading effects in dual-hop RF-FSO systems compared to
single-hop FSO?**

IMPROVED SUMMARY: Lei et al. (2017) provide a foundational analysis of
the secrecy performance in mixed RF-FSO systems, focusing on the effects
of Gamma-Gamma and Nakagami-m fading on FSO and RF links respectively.
Their study rigorously evaluates how atmospheric turbulence, pointing
errors, and detection technologies such as heterodyne detection and
intensity modulation with direct detection influence the secrecy outage
probability (SOP) and average secrecy capacity (ASC). Through analytical
derivations and Monte Carlo simulations, they demonstrate that
heterodyne detection generally offers superior secrecy performance over
intensity modulation with direct detection, especially under conditions
of high atmospheric turbulence and severe pointing errors.

Building upon this, Pattanayak et al. (2022) delve deeper into physical
layer security in hybrid RF-FSO systems where dual-hop communication
involves both RF and FSO links. This study introduces diversity
combining techniques at the destination node to enhance physical layer
security (PLS) in the presence of multiple eavesdroppers, considering
both collusion and non-collusion scenarios. The FSO and RF links are
modeled with independent Málaga (M) and Nakagami-m fading distributions,
incorporating boresight and non-zero boresight pointing errors along
with different optical demodulation schemes. Pattanayak et al. (2022)
derive closed-form expressions for SOP and effective secrecy throughput
(EST), emphasizing how receiver diversity techniques like selection
combining (SC) and maximal ratio combining (MRC) can significantly
mitigate fading effects and enhance system performance in urban
environments. Their findings also highlight the importance of
considering energy efficiency alongside security in designing modern
communication systems.

Further expanding on these concepts, Singh et al. (2022) investigate a
mixed FSO/RF SWIPT system employing decode-and-forward relaying where
the FSO link experiences Málaga distributed turbulence coupled with
pointing errors, while the RF link suffers from double shadowed Rician
fading. Their analysis reveals that higher levels of turbulence and
pointing errors can paradoxically enhance secrecy by impairing the
eavesdropper's received signal quality, thus affecting key system
performance metrics such as bit error rate, outage probability, and
ergodic capacity.

Additionally, Ahmed et al. (2023) introduce an innovative approach by
incorporating a reconfigurable intelligent surface (RIS) into dual-hop
RF-FSO systems to address physical layer security challenges under
diverse eavesdropping scenarios including RF eavesdropping, FSO
eavesdropping, and simultaneous attacks on both channels. The
integration of RIS technology allows dynamic adjustment of signal phases
to counteract Nakagami-m fading on the RF link and Málaga turbulence
with pointing errors on the FSO link. Their findings underscore that
RIS-assisted systems not only bolster average secrecy capacity but also
reduce secrecy outage probability and enhance effective secrecy
throughput significantly.

Collectively, these studies from Lei et al. (2017), Pattanayak et al.
(2022), Singh et al. (2022), and Ahmed et al. (2023) underscore a
multifaceted approach to enhancing physical layer security in mixed
RF-FSO systems through careful management of technological and
environmental variables alongside innovative adaptations using modern
computational techniques. Future research directions include
investigating more complex eavesdropping scenarios, integrating advanced
signal processing techniques, and exploring quantum key distribution
within hybrid RF-FSO systems to further enhance security measures.

❓ **Question 5: What comparative analyses exist between spatial
diversity schemes in secure pure-FSO links versus hybrid RF-FSO
configurations?**

IMPROVED SUMMARY: The comprehensive study by Pattanayak et al. (2020)
delves into the physical layer security (PLS) of hybrid RF-FSO
communication systems, focusing on scenarios involving multiple
eavesdroppers and diverse receiver configurations. This research models
a dual-hop communication system where the initial hop employs radio
frequency (RF) and the subsequent hop integrates both RF and Free-Space
Optical (FSO) links. The RF links are characterized using Rayleigh
distribution, while the FSO links are described by Málaga distribution,
allowing for an in-depth analysis of secrecy performance metrics such as
secrecy outage probability (SOP) and effective secrecy throughput (EST).
The impact of receiver diversity techniques, including selection
combining (SC) and maximal ratio combining (MRC), is thoroughly
examined.

Further expanding on hybrid systems, Ai et al. (2020) analyze a hybrid
FSO/RF system under a modified selection combining scheme that accounts
for both secrecy performance and diversity gain. Their study
incorporates the effects of atmospheric turbulence, FSO receiver
pointing errors, and RF power amplifier inefficiencies, providing a
realistic assessment of the system's performance under various
atmospheric and hardware impairments. They derive exact analytical
expressions for performance indicators such as average secrecy capacity
(ASC) and SOP, with asymptotic SOP analysis offering deeper insights
into system resilience under extreme conditions.

Building upon these insights, Althunibat et al. (2023) explore the
physical-layer security of dual-hop hybrid FSO-mmWave systems, where
both FSO and millimeter wave (mmWave) links are used simultaneously at
each hop. This study introduces a mathematical framework to derive
metrics like average secrecy capacity, secrecy outage probability, and
effective secrecy throughput. Monte Carlo simulations validate these
analytical results, demonstrating robust secrecy performance under
various operational conditions such as link distances and weather
scenarios. The research highlights that hybrid-type eavesdroppers pose
the most significant threat to system security, emphasizing the
effectiveness of integrating FSO and mmWave technologies to counteract
these threats.

Shakir et al. (2021) extend this analysis to a hybrid FSO/RF system
where the FSO link is characterized by Málaga-M distribution and the RF
link by Nakagami-m distribution. Their study introduces two
eavesdropping modes—colluding and non-colluding—and derives exact
closed-form expressions for various secrecy metrics including SOP, SOP∞,
SPSC, ASC, and ASC∞. They explore how channel parameters such as fading
severity, atmospheric turbulence, pointing error, number of
eavesdroppers, and eavesdropper link power impact the secrecy
performance. Their findings indicate that an increase in the number of
eavesdroppers significantly degrades the secrecy performance under both
eavesdropping modes.

Tokgoz et al. (2022) contribute significantly to understanding hybrid
FSO-mmWave systems from a physical-layer security perspective in
environments with exponential atmospheric turbulence for FSO links and
Weibull fading for mmWave links. Their work provides analytical
derivations for strictly positive secrecy capacity (SPSC), considering
different types of eavesdroppers: RF-, FSO-, and Hybrid-Eve. The study
demonstrates that Hybrid-Eve poses the greatest threat due to their
capability to exploit both link types simultaneously. This underscores
the necessity for advanced security measures tailored to these complex
hybrid environments.

Liang et al. (2021) further enrich this discourse by investigating how
hybrid FSO/RF systems perform under non-cooperative targets including
eavesdroppers and jammers using selection combining techniques at the
receiver without needing transmitter channel state information. Their
findings reveal that such systems exhibit superior performance in terms
of outage probability, average bit error rate, and secrecy outage
probability compared to standalone FSO systems even amidst RF
interference \[Liang et al., 2021\]. This study not only confirms the
robustness of hybrid systems against interference but also underscores
their potential in mitigating adverse effects caused by non-cooperative
entities.

Both studies underscore the enhanced security features of hybrid RF-FSO
systems over traditional mixed FSO/RF configurations, particularly in
urban environments susceptible to eavesdropping threats. They also
discuss practical challenges associated with implementing these advanced
communication technologies in dense urban settings, including issues
related to system deployment, maintenance, and operational efficiency in
areas with high structural density which may lead to increased signal
obstruction and interference (\[Pattanayak et al., 2020\]; \[Shakir et
al., 2021\]).

This integrated discussion not only enhances understanding of hybrid
RF-FSO systems' operational dynamics but also provides valuable insights
into their practical applications in real-world scenarios. The derived
expressions for secrecy metrics offer valuable tools for assessing and
enhancing the security of such systems under various operational
scenarios. Future research should explore adaptive security mechanisms
that dynamically adjust to varying channel conditions and eavesdropper
presence, as well as extending the analysis to include more complex
eavesdropping scenarios and other types of hybrid systems to further
enhance understanding of physical layer security in diverse
communication environments (\[Shakir et al., 2021\]).

## Supertopic 4: Advanced Modulation and Security Techniques

❓ **Question 1: How does chaotic modulation enhance physical layer
security in FSO channels affected by atmospheric turbulence?**

IMPROVED SUMMARY: The comprehensive study by Guo et al. (2024)
investigates the enhancement of security in Free-Space Optical (FSO)
communication systems through the application of Differential Chaotic
Shift Keying (DCSK). This method, which partitions the transmitted
signal into reference and data segments, significantly improves
resistance to physical layer attacks and maintains lower bit error
rates, especially under severe atmospheric turbulence modeled by the
gamma-gamma approach \[Guo et al., 2024\].

In parallel, Saber et al. (2017) explore the performance of secure FSO
communications over Málaga (M) turbulence channels, which include
effects from intensity modulation/direct detection (IM/DD) and pointing
errors. Their findings reveal that the Málaga model effectively captures
the complex dynamics of FSO channels under security constraints,
providing a robust framework for assessing security performance across
different turbulence conditions. The study derives closed-form
expressions for key security metrics such as average secrecy capacity,
secrecy outage probability, and strictly positive secrecy capacity,
confirming that these metrics improve with better pointing accuracy and
reduced turbulence intensity \[Saber et al., 2017\].

Ai et al. (2020) further enrich this discourse by analyzing physical
layer security over Málaga channels under various eavesdropping
scenarios. They demonstrate that proximity of the eavesdropper to the
transmitter has a less significant impact on secrecy performance
compared to other positions. Additionally, they uncover that channel
correlation can either enhance or deteriorate secrecy performance
depending on its level, exhibiting a non-monotonic relationship with
performance metrics. Notably, Ai et al. find that the asymptotic slope
of the secrecy outage probability is consistently 0.5 across different
scenarios \[Ai et al., 2020\].

Narang et al. (2019) contribute to this discussion by examining DCSK in
FSO systems under Gamma-Gamma turbulence conditions. Their research
highlights how increasing the spreading factor enhances the average
signal-to-noise ratio (SNR), yet also raises the probability of error
under consistent link lengths and turbulence intensities. This finding
underscores a critical trade-off between achieving high SNR and
maintaining system security in DCSK-based FSO systems \[Narang et al.,
2019\].

Verma et al. (2024) extend these insights by employing differential
chaos shift keying (DCSK) for FSO communication systems to improve their
performance under atmospheric turbulence and non-zero boresight pointing
errors using generalized Malaga and modified Rayleigh distributions for
modeling channel gain and jitter effects respectively \[Verma et al.,
2024\]. Their study demonstrates improved average bit error rate (ABER)
performance compared to other modulation schemes like CDSK, BPSK, and
CDMA under varying conditions of atmospheric turbulence and boresight
pointing errors. Moreover, they derive expressions for ergodic capacity
and average secrecy capacity which show significant improvements over
traditional modulation techniques \[Verma et al., 2024\].

Wu et al. (2024) introduce an innovative approach in OFDM-FSO
communications by integrating digital chaos encryption with
probabilistic shaping to enhance both security and efficiency \[Wu et
al., 2024\]. By encrypting permutation information using a pseudo-random
binary sequence generated by a 1-dimensional chaotic map amplifier and
incorporating it into the synchronization head, they achieve notable
improvements in transmission distance by 3.8–10% and an increase in
received optical power by about 0.8–1 dB compared to traditional models
without encryption \[Wu et al., 2024\]. This method not only secures
sensitive data but also optimizes bandwidth usage without adversely
affecting bit error rate performance.

Comparing DCSK with traditional cryptographic methods like Triple DES
and AES, DCSK shows superior performance in maintaining data integrity
and confidentiality in optically turbulent environments \[Guo et al.,
2024\]. This suggests a potential for DCSK to replace or augment
existing encryption methods within optical wireless networks.

Looking forward, both studies propose future research directions aimed
at enhancing FSO system security. Guo et al. (2024) suggest optimizing
DCSK performance across a broader spectrum of atmospheric conditions and
exploring synergies between DCSK and other cryptographic strategies
\[Guo et al., 2024\]. Similarly, Saber et al. (2017) recommend
integrating advanced modulation techniques and adaptive optics to
further enhance security and reliability under diverse atmospheric
conditions \[Saber et al., 2017\].

These investigations collectively underscore the importance of
considering various atmospheric models and pointing errors in designing
secure FSO systems. They also highlight the potential of innovative
cryptographic techniques like DCSK in improving the robustness of FSO
communications against evolving security threats.

❓ **Question 2: What is orbital angular momentum (OAM), how is it
generated in FSO transmitters, and how can it be exploited for secure
communication?**

IMPROVED SUMMARY: In their comprehensive analysis, Ai et al. (2020)
delve into the physical layer security dynamics of free-space optical
(FSO) communications over Málaga channels, effectively encapsulating the
complexities introduced by atmospheric turbulence. The study employs
intensity modulation/direct detection (IM/DD) methodologies to
scrutinize how different eavesdropping scenarios affect secrecy metrics
such as average secrecy capacity (ASC) and secrecy outage probability
(SOP). Theoretical models developed in this research consider varying
degrees of correlation between communication channels and their
interaction with atmospheric conditions. It is demonstrated that while
proximity to the transmitter diminishes its influence on secrecy
performance, channel correlation has a nuanced impact—being beneficial
or detrimental depending on its magnitude \[Ai et al., 2020\].

Further enriching this discourse, Saber et al. (2017) provide a detailed
examination of secure FSO communications over Málaga turbulence
channels, which are modeled by the general M distribution. This model
captures both log-normal and Generalized-K distributions, offering a
robust framework for analyzing FSO security under diverse atmospheric
disturbances. Their findings underscore the importance of considering
pointing errors and optimizing channel conditions to enhance security.
By deriving closed-form expressions for key security metrics such as
ASC, SOP, and strictly positive secrecy capacity, they confirm that
improved pointing accuracy and reduced turbulence intensity
significantly bolster FSO link security \[Saber et al., 2017\].

Building upon these foundational insights, Shaw et al. (2018) propose an
innovative approach by integrating chaotic systems with quantum key
distribution (QKD) to enhance the security and synchronization in FSO
communications. Utilizing a Lorenz chaotic system for data transmission
over a classical channel, they combine this with QKD to secure the
exchange of chaotic system parameters over a quantum channel. Their
experimental work includes successful transmission of images as binary
data across an FSO channel using techniques like
Low-density-parity-check (LDPC) and Quadrature-Phase-Shift-Keying (QPSK)
for noise minimization and error correction \[Shaw et al., 2018\].

The integration of chaotic communications with QKD not only provides
robust security against potential eavesdropping and interception but
also makes the system resilient against quantum computing threats. This
dual-layer security mechanism is particularly suitable for deep-space
communications, offering a robust solution against eavesdropping and
interception while ensuring end-to-end encrypted links in space missions
conducted by agencies like NASA and ESA \[Shaw et al., 2018\].

The inherent unpredictability and broadband noise-like signals of
chaotic systems, along with the unconditional security of QKD,
significantly enhance the security against eavesdropping and other
security threats. The results also suggest robustness against noise and
potential applicability in long-range space missions \[Shaw et al.,
2018\]. Future research will focus on further optimizing this
integration, exploring hardware implementations, testing the system in
space relay scenarios, extending the range, and improving error rates
under different atmospheric conditions.

Expanding on these studies, Liu et al. (2024) explore the physical-layer
security performance for a reconfigurable intelligent surface
(RIS)-assisted hybrid FSO-RF system employing non-orthogonal multiple
access (NOMA). They analyze various user scenarios where signals are
transmitted through direct paths or reflected paths via RIS or both
combined under different eavesdropping conditions. The study reveals
that RIS can significantly manipulate signal paths to enhance system
security by providing robustness against eavesdropping when both direct
and RIS-reflected paths are utilized \[Liu et al., 2024\]. This research
highlights how strategic placement of RIS elements and optimization of
transmission power can maximize physical-layer security in hybrid
communication systems.

Adding to this body of knowledge, Narang et al. (2024) investigate
dual-hop mixed FSO RF systems employing differential chaos shift keying
(DCSK), which enhances both performance and confidentiality in
challenging atmospheric conditions such as Gamma-Gamma turbulence and
Nakagami-m fading scenarios. Their study demonstrates that while FSO-RF
configurations offer better bit error rate performance due to advanced
relaying protocols like decode-and-forward (DF), all-optical
configurations such as FSO-FSO provide superior outcomes in terms of
secrecy outage probability (SOP), making them preferable for
high-security applications \[Narang et al., 2024\]. This underscores the
trade-offs between performance metrics like BER and secrecy measures
such as SOP in choosing optimal system configurations under varying
environmental conditions.

This body of work not only advances our understanding of physical layer
security in FSO communications but also sets a foundational framework
for future explorations aimed at mitigating risks associated with
eavesdropping under varying atmospheric disturbances \[Ai et al., 2020;
Shaw et al., 2018; Saber et al., 2017; Liu et al., 2024; Narang et al.,
2024\].

❓ **Question 3: What are the major technical challenges of implementing
OAM-based secure FSO links under moderate and strong turbulence
conditions?**

IMPROVED SUMMARY: The research conducted by Saber et al. (2017) and Ai
et al. (2020) provides a comprehensive analysis of physical layer
security in Free-Space Optical (FSO) communications, particularly
focusing on the challenges posed by Málaga turbulence channels and
various eavesdropping scenarios. Saber et al. (2017) delve into the
derivation of closed-form expressions for key security metrics such as
average secrecy capacity, secrecy outage probability, and strictly
positive secrecy capacity under the influence of intensity
modulation/direct detection (IM/DD) systems and pointing errors. These
metrics are crucial for assessing the impact of average SNR, pointing
accuracy, and turbulence intensity on the security performance of FSO
links.

Ai et al. (2020) extend this analysis by examining the physical layer
security over Málaga channels under different eavesdropping conditions.
Their study highlights how the placement of eavesdroppers relative to
the transmitter and receiver affects secrecy performance, with proximity
to the transmitter showing a lesser impact on security due to
atmospheric conditions. They introduce novel theoretical models that
incorporate channel correlation effects, revealing a non-monotonic
relationship between correlation levels and secrecy performance metrics.
This study also establishes that the asymptotic slope of secrecy outage
probability remains consistent at 0.5 across various scenarios,
emphasizing the complex interplay between eavesdropper positioning,
channel correlation, and atmospheric conditions.

Building upon these insights, Ahmed et al. (2023) explore the
integration of Reconfigurable Intelligent Surfaces (RIS) in dual-hop
RF-FSO systems to enhance physical layer security against diverse
eavesdropping scenarios including RF eavesdropping, FSO eavesdropping,
and simultaneous RF and FSO eavesdropping. The study employs a system
model with Nakagami-m fading for the RF link and Málaga turbulence with
pointing error for the FSO link. Ahmed et al. develop closed-form
expressions for various secrecy metrics such as average secrecy
capacity, secrecy outage probability, and effective secrecy throughput
\[Ahmed et al., 2023\]. Their results demonstrate that RIS technology
significantly enhances physical layer security by dynamically adjusting
signal phases to counteract eavesdropping attempts effectively.

Liu et al. (2021) further contribute to understanding these systems by
analyzing RIS-assisted mixed dual-hop FSO-RF communication systems under
exponentiated Weibull channels. They find that atmospheric turbulence
parameters, channel distance of FSO, intensity of atmospheric
turbulence, and number of reflectors all critically affect system
performance \[Liu et al., 2021\]. Specifically, increased atmospheric
turbulence and longer channel distances degrade system performance while
a higher number of reflectors improves it.

Sun et al. (2024) extend this discussion by proposing a hybrid RF/FSO
system utilizing RIS reflection to interfere with eavesdroppers in
dual-link scenarios where both RF and FSO links are susceptible to
eavesdropping. This study analyzes how interference signal-to-noise
ratio, time switching factor, energy conversion efficiency of jammers,
number of RIS reflective elements, weather conditions, and detection
methods influence physical layer security \[Sun et al., 2024\]. Their
findings underscore that optimizing these parameters can substantially
mitigate eavesdropping risks while enhancing overall system resilience.

Both Saber et al. (2017), Ai et al. (2020), along with Ahmed et al.
(2023), utilize Monte Carlo simulations to validate their theoretical
findings, suggesting a need for experimental validation to confirm these
models' applicability in real-world scenarios. This approach not only
enhances our understanding but also sets a foundation for future
advancements in FSO communication security.

Future research directions proposed include exploring the impact of
dynamic atmospheric conditions on correlation and secrecy performance,
developing adaptive security mechanisms that adjust based on real-time
environmental and system parameters, integrating advanced cryptographic
techniques with physical layer security measures \[Saber et al., 2017;
Ai et al., 2020\], investigating more complex eavesdropping scenarios,
integrating advanced signal processing techniques, and exploring the use
of quantum key distribution in RIS-aided RF-FSO systems to further
enhance security \[Ahmed et al., 2023\]. These comprehensive studies
collectively advance our knowledge in securing FSO systems against
diverse atmospheric disturbances and strategic eavesdropping attempts.

❓ **Question 4: Which optical devices (e.g., spatial light modulators,
q-plates, metasurfaces) are used for encoding and decoding OAM modes in
secure FSO communication?**

IMPROVED SUMMARY: In their pivotal research, Ai et al. (2020) delve into
the complexities of physical layer security in free-space optical (FSO)
communications, particularly focusing on systems operating over Málaga
channels. These channels are crucial for understanding the effects of
atmospheric turbulence on optical wave propagation in FSO systems. The
study assesses how different eavesdropping scenarios—particularly
varying distances between eavesdroppers and primary communicators—affect
key security metrics such as average secrecy capacity (ASC) and secrecy
outage probability (SOP). One significant finding is that closer
proximity of an eavesdropper to the transmitter does not necessarily
correlate with greater risk, which suggests that other factors like
atmospheric conditions and channel correlation play substantial roles in
influencing FSO communication security.

Moreover, Ai et al. (2020) explore how channel correlation impacts
secrecy performance in a non-linear manner; both enhancement and
deterioration of security are possible depending on the level of
correlation. This introduces a complex dynamic where managing channel
correlation could be leveraged as a strategic tool in enhancing FSO
communication security. Additionally, their research consistently shows
an asymptotic SOP slope of 0.5 across various scenarios, indicating a
stable element in the behavior of these systems under different
eavesdropping conditions.

Building upon this foundation, Liu et al. (2024) extend the discussion
to hybrid FSO-RF systems assisted by reconfigurable intelligent surfaces
(RIS) with non-orthogonal multiple access (NOMA). Their study highlights
how RIS can manipulate signal paths to enhance system security
significantly, especially when both direct and RIS-reflected paths are
available \[Liu et al., 2024\]. They demonstrate that the integration of
RIS not only diversifies transmission routes but also robustly defends
against eavesdropping under various atmospheric conditions and pointing
errors. This research underscores the importance of strategic RIS
placement and power optimization to maximize security.

Furthermore, Shaw et al. (2018) introduce an innovative approach by
integrating chaotic communications with Quantum Key Distribution (QKD)
to enhance FSO communication security. They utilize a Lorenz chaotic
system for data transmission over a classical channel while securing the
exchange of chaotic system parameters over a quantum channel. Their
experiments demonstrate that this integration can securely transmit data
with high accuracy, even in noisy environments, maintaining a low
bit-error-rate (BER) across varying signal-to-noise ratios (SNR). The
inherent unpredictability and broadband noise-like signals of chaotic
systems, combined with the unconditional security provided by QKD,
significantly enhance protection against eavesdropping and other
security threats.

Expanding on these concepts, Mahmud et al. (2021) propose a novel FSO
communication system that combines chaotic communications with QKD to
achieve greater security and range compared to existing techniques such
as N-slit interferometers \[Mahmud et al., 2021\]. Utilizing inherently
auto-synchronizable Lorenz chaotic models for data transmission and
securing critical synchronization parameters via a quantum channel using
QKD and public-key cryptography protocols, this system demonstrates
robustness against quantum computing threats and dynamic environmental
conditions. Their experimental work includes successful real-time
transmission of high-resolution single-spectral and multi-spectral
images over classical channels with dynamic reconfiguration of chaotic
systems to test security robustness \[Mahmud et al., 2021\]. The
integration provides a dual-layer security mechanism enhancing FSO
communications' defense against potential eavesdropping and
interception.

Ahmed et al. (2023) further enrich our understanding by investigating
physical layer security issues in dual-hop RIS-aided RF-FSO systems
under various eavesdropping scenarios including RF eavesdropping, FSO
eavesdropping, and simultaneous RF-FSO eavesdropping \[Ahmed et al.,
2023\]. Their findings emphasize the effectiveness of RIS technology in
dynamically adjusting signal phases to enhance confidentiality against
unauthorized access or disclosure under challenging conditions such as
Nakagami-m fading for RF links and Málaga turbulence with pointing
errors for FSO links. The study's development of closed-form expressions
for secrecy metrics like average secrecy capacity and effective secrecy
throughput provides valuable insights into optimizing secure wireless
communication systems \[Ahmed et al., 2023\].

Narang et al. (2024) contribute significantly to this field by
evaluating dual-hop mixed FSO RF systems employing differential chaos
shift keying (DCSK), which enhances both performance and confidentiality
\[Narang et al., 2024\]. They investigate three dual-hop communication
systems: FSO-FSO, RF-FSO, and FSO-RF, all using decode-and-forward
relaying protocols where DCSK is employed to boost system
confidentiality effectively. The study highlights that while FSO-RF
configurations offer better BER performance due to less susceptibility
to Gamma-Gamma turbulence and pointing errors affecting the FSO link
modeled with Nakagami-m fading; all-optical configurations like FSO-FSO
provide superior outcomes in terms of secrecy as measured by SOP
\[Narang et al., 2024\]. This underscores the trade-offs between system
performance and secrecy in choosing the optimal configuration based on
specific requirements for performance and prevailing atmospheric
conditions.

These insights not only broaden our understanding of physical layer
security dynamics in FSO systems but also highlight critical areas for
future investigation and development aimed at enhancing robustness
against eavesdropping and other forms of cyber threats in optical
wireless networks. The integration of chaotic communications and QKD
proposed by Shaw et al. (2018) not only improves security over
traditional methods but also extends the operational range, making it
suitable for space missions. This suggests robustness against noise and
potential applicability in long-range space missions, marking a
significant advancement in secure FSO communications technology.

❓ **Question 5: What is the working principle of reconfigurable
intelligent surfaces (RIS) in optical and hybrid RF-FSO secure
communication systems?**

IMPROVED SUMMARY: The comprehensive study conducted by Ahmed et al.
(2023) delves into the enhancement of physical layer security within a
dual-hop RIS-aided RF-FSO communication system under various
eavesdropping scenarios including RF eavesdropping, FSO eavesdropping,
and simultaneous attacks on both channels. The research meticulously
develops closed-form expressions for key secrecy metrics such as average
secrecy capacity, secrecy outage probability, and effective secrecy
throughput, which are rigorously validated through Monte Carlo
simulations. These simulations demonstrate the significant role that RIS
technology plays in bolstering the security of wireless communications
against diverse eavesdropping scenarios.

Particularly noteworthy is the study's focus on the impact of pointing
errors in the FSO link, which are critical due to their potential to
degrade signal integrity and thus compromise security. The role of RIS
in dynamically adjusting signal phases is also emphasized as a crucial
mechanism for enhancing signal resilience against interception and
unauthorized access. Furthermore, the influence of atmospheric
conditions, especially turbulence which affects both RF and FSO links,
is analyzed to determine their effect on the overall system's ability to
maintain secure communications under adverse environmental conditions.

Building upon these insights, Wang et al. (2023) further explore the
physical layer security in mixed RF/FSO systems facilitated by RIS
technology. Their study introduces a novel approach using a
wireless-powered jammer whose signals are reflected by an RIS to disrupt
eavesdropping activities effectively. This method not only leverages the
inherent advantages of RIS in phase adjustments but also introduces
additional layers of security through strategic jamming reflections
aimed at potential eavesdroppers.

Liu et al. (2021) extend this analysis by examining a RIS-assisted
hybrid FSO-RF system with NOMA, focusing on different user scenarios
where direct and reflected paths from RIS are considered separately or
in combination. They provide analytical and asymptotic expressions for
secrecy outage probability under varying conditions of eavesdropping
exposure and channel characteristics such as Gamma-Gamma distribution
for FSO links and Nakagami-m fading for RF channels. Their findings
underscore that the presence of both direct and RIS-reflected paths
significantly enhances system security, particularly when strategic
placement of RIS elements and optimization of transmission power are
employed.

Sun et al. (2024) contribute significantly to this body of knowledge by
proposing a hybrid RF/FSO system utilizing RIS reflection to
specifically interfere with eavesdroppers under dual eavesdropping
scenarios. Their model incorporates Nakagama-m distribution for RF links
and Málaga distribution for FSO links, with detailed analysis on how
various system parameters like interference signal-to-noise ratio, time
switching factor, energy conversion efficiency, number of RIS reflective
elements, and environmental conditions such as weather impact physical
layer security performance.

Narang et al. (2024) enhance our understanding by evaluating dual-hop
mixed FSO-RF systems employing differential chaos shift keying (DCSK) to
optimize performance and secrecy under various atmospheric conditions
and fading models. They highlight that while FSO-RF configurations offer
better BER performance due to Nakagami-m fading handling in RF links and
Gamma-Gamma turbulence in FSO links, all-optical (FSO-FSO)
configurations provide superior secrecy outcomes measured by secrecy
outage probability (SOP). This study underscores the trade-offs between
system performance and secrecy across different configurations \[Narang
et al., 2024\].

Both studies underscore the critical role of system parameters such as
fading severity, link distances, atmospheric turbulence in maximizing
the effectiveness of RIS-aided jamming. Comparisons with RIS-free
systems confirm substantial improvements in security metrics due to RIS
integration. These findings collectively demonstrate that optimizing
RIS-related parameters can substantially improve a system's security
performance against sophisticated eavesdropping techniques.

Future research directions suggested include exploring optimization
strategies for RIS configurations under various environmental conditions
and potential integration of advanced machine learning techniques for
dynamic configuration adjustments to further enhance system security.
This body of work highlights how environmental factors and technological
innovations like RIS can significantly impact the performance of secure
communication systems \[Ahmed et al., 2023; Wang et al., 2023; Liu et
al., 2021; Sun et al., 2024; Narang et al., 2024\].

❓ **Question 6: How can RIS-based designs enhance secrecy capacity by
dynamically reflecting FSO beams toward legitimate users while
suppressing leakage?**

IMPROVED SUMMARY: The research conducted by Ahmed et al. (2023) and Wang
et al. (2023) provides a comprehensive analysis of physical layer
security enhancements in dual-hop RIS-aided RF-FSO communication
systems, focusing on the dynamic reflection of FSO beams and suppression
of leakage to unauthorized entities. Ahmed et al. (2023) explore various
eavesdropping scenarios including RF eavesdropping, FSO eavesdropping,
and simultaneous RF and FSO eavesdropping, employing a model with
Nakagami-m fading for the RF link and Málaga turbulence with pointing
errors for the FSO link. These atmospheric conditions and alignment
challenges critically influence FSO link performance, impacting both
signal integrity and security.

Wang et al. (2023) extend this analysis by incorporating a
wireless-powered jammer that disrupts eavesdropping activities through
signals reflected by an RIS. This study not only corroborates the
findings of Ahmed et al. regarding the efficacy of RIS in enhancing
secrecy metrics but also delves into the optimization of system
parameters such as the number of RIS reflecting elements, energy
conversion efficiency, and time switching factor. These factors are
shown to significantly reduce secrecy outage probability and enhance
average secrecy capacity, confirming the pivotal role of RIS in
mitigating eavesdropping risks.

Building on these insights, Liu et al. (2021) further investigate the
physical-layer security performance for a RIS-assisted hybrid FSO-RF
system under varying atmospheric conditions modeled by exponentiated
Weibull channels \[Liu et al., 2021\]. Their study highlights how
atmospheric turbulence, channel distance, and the number of reflectors
critically affect system performance, particularly impacting outage
probability and bit error rate (BER). The integration of RIS technology
effectively enhances system resilience against atmospheric challenges
and improves BER, underscoring the importance of optimizing system
parameters such as the number of reflectors and channel configurations
to mitigate effects of atmospheric turbulence and path loss.

Sun et al. (2024) contribute to this body of knowledge by proposing a
hybrid RF/FSO system that utilizes RIS-based reflections to specifically
interfere with eavesdroppers under dual eavesdropping scenarios on both
RF and FSO links. Their work emphasizes the critical role of system
parameters such as interference signal-to-noise ratio, time switching
factor, and energy conversion efficiency in enhancing physical layer
security \[Sun et al., 2024\]. By deriving Strict Positive Secrecy
Capacity (SPSC) and Secure Outage Probability (SOP), they provide a
robust analytical framework verified through Monte Carlo simulations,
which underscores how environmental conditions like weather can
significantly influence security outcomes.

Narang et al. (2024) expand upon these findings by investigating three
dual-hop communication systems: FSO-FSO, RF-FSO, and FSO-RF using
decode-and-forward relaying with differential chaos shift keying (DCSK)
to enhance confidentiality \[Narang et al., 2024\]. Their study reveals
that while FSO-RF configurations offer better BER performance due to
differential chaos shift keying integration, all-optical (FSO-FSO)
configurations provide superior secrecy outcomes measured by SOP. This
underscores the trade-offs between system performance and secrecy across
different configurations under varying atmospheric conditions including
Gamma-Gamma turbulence.

Overall, these studies collectively advance our understanding of how
RIS-based designs can optimize physical layer security in mixed RF-FSO
systems under diverse environmental conditions and eavesdropping
scenarios. Future research directions suggested include exploring
advanced machine learning techniques for dynamic RIS configuration to
adaptively respond to evolving security threats \[Wang et al., 2023; Liu
et al., 2021; Sun et al., 2024; Narang et al., 2024\].

❓ **Question 7: What phase-shift design algorithms in RIS maximize
secrecy rate and minimize signal leakage to eavesdroppers in FSO
links?**

IMPROVED SUMMARY: In their detailed investigation, Ahmed et al. (2023)
explore the enhancement of physical layer security in a dual-hop
RIS-aided RF-FSO communication system, addressing various eavesdropping
scenarios including RF eavesdropping, FSO eavesdropping, and
simultaneous RF and FSO eavesdropping. Employing a model characterized
by Nakagami-m fading for the RF link and Málaga turbulence with pointing
errors for the FSO link, they develop robust closed-form expressions for
key secrecy metrics such as average secrecy capacity, secrecy outage
probability, and effective secrecy throughput. These metrics are
rigorously validated through Monte Carlo simulations to ensure accuracy
(\[Ahmed et al., 2023\]).

The study underscores the significant role of Reconfigurable Intelligent
Surfaces (RIS) in bolstering physical layer security by dynamically
adjusting signal phases to counteract eavesdropping threats.
Additionally, the research by Wang et al. (2023) complements these
findings by demonstrating how RIS-aided jamming in mixed RF/FSO systems
can disrupt eavesdropping activities through a two-hop
decode-and-forward relaying method. This method effectively utilizes a
wireless-powered jammer whose signals are reflected by the RIS to
enhance security measures (\[Wang et al., 2023\]).

Both studies highlight the critical influence of system parameters on
security performance. Ahmed et al. (2023) analyze the impact of fading
severity and atmospheric conditions, while Wang et al. (2023) extend
this analysis to include the effects of time switching factor, energy
conversion efficiency, and average interference noise ratio on the
system's secrecy outage probability. Furthermore, Wang et al. (2023)
investigate how varying the number of RIS reflecting elements and
optimizing link distances before and after reflection can substantially
improve the system's resistance to eavesdropping (\[Wang et al.,
2023\]).

A novel aspect addressed by Ahmed et al. (2023) is the impact of
pointing errors on FSO link security, which can severely degrade optical
link quality and affect secrecy performance metrics. To counteract these
effects, adaptive algorithms for phase-shift design are proposed as a
means to dynamically optimize RIS configurations based on real-time
environmental feedback and system states (\[Ahmed et al., 2023\]). These
adaptive algorithms play a crucial role in maintaining high levels of
security by minimizing signal leakage to potential eavesdroppers and
maximizing the secrecy rate under varying operational conditions.

Liu et al. (2024) further expand on these findings by analyzing a
RIS-assisted hybrid FSO-RF system with NOMA under various user scenarios
and eavesdropping conditions. Their study reveals that the integration
of RIS significantly enhances system security by manipulating signal
paths effectively. Particularly noteworthy is their finding that the
presence of both direct and RIS-reflected paths offers optimal security
performance against sophisticated eavesdroppers (\[Liu et al., 2024\]).
The research also discusses how strategic placement of RIS elements and
optimization of transmission power and beam directions are crucial for
maximizing security.

Sun et al. (2024) introduce an innovative approach in their study on
hybrid RF/FSO systems where they utilize RIS-based interference
specifically designed to thwart eavesdroppers in dual-link scenarios
involving both RF and FSO transmissions. By modeling both links with
distinct statistical distributions—Nakagami-m for RF and Málaga for
FSO—they derive new metrics such as Strict Positive Secrecy Capacity
(SPSC) and Secure Outage Probability (SOP), verified via Monte Carlo
simulations (\[Sun et al., 2024\]). Their findings emphasize that
enhancing interference signal-to-noise ratio, increasing RIS reflective
elements count, improving detection methods, optimizing weather
conditions, and boosting energy conversion efficiencies are pivotal in
elevating physical layer security.

Narang et al. (2024) contribute significantly to this discourse by
evaluating dual-hop mixed FSO RF systems employing differential chaos
shift keying (DCSK). Their analysis highlights how DCSK enhances
confidentiality in systems experiencing Gamma-Gamma turbulence along
with pointing errors in FSO links while facing Nakagami-m fading in RF
links. Notably, their results show that all-optical (FSO-FSO-DCSK)
configurations provide superior secrecy outcomes compared to mixed
configurations (\[Narang et al., 2024\]). This underscores the
importance of choosing appropriate system configurations based on
specific performance and secrecy requirements under varying atmospheric
conditions.

Overall, these comprehensive analyses from Ahmed et al. (2023), Wang et
al. (2023), Liu et al. (2024), Sun et al. (2024), and Narang et al.
(2024) significantly contribute to understanding how advanced
technologies like RIS can be leveraged to enhance wireless system
security across multiple fronts, suggesting further exploration into
optimizing RIS configurations under various environmental conditions and
potential integration of advanced machine learning techniques for
dynamic RIS configuration (\[Wang et al., 2023\]; \[Liu et al., 2024\];
\[Sun et al., 2024\]; \[Narang et al., 2024\]).

❓ **Question 8: Can RIS architectures be employed to dynamically
control secure transmission paths in ground-to-satellite FSO
communication scenarios?**

IMPROVED SUMMARY: \[Ahmed et al., 2023\] delves into the enhancement of
physical layer security within a dual-hop RIS-aided RF-FSO system under
various eavesdropping scenarios such as RF eavesdropping, FSO
eavesdropping, and simultaneous RF and FSO eavesdropping. The study
utilizes Nakagami-m fading for the RF link and Málaga turbulence with
pointing error for the FSO link. It meticulously develops closed-form
expressions for critical secrecy metrics including average secrecy
capacity, secrecy outage probability, and effective secrecy throughput.
These metrics are validated through rigorous Monte Carlo simulations
which confirm that RIS technology substantially improves the physical
layer security in dual-hop RF-FSO systems. The research underscores the
significant impact of system parameters like fading severity,
atmospheric conditions, and detection techniques on the overall secrecy
performance.

Further expanding on this theme, \[Liu et al., 2024\] investigates the
physical-layer security performance in a RIS-assisted hybrid FSO-RF
system employing non-orthogonal multiple access (NOMA). This study
introduces a dual-hop communication model where a source transmits an
optical NOMA signal to a relay, which then forwards it to two users in
scenarios involving direct and RIS-reflected paths. The analysis
includes scenarios where an eavesdropper might intercept transmissions
during different phases of communication. By modeling the FSO link with
a Gamma-Gamma distribution and RF channels with Nakagami-m fading, \[Liu
et al., 2024\] derive analytical and asymptotic expressions for secrecy
outage probability under various user scenarios and eavesdropping
conditions. Their results demonstrate that the integration of RIS
significantly enhances security by manipulating signal paths,
particularly when both direct and reflected paths are utilized.

Building upon these findings, \[Sun et al., 2024\] explores the
optimization of physical layer security in a hybrid RF/FSO system under
dual eavesdropping scenarios on both RF and FSO links. The study employs
RIS-based interference to disrupt eavesdroppers effectively, analyzing
how various system parameters such as interference signal-to-noise
ratio, time switching factor, energy conversion efficiency, number of
RIS reflective elements, and environmental conditions influence security
outcomes. Notably, \[Sun et al., 2024\] demonstrates that enhancements
in these parameters can significantly improve Strict Positive Secrecy
Capacity (SPSC) and Secure Outage Probability (SOP), verified through
Monte Carlo simulations.

\[Wang et al., 2023\] contributes to this body of knowledge by focusing
on the physical layer security of mixed RF/FSO systems enhanced by
RIS-aided jamming to counteract active eavesdropping. This study
highlights how a wireless-powered jammer utilizing signals reflected by
an RIS can thwart eavesdroppers in systems experiencing Nakagami-m
fading and Málaga turbulence. Theoretical expressions for SOP and ASC
were derived and validated using Monte Carlo simulations, demonstrating
substantial improvements in security metrics through the strategic
manipulation of RIS elements like reflecting element count and link
distances.

\[Narang et al., 2024\] further enriches this discourse by evaluating
dual-hop mixed FSO RF systems using differential chaos shift keying
(DCSK) to enhance confidentiality. Their study investigates three
configurations: FSO-FSO, RF-FSO, and FSO-RF with decode-and-forward
relaying affected by Gamma-Gamma turbulence and pointing errors on the
FSO link, alongside Nakagami-m fading on the RF link. They find that
while FSO-RF configurations offer better BER performance due to their
robustness against atmospheric impairments, all-optical (FSO-FSO)
configurations provide superior secrecy outcomes measured by SOP. This
highlights the trade-offs between performance and secrecy in choosing
system configurations based on specific requirements under varying
atmospheric conditions.

Both \[Ahmed et al., 2023\] and \[Liu et al., 2024\] highlight the
critical role of RIS in enhancing communication security and reliability
under challenging conditions. While \[Ahmed et al., 2023\] emphasizes
dynamic phase adjustment capabilities of RIS to secure transmission
paths against eavesdroppers in ground-to-satellite communications, \[Liu
et al., 2024\] underscores the necessity to optimize system parameters
such as reflector numbers and channel configurations to mitigate
atmospheric turbulence effects.

These insights collectively advance our understanding of how RIS
technology can be strategically employed to bolster the robustness and
security of next-generation wireless communication systems across
diverse environmental challenges and sophisticated eavesdropping
scenarios. Future research should focus on optimizing the design and
deployment of RIS elements to maximize system performance across a
broader range of atmospheric conditions and exploring advanced
modulation techniques like DCSK along with machine learning algorithms
for dynamic adaptation to varying environmental factors.

❓ **Question 9: What experimental RIS prototypes or testbeds have been
developed for validating secure optical wireless communication?**

IMPROVED SUMMARY: The research conducted by \[Ahmed et al., 2023\]
delves into the enhancement of physical layer security within a dual-hop
RIS-aided RF-FSO communication framework. This study meticulously
examines how reconfigurable intelligent surfaces (RIS) can fortify
security against diverse eavesdropping threats—RF eavesdropping, FSO
eavesdropping, and simultaneous RF and FSO eavesdropping—by dynamically
adjusting signal phases to protect transmitted information. Utilizing
Nakagami-m fading models for RF links and Málaga turbulence models with
pointing errors for FSO links, the authors develop robust closed-form
expressions for critical secrecy metrics including average secrecy
capacity, secrecy outage probability, and effective secrecy throughput.
These metrics are substantiated through comprehensive Monte Carlo
simulations that underscore the significant enhancement in physical
layer security facilitated by RIS technology.

Further expanding on this topic, \[Liu et al., 2021\] investigates a
similar RIS-assisted hybrid FSO-RF system employing non-orthogonal
multiple access (NOMA). This study focuses on the secrecy performance
under various transmission scenarios and eavesdropping conditions. It
introduces a dual-hop communication model where the source transmits an
optical NOMA signal to a relay, which then forwards it to two users in
the presence of an eavesdropper. The scenarios considered include
different combinations of direct and RIS-reflected paths, enhancing
understanding of how these elements interact under Gamma-Gamma
distributed FSO links and Nakagami-m faded RF channels. The results from
Monte-Carlo simulations confirm that the integration of RIS
significantly enhances security by manipulating signal paths,
particularly when both direct and reflected paths are utilized.

Building upon these insights, \[Wang et al., 2023\] explores the
physical layer security in a mixed RF/FSO system enhanced by RIS-aided
jamming to thwart eavesdroppers. This study employs a two-hop
decode-and-forward relaying method with Nakagami-m fading for RF links
and Málaga turbulence for FSO links. A novel approach involves a
wireless-powered jammer whose signals are reflected by an RIS to disrupt
eavesdropping activities effectively. Theoretical expressions for
secrecy outage probability (SOP) and average secrecy capacity (ASC) were
derived and validated using Monte Carlo simulations. The integration of
RIS not only reduced the SOP but also enhanced the ASC significantly.
Key parameters such as time switching factor, energy conversion
efficiency, average interference noise ratio, number of RIS reflecting
elements, and link distances were varied to analyze their effects on
system security.

Additionally, \[Sun et al., 2024\] provides an in-depth analysis of a
hybrid RF/FSO system utilizing RIS-based interference to mitigate dual
eavesdropping scenarios on both RF and FSO links. This study highlights
how strategic adjustments in system parameters such as interference
signal-to-noise ratio, time switching factor, energy conversion
efficiency, and number of RIS reflective elements can substantially
enhance physical layer security. The research emphasizes that better
weather conditions and improved detection methods also contribute
positively to securing communications against sophisticated
eavesdroppers equipped with advanced optical devices.

Incorporating findings from \[Narang et al., 2024\], we see further
advancements in dual-hop mixed FSO RF systems employing differential
chaos shift keying (DCSK) to optimize performance under various
atmospheric conditions including Gamma-Gamma turbulence and Nakagami-m
fading models. The study investigates three dual-hop communication
systems: FSO-FSO, RF-FSO, and FSO-RF using decode-and-forward relaying
where DCSK is employed to enhance system confidentiality. Notably, while
the FSO-RF-DCSK system demonstrated superior performance in terms of
BER, the all-optical (FSO-FSO) configuration exhibited significantly
better outcomes in terms of secrecy outage probability (SOP),
highlighting the trade-offs between performance and confidentiality.

Both studies affirm that strategic manipulation of system parameters
such as fading severity, atmospheric conditions, number of RIS elements,
and pointing errors can substantially bolster system resilience against
diverse eavesdropping modalities. They suggest that future research
should focus on optimizing RIS configurations and power allocation
strategies to further enhance the secrecy performance. Additionally,
they highlight the potential for integrating advanced signal processing
techniques and exploring more complex eavesdropping scenarios to address
evolving security threats in wireless communications.

This comprehensive analysis not only underscores the pivotal role of RIS
in enhancing physical layer security but also sets a forward-looking
agenda for integrating sophisticated technological innovations to
fortify wireless communication systems against evolving security
threats.

## Supertopic 5: Hybrid RF-FSO Security Strategies

❓ **Question 1: What performance metrics (BER, secrecy rate, outage
probability) characterize RIS-assisted dual-hop RF-FSO networks under
eavesdropping scenarios?**

IMPROVED SUMMARY: The comprehensive studies by Ahmed et al. (2023) and
Wang et al. (2023) delve into the enhancement of physical layer security
within dual-hop RIS-assisted RF-FSO communication systems, confronting
various eavesdropping scenarios. Ahmed et al. (2023) meticulously model
the RF link with Nakagami-m fading and the FSO link influenced by Málaga
turbulence coupled with pointing errors, significantly affecting
transmission reliability and security. They derive closed-form
expressions for several critical secrecy performance metrics such as
average secrecy capacity, secrecy outage probability, and effective
secrecy throughput, substantiated through rigorous Monte Carlo
simulations. These simulations confirm the robustness of the proposed
model in safeguarding confidential communications against different
eavesdropping modalities.

Wang et al. (2023) extend this analysis by incorporating a
wireless-powered jammer that transmits signals reflected by an RIS to
disrupt eavesdropping activities effectively. Their study highlights how
RIS technology not only dynamically adjusts signal phases but also
utilizes jamming techniques to enhance system security significantly.
They provide theoretical expressions for secrecy outage probability
(SOP) and average secrecy capacity (ASC), validated using Monte Carlo
simulations, demonstrating substantial improvements in these metrics
when compared to RIS-free systems.

Building on these insights, Liu et al. (2024) explore the physical-layer
security performance of a RIS-assisted hybrid FSO-RF system employing
non-orthogonal multiple access (NOMA). They focus on a dual-hop
communication model where the source transmits an optical NOMA signal to
a relay, which then forwards it to two users in the presence of an
eavesdropper. This study introduces scenarios where the far user
receives signals solely via RIS-reflected paths while the near user
benefits from both direct and reflected paths, enhancing security
robustness \[Liu et al., 2024\]. The FSO link's Gamma-Gamma distribution
and RF's Nakagami-m fading are considered, with derived analytic and
asymptotic expressions for SOP under varying eavesdropping conditions.
The integration of direct and RIS-reflected paths is shown to provide
optimal security outcomes.

Further expanding on these themes, Wang et al. (2024) investigate uplink
secrecy performance in a novel three-dimensional heterogeneous network
comprising high-altitude platforms (HAPs) and unmanned aerial vehicles
(UAVs). Utilizing Gamma-Gamma distribution for atmospheric turbulence
characterization in FSO links and Nakagami-m fading for wiretap RF
links, their findings underscore the dependency of secrecy performance
on the weaker channel between RF and FSO links \[Wang et al., 2024\].
The study also emphasizes how adjusting the number of RIS elements and
terrestrial users can optimize system performance, particularly under
high atmospheric turbulence conditions.

Incorporating findings from Sun et al. (2024), we see further
advancements in hybrid RF/FSO systems under dual eavesdropping scenarios
where both RF and FSO links are susceptible to interception \[Sun et
al., 2024\]. Sun et al.'s research introduces a novel approach using
RIS-based interference specifically tailored to disrupt both RF and
optical eavesdroppers effectively. Their analysis includes deriving
Strict Positive Secrecy Capacity (SPSC) and Secure Outage Probability
(SOP), with Monte Carlo simulations affirming these metrics' validity
under varied system parameters like interference signal-to-noise ratio,
time switching factor, energy conversion efficiency, number of RIS
reflective elements, and environmental conditions.

Both studies emphasize the critical role of system parameters such as
fading severity, atmospheric conditions, detection techniques, pointing
errors in influencing overall security performance. Wang et al. (2023)
further explore the impact of time switching factor, energy conversion
efficiency, average interference noise ratio, number of RIS reflecting
elements, and link distances on system security. Their findings suggest
that optimizing these parameters can substantially improve the system's
resistance to eavesdropping.

This detailed exploration underscores not only the technical feasibility
but also the practical implications of deploying advanced RIS technology
in dual-hop RF-FSO networks to effectively enhance physical layer
security. Future research directions proposed include exploring
optimization of RIS configurations under various environmental
conditions and integrating advanced machine learning techniques for
dynamic RIS configuration to further enhance system security \[Ahmed et
al., 2023; Wang et al., 2023; Liu et al., 2024; Wang et al., 2024; Sun
et al., 2024\].

❓ **Question 2: Can intermediate relays in RF-FSO dual-hop systems act
as friendly jammers, and how does this strategy improve secrecy
capacity?**

IMPROVED SUMMARY: In their comprehensive analysis, Mandira et al. (2023)
delve into the intricacies of optimizing secrecy performance within
mixed RF-FSO communication systems under challenging fading conditions
characterized by α−η−μ and Málaga models. The study meticulously
constructs a dual-hop communication framework that incorporates both RF
and FSO technologies, where RF links are affected by α−η−μ fading while
FSO links are influenced by Málaga turbulence along with pointing
errors. This setup allows for an extensive evaluation of secrecy metrics
including average secrecy capacity, secrecy outage probability, and
probability of non-zero secrecy capacity. These metrics are rigorously
derived using sophisticated mathematical formulations involving
univariate and bivariate Meijer<span dir="rtl">’</span>s G and
Fox<span dir="rtl">’</span>s H functions.

Sharma et al. (2024) further enhance this discourse by analyzing the
hybrid FSO-RF system under Gamma-Gamma distribution for FSO links and
Nakagami-m distribution for RF links, providing a detailed examination
of the impact of these fading conditions on the end-to-end secrecy
capacity \[Sharma et al., 2024\]. Their findings indicate that the
secrecy capacity improves with stronger line-of-sight components to both
the legitimate user and the eavesdropper, highlighting the critical role
of fading parameters in system performance.

A significant aspect of this research is the application of variable
gain relaying in the RF-FSO system, which is shown to substantially
enhance the system's ability to maintain secrecy under various
atmospheric disturbances \[Mandira et al., 2023\]. Furthermore, the
study provides a comparative analysis between heterodyne detection (HD)
and intensity modulation with direct detection (IM/DD), where HD emerges
as markedly superior in terms of improving secrecy performance.

Lei et al. (2018) contribute to understanding how atmospheric
turbulence, pointing errors, detection technology, path loss, and energy
harvesting affect the secrecy performance of mixed RF-FSO downlink SWIPT
systems. They underscore that improving pointing accuracy and employing
heterodyne detection can notably enhance secrecy performance while also
highlighting critical trade-offs involved in managing path loss and
energy harvesting efficiency \[Lei et al., 2018\].

Saber et al. (2020) analyze a mixed RF-FSO decode-and-forward relaying
system with energy harvesting capabilities focusing on how Nakagami-m
fading in RF channels and Malaga turbulence with pointing errors in FSO
channels affect security metrics such as average secrecy capacity and
secrecy outage probability \[Saber et al., 2020\]. Their results
demonstrate that physical-layer security performance improves with
increasing SNR at the relay and destination but deteriorates with higher
SNR at the eavesdropper.

Wang et al. (2023) introduce an innovative approach by integrating a
Reconfigurable Intelligent Surface (RIS) into the mixed RF/FSO system to
act as a friendly jammer against eavesdropping activities. This
integration significantly improves physical layer security by utilizing
a wireless-powered jammer whose signals are reflected by RIS towards
eavesdroppers, effectively disrupting their attempts to intercept
communications \[Wang et al., 2023\]. The study meticulously analyzes
how RIS-related parameters such as number of reflecting elements, link
distances before and after reflection, time switching factor, energy
conversion efficiency, and average interference noise ratio influence
system security.

Looking forward, Mandira et al. (2023) suggest avenues for future
research which include integrating advanced modulation techniques and
employing machine learning algorithms to further refine the secrecy
capabilities of mixed RF-FSO systems. They also propose investigating
more complex channel conditions and considering scenarios involving
multiple eavesdroppers to comprehensively assess system robustness
\[Mandira et al., 2023\].

Pattanayak et al. (2020) complement these findings by exploring how
different detection techniques—specifically heterodyne versus intensity
modulation/direct detection—impact physical layer security in a mixed
FSO/RF system besieged by multiple passive eavesdroppers. They provide
closed-form expressions for secrecy outage probability (SOP) and secrecy
throughput (ST), derived using Meijer<span dir="rtl">’</span>s
G-function, with results validated through Monte Carlo simulations
\[Pattanayak et al., 2020\].

Together, these studies underscore a multi-faceted approach to enhancing
physical layer security in mixed FSO/RF systems, advocating for a
combination of advanced detection techniques and variable gain relaying
to combat both environmental challenges and sophisticated eavesdropping
tactics.

❓ **Question 3: How do relay placement and UAV-based relay mobility
affect secrecy performance in hybrid RF-FSO secure networks?**

IMPROVED SUMMARY: In their groundbreaking study, Song et al. (2025)
delve into the enhancement of communication security in unmanned aerial
vehicles (UAVs) through a hybrid RF/FSO system. This innovative approach
leverages the strengths of both RF and FSO technologies to address
secure and covert communication challenges, particularly in scenarios
involving active eavesdropping. The research introduces sophisticated
metrics such as secrecy outage probability (SOP) and effective secrecy
throughput (EST), which are crucial for assessing the robustness of
secure communications. Additionally, the RF link is utilized to generate
interfering signals that aid the FSO link in maintaining covert
operations, thereby enhancing the overall security framework.

Building on this foundation, Zhang et al. (2024) explore similar themes
within a space-air-ground integrated network (SAGIN), employing a
two-phase transmission approach using hybrid FSO/RF links. In this
model, a UAV first receives secrecy data via an RF link while
simultaneously emitting artificial noise to confuse potential
eavesdroppers. The data is then relayed to a satellite via an FSO link,
providing an additional layer of security against RF eavesdropping. This
study is particularly notable for its introduction of slot-based and
period-based transmission schemes, optimized for delay-sensitive and
delay-insensitive data respectively. These schemes are evaluated through
numerical simulations that demonstrate significant improvements in
average secrecy rates when compared to benchmark schemes without
trajectory and power optimization.

Both studies emphasize the importance of optimizing UAV trajectory and
power allocation to maximize secrecy rates—a strategy that proves
effective in enhancing physical-layer security. Zhang et al. (2024)
employ advanced optimization techniques such as block coordinate descent
and successive convex approximation to address nonconvex problem
formulations inherent in these systems.

Furthermore, Song et al. (2025) consider the impact of atmospheric
conditions on FSO link performance, acknowledging that fluctuations in
atmospheric parameters can significantly affect the reliability and
efficiency of optical transmissions. This aspect is critical for
ensuring consistent performance across varying environmental conditions.

The integration strategies for RF and FSO technologies within UAV
systems are explored extensively in both studies, highlighting how these
technologies can be seamlessly combined to enhance overall system
robustness against potential security breaches. Moreover, future
research directions suggested include real-time adaptive strategies for
transmission power adjustment and the integration of machine learning
techniques for dynamic adaptation of UAV trajectories and power
settings, which could further enhance system performance under varying
environmental conditions and threat levels.

Lei et al. (2018) contribute significantly to this field by analyzing a
secure dual-hop mixed RF-FSO downlink SWIPT system where both links
experience distinct fading effects—Gamma-Gamma for FSO and Nakagami-m
for RF links—and their interdependencies significantly influence secrecy
performance \[Lei et al., 2018\]. Their findings underscore how
atmospheric turbulence, pointing errors, detection technology, path
loss, and energy harvesting intricately affect SOP and SDO under various
signal-to-noise ratio conditions \[Lei et al., 2018\]. These insights
are crucial for designing systems that can maintain high levels of
security even under adverse conditions or sophisticated eavesdropping
attempts.

Adding to this body of knowledge, Saber et al. (2024) investigate the
secrecy performance of an integrated HAP-based FSO and UAV-enabled RF
downlink system using a decode-and-forward relaying protocol \[Saber et
al., 2024\]. They provide novel analytical insights into how atmospheric
turbulence, pointing errors, RF fading, and advanced detection
techniques like heterodyne detection (HD) impact the overall secrecy
performance \[Saber et al., 2024\]. Their results indicate that reducing
pointing errors and employing advanced detection techniques can
significantly enhance system security \[Saber et al., 2024\]. This study
also emphasizes the critical role of environmental and system parameters
in influencing the secrecy performance of integrated HAP-based FSO and
UAV-enabled RF systems \[Saber et al., 2024\].

Pattanayak et al. (2020) further enrich our understanding by analyzing
physical layer security in a two-way relay based mixed FSO/RF network
with multiple eavesdroppers \[Pattanayak et al., 2020\]. Their study
employs closed-form expressions derived using
Meijer<span dir="rtl">’</span>s G-function to evaluate SOP and ST under
different fading models—Nakagami-m for RF links and Málaga distribution
for FSO links—and various detection techniques including intensity
modulation/direct detection (IM/DD) and heterodyne detection (HD). The
inclusion of multiple eavesdroppers highlights the necessity for robust
security measures across different network configurations \[Pattanayak
et al., 2020\].

Overall, these studies not only advance our understanding of hybrid
communication systems in UAVs but also set a foundation for further
exploration into adaptive strategies and integration techniques that
could revolutionize secure UAV communications in challenging
environments.

❓ **Question 4: How does spatial diversity improve secrecy rate and
mitigate fading effects in dual-hop RF-FSO systems compared to
single-hop FSO?**

IMPROVED SUMMARY: In their comprehensive analysis, Lei et al. (2017)
delve into the secrecy performance of mixed RF-FSO systems, focusing on
dual-hop configurations where RF links experience Nakagami-m fading and
the FSO link is subject to Gamma-Gamma fading. This study rigorously
evaluates how atmospheric turbulence, pointing errors, and detection
technologies such as heterodyne detection and intensity modulation with
direct detection influence secrecy outcomes. Through analytical
derivations and Monte Carlo simulations, they validate their theoretical
models and derive closed-form expressions for secrecy outage probability
(SOP) and average secrecy capacity (ASC), also analyzing their
asymptotic behaviors in high signal-to-noise ratio scenarios \[Lei et
al., 2017\].

Building upon this framework, Pattanayak et al. (2022) explore physical
layer security in hybrid RF-FSO systems, particularly focusing on
dual-hop configurations that employ receiver diversity techniques such
as selection combining (SC) and maximal ratio combining (MRC). These
techniques significantly enhance system performance by mitigating fading
effects and improving secrecy rates. The study introduces additional
complexity by considering multiple eavesdroppers and reveals that hybrid
systems employing SC and MRC can robustly secure communications against
eavesdropping in urban environments where interception risks are
elevated \[Pattanayak et al., 2022\].

Both studies underscore the critical role of receiver diversity in
enhancing SOP. Pattanayak et al. (2022) further demonstrate that hybrid
systems employing SC and MRC offer superior security and reliability
compared to traditional mixed FSO/RF systems. They also highlight how
atmospheric turbulence and pointing errors critically impact system
performance, suggesting that these factors require careful modeling to
maintain effective communication security.

Expanding on these insights, Singh et al. (2022) analyze the performance
of mixed FSO/RF SWIPT systems under conditions of Málaga distributed
turbulence and double shadowed Rician fading affecting both FSO and RF
links respectively. Their findings reveal that pointing errors and
atmospheric turbulence not only degrade overall system performance but
can paradoxically enhance secrecy by reducing the eavesdropper's signal
quality. Additionally, they demonstrate how energy harvesting
capabilities integrated into these systems influence both energy
efficiency and security metrics such as secure outage probability and
strictly positive secrecy capacity.

Further advancing the field, Ahmed et al. (2023) incorporate a
reconfigurable intelligent surface (RIS) into dual-hop RF-FSO systems to
enhance physical layer security. Employing a model with Nakagami-m
fading for the RF link and Málaga turbulence with pointing error for the
FSO link, they develop closed-form expressions for various secrecy
metrics including average secrecy capacity, secrecy outage probability,
and effective secrecy throughput. The integration of RIS allows dynamic
adjustment of signal phases which significantly enhances resilience
against eavesdropping attempts \[Ahmed et al., 2023\]. This research
highlights how RIS technology not only improves the confidentiality of
transmitted information but also quantifies the impact of system
parameters such as fading severity and atmospheric conditions on secrecy
performance \[Ahmed et al., 2023\].

In conclusion, Lei et al. (2017), Pattanayak et al. (2022), Singh et al.
(2022), and Ahmed et al. (2023) collectively contribute to understanding
how dual-hop RF-FSO systems can leverage spatial diversity to enhance
secrecy rates and combat fading effects more effectively than single-hop
FSO systems. Future research is suggested to focus on more advanced
diversity techniques and adaptive systems that dynamically respond to
varying eavesdropping threats and environmental conditions, potentially
integrating quantum key distribution to further bolster security
measures in hybrid RF-FSO systems.

❓ **Question 5: What comparative analyses exist between spatial
diversity schemes in secure pure-FSO links versus hybrid RF-FSO
configurations?**

IMPROVED SUMMARY: The comprehensive study by Pattanayak et al. (2020)
delves into the intricacies of physical layer security (PLS) within
hybrid RF-FSO communication systems, focusing on dual-hop configurations
where the initial transmission is via radio frequency (RF), followed by
a combination of RF and free-space optical (FSO) links. The RF segments
are characterized using a Rayleigh distribution model, while the FSO
segments employ a Málaga distribution to accurately depict their
behavior under varying atmospheric conditions. Key performance metrics
such as secrecy outage probability (SOP) and effective secrecy
throughput (EST) are meticulously derived to quantify the system's
security posture.

In addition to receiver diversity strategies like selection combining
(SC) and maximal ratio combining (MRC), which significantly enhance
system robustness against eavesdropping, especially in urban settings,
the study also highlights how atmospheric turbulence and optical
detection inaccuracies—exacerbated by pointing errors—can adversely
affect communication security. Strategic application of SC and MRC can
mitigate some of these detrimental effects.

Shakir et al. (2021) extend this analysis by examining hybrid FSO/RF
systems under different eavesdropping modes—colluding and non-colluding.
Their research employs a hybrid system model with the FSO link
characterized by Málaga-M distribution and the RF link by Nakagami-m
distribution. They derive exact closed-form expressions for various
secrecy metrics including SOP, SOP∞, SPSC, ASC, and ASC∞, providing an
efficient tool to investigate the impact of channel parameters such as
fading severity, atmospheric turbulence severity, pointing error, number
of eavesdroppers, and eavesdropper link power on secrecy performance.
The increase in the number of eavesdroppers significantly degrades the
secrecy performance under both colluding and non-colluding modes.

Both studies emphasize the critical role of channel conditions and
eavesdropper presence in influencing physical layer security. Pattanayak
et al. provide a comparative analysis highlighting the advantages of
hybrid RF-FSO systems over traditional mixed FSO/RF configurations in
terms of enhanced security and reliability under diverse operational
conditions. Shakir et al.'s findings further underscore the sensitivity
of system's secrecy performance to environmental factors and
eavesdropping strategies.

Ai et al. (2020) contribute to this discourse by analyzing a hybrid
FSO/RF system employing a modified selection combining scheme that
accounts for both secrecy performance and diversity gain. Their study
incorporates atmospheric turbulence effects, FSO receiver pointing
errors, and RF power amplifier inefficiencies into their analysis. They
derive exact analytical expressions for performance indicators such as
average secrecy capacity (ASC) and secrecy outage probability (SOP),
providing insights into how these factors influence PLS performance
under various atmospheric and hardware impairments \[Ai et al., 2020\].
The results demonstrate that this modified selection combining scheme
not only enhances physical layer secrecy but also offers significant
resilience against diverse operational challenges, making it a viable
solution for secure communication in next-generation networks.

Althunibat et al. (2023) expand upon these findings by focusing on
dual-hop hybrid FSO-mmWave systems which utilize both FSO and millimeter
wave (mmWave) links simultaneously at each hop to enhance spectral
efficiency while maintaining link reliability even under different
weather conditions \[Althunibat et al., 2023\]. Their study develops a
mathematical framework to analyze various operational parameters' impact
on secrecy metrics like average secrecy capacity, secrecy outage
probability, and effective secrecy throughput in these systems. Monte
Carlo simulations validate their analytical results, demonstrating
robust secrecy performance across varying conditions including different
types of eavesdroppers such as FSO-Eve, RF-Eve, and Hybrid-Eve
\[Althunibat et al., 2023\]. This research underscores the effectiveness
of integrating FSO with mmWave technologies to provide resilient
solutions against potential security threats while adapting to
environmental changes.

Tokgoz et al. (2022) further enrich this discussion by exploring hybrid
FSO-mmWave systems from a physical-layer security perspective in
scenarios involving various types of eavesdroppers operating under
exponential atmospheric turbulence for FSO links and Weibull fading for
mmWave links \[Tokgoz et al., 2022\]. Their findings highlight that
Hybrid-Eve poses the greatest threat due to its capability to intercept
both link types simultaneously. The study emphasizes that understanding
the interplay between different channel impairments is crucial for
enhancing system robustness against sophisticated interception tactics
\[Tokgoz et al., 2022\].

The practical implications of implementing these diversity techniques in
real-world scenarios are discussed, emphasizing their effectiveness not
just in theoretical models but also in tangible applications. This
bridges the gap between experimental research and practical deployment,
suggesting pathways for future enhancements.

Looking ahead, both studies suggest several future research directions
aimed at further fortifying the security framework of hybrid RF-FSO
systems. These include exploring more advanced diversity techniques and
adaptive systems capable of dynamically responding to fluctuating
eavesdropping threats and environmental conditions. Additionally,
integrating quantum key distribution within these hybrid systems could
open new frontiers for securing optical communications against
sophisticated interception tactics \[Pattanayak et al., 2020; Shakir et
al., 2021; Ai et al., 2020; Althunibat et al., 2023; Tokgoz et al.,
2022\].
