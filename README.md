# IRES
Summer astronomy research, 10 weeks in National Centre for Radio Astronomy, India. Detecting pulsar mode changes.

3 main notebooks for detecting mode changes employ gaussian fitting, Kolmogorov-Smirnov (KS) test, and discrete/continuous wavelet transform (DWT/CWT).

 - **/R_wavelet/wavelet_sigtest.R** employs cumulative areawise significance testing on the DWT of difference of profiles. Resulting plots are in **/plots/diff_xx_xx.pdf**. DWT of differneces identify many as significant, but knowing that holes in a contour indicate a significant feature, and that while cumulative areawise testing is designed to reduce (but not completely eliminate) false positives/contours, if we only consider contours with holes as significant, it produces quite a good result in mode change detection.
 
  - **J0332_KS_test_sim.ipynb**, which also utilizes **/R_analysis/ks_test.R**
 - **J0332_gaussian_fitting.ipynb**

4th notebook **test_comparison.ipynb** to compare mode change classifications from different tests. Resulting plot is **/plots/test_comp.jpeg**
