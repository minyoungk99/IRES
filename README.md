# IRES
Summer astronomy research, 10 weeks in National Centre for Radio Astronomy, India. Detecting pulsar mode changes.

3 main notebooks for detecting mode changes employ gaussian fitting, Kolmogorov-Smirnov (KS) test, and discrete/continuous wavelet transform (DWT/CWT).

 - **/R_wavelet/wavelet_sigtest.R** employs cumulative areawise significance testing on the DWT of ratios of profiles. Resulting lots are in **/plots/ratio_power_spectra.pdf**
  - **J0332_KS_test_sim.ipynb**, which also utilizes **/R_analysis/ks_test.R**
 - **J0332_gaussian_fitting.ipynb**

4th notebook **test_comparison.ipynb** to compare mode change classifications from different tests
