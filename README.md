# IRES
Summer astronomy research, 10 weeks in National Centre for Radio Astronomy, India. Detecting pulsar mode changes.

3 important notebooks for detecting mode changes employ gaussian fitting, Kolmogorov-Smirnov (KS) test, and discrete/continuous wavelet transform (DWT/CWT).

 - **fake_CWT.ipynb** which works on simulated pulse profiles, and **/R_wavelet/wt_spectrum.R** to analyze J0332 data. Resulting continuous wavelet transform (CWT) power spectrum plots are in **/power_spectrum**
  - **J0332_KS_test_sim.ipynb**, which also utilizes **/R_analysis/ks_test.R**
 - **J0332_gaussian_fitting.ipynb**
