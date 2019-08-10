'''Utility functions'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
import scipy.special as ss
import scipy.stats as st
from scipy.fftpack import fft, ifft
import utils as u
import fake_profile as fp
from astropy.modeling import models, fitting
import pywt

def noise_stats_out(profile,N, err=0.5):  
        '''This algorithm only works for ratio
        of profiles, that way the distribution
        of just noise can be Gaussian.
        
        N: Number to divide max value of 
        flux density by, hence choosing interval
        width to decrease critical flux density
        per loop
        
        err: Maximum range of skewness and 
        kurtosis about the values for a normal
        distribution.
        '''
        
        crit = np.max(np.abs(profile))
        delta = crit/N
        kurt = st.kurtosis(profile)
        skew = st.skew(profile)
        kurt_p = kurt
        skew_p = skew
        noise = profile
        iterations = 0
        
        while (np.abs(kurt) > err) or (np.abs(skew) > err): 
            noise = [i for i in profile if np.abs(i) <= crit]
            
            kurt_p = kurt
            skew_p = skew
            kurt = st.kurtosis(noise)
            skew = st.skew(noise)
            
            crit -= delta
            iterations += 1
        
        plt.hist(noise,bins=100)
        plt.show()
        
        plt.plot(noise)
        plt.title('Cutoff Spectral Density:{}'.format(crit))
        plt.show()
        print('length of noise:', len(noise))
        print("Delta: {}".format(delta))
        print("Iterations: {}".format(iterations))
        #print('Previous kurtosis: {}'.format(kurt_p))
        #print('Previous skew: {}'.format(skew_p))
        #print("Final kurtosis: {}".format(kurt))
        #print("Final skew: {}".format(skew))
        
        return np.mean(noise), np.std(noise)

def average_sd(sd):
    '''Compute average of standard deviations
    Double check that this is correct way'''
    x = 0
    
    for i in range(len(sd)):
        x += sd[i]**2
    return (x/2)**(1/2)

def chi_squared(ratio, sample_mean, sd):#todo - way to do for 1d array?
    '''Perform Chi Square test of profile ratios
    against white noise
    
    Parameters
    ----------
    ratios: 2-D array, nratios X nbins
        Array containing ratios of successive
        pulse profiles. It is assumed that the
        ratio is centered about 0 already.
    
    '''
    nratios = len(ratio)
    chi_arr = np.zeros(nratios)
    chi = 0
    df = len(ratio[0]) - 1
    
    #for each profile ratio in 2D array
    for i in range(nratios):
        chi = 0
        #for each bin
        for j in range(df):
            chi += ((ratio[i,j]) - sample_mean)**2 #no need to subtract 1 from ratio because already assumed
        chi = chi / sd**2
        chi_arr[i] = chi
 
    a = df/2 
    for i in range(nratios):
        lower = chi_arr[i]**2 / 2
        p = ss.gammaincc(a, lower)
        print("Between {}th and {}th profile, P( >chi squared): {}%".format(i, i+1, p*100))
    return chi_arr

def gaussian_fit(domain, data, amp, mean, stddev):
    '''Multi peak gaussian fit given educated guesses
    of Gaussian models. Ignore the first 3 values in
    g.parameters, which is from models.Gaussian1D(amplitude=0).
    
    Parameters
    ----------
    domain: 1D array
    Domain over which data is to be fitted. Must have
    same size as data.
    
    data: 1D array
    Pulse profile data in time domain to be fitted.
    
    amp, mean, stddev: iterable
    Iterable of guesses for each Gaussian component
    to be used in model. Most important is the mean
    guesses.
    
    Returns
    -------
    g: CompoundModel object
    Fitted compoundmodel object. 
    '''
    g_init = models.Gaussian1D(amplitude=0)
    for i in range(len(amp)):
        g_init += models.Gaussian1D(amplitude=amp[i], mean=mean[i], stddev=stddev[i])
    
    fitter = fitting.LevMarLSQFitter()
    g = fitter(g_init, domain, data)
    return g

def phase_shift(prof_arr, basis=0, N=714, P=.714):
    '''Phase shift all profiles to match profile at
    basis index.
    
    Parameters
    ----------
    prof_arr: 1D array
    Array of profile class objects.
    
    basis: int
    Profiles will shift phase to match
    profile with index = basis in data
    
    N: int
    Number of bins
    
    P: float
    Profile length in seconds'''
    
    data = prof_arr.copy()
    
    for i in range(len(data)):
        if i != basis:
            #find tau, convert into nbins using taylor's paper, but
            #for now, makeshift using max value of profile
            
            #find delay
            ref = data[basis].profile.tolist()
            m = ref.index(max(ref))#index of max flux value in reference profile
            comp = data[i].profile.tolist()
            n = comp.index(max(comp))
            delay = n-m
            
            #find k, omega
            k = np.arange(N)
            omega = 2*np.pi*k / N
            #phase shift
            phase = np.exp(1j*omega*delay)
            
            yf = fft(comp)
            iyf = ifft(yf * phase)
            data[i].profile = np.abs(iyf)
    return data

def gridplot(data, ncols, figsize=(15,70), hist=True, nbins=100, confid_int=False, mjd=None):
    '''Plot grid of histograms/plots
    
    Parameters
    ----------
    data : 2D array
    2D array to be plotted, organized row-wise, ie, a single row
    corresponds to data for a single plot.
    
    nrows : int
    Number of rows in grid
    
    ncols : int
    Number of columns in grid
    
    figsize : tuple, optional
    Tuple specifying total grid size in inches (width, height)
    
    hist : bool, optional
    Plots histograms if True. Line plots otherwise.
    
    nbins : int, optional
    Number of bins in histogram
    
    mjd : n-D array, optional
    Array of corresponding MJDs to use as lineplot titles
    
    x : 1D array, optional
    If hist=False, provide optional 
    '''
    #inteprolate grid row size from specified column size
    nplots = len(data)
    remainder = (nplots % ncols) == 0#boolean, true if ncols perfectly divides nplots
    if remainder:
        nrows = nplots // ncols
    else:
        nrows = (nplots // ncols) + 1
        
    
    fig = plt.figure(figsize=figsize)
    for i, val in enumerate(data):
        ax = fig.add_subplot(nrows, ncols, i+1)
        if hist:
            n,bins,patches = ax.hist(val, bins=nbins)
            if mjd is not None:
                ax.set_title(str(mjd[i]))
            else:
                ax.set_title(i)
            if confid_int:
                sd = np.std(val)
                mu = np.mean(val)
                ymax = np.max(n)
                ax.axvspan(xmin=mu+(2*sd), xmax=bins[-1], color='r',alpha=.1)
                ax.axvspan(xmin=bins[0], xmax=mu-(2*sd), color='r',alpha=.1, label="2-sigma")
                ax.legend()
        else:
            ax.plot(val)
            if mjd is not None:
                ax.set_title(str(mjd[i]))
            else:
                ax.set_title(i)
    fig.tight_layout() #makes it look somewhat better
    plt.show()
    
def dwt_denoise(profile, d_ignore=[-1], wavelet_name='sym20', mode='zero', max_level=None)
    '''This function utilizes pywt's discrete wavelet transform 
    to denoise a given 1D array signal by discarding the smallest
    scale DWT coefficients in wavelet domain and returning reconstructed
    signal through inverse DWT.
    
    Parameters
    ----------
    profile : 1D array
    1D array signal to apply DWT on. Theoretically, the pywt functions used
    can be applied to nD arrays.
    
    d_ignore : list
    List of indices indicating which detail coefficients to ignore.
    -1 corresponds to smallest scale coeffients.
    
    wavelet_name : string
    pywt wavelet name. Check with pywt.wavelist(kind='discrete')
    
    mode : string
    DWT signal extension modes. Check with pywt.Mode.modes
    
    max_level : int
    Maximum level to decompose signal to using DWT.
    '''
    
    if max_level is None:
        max_level = pywt.dwt_max_level(len(calib[36]), wavelet)
    wavelet_name = wavelet_name
    wavelet = pywt.Wavelet(wavelet_name)
    coeff = pywt.wavedecn(profile, wavelet, mode=mode, level=max_level)
    
    for i in d_ignore:
        coeff[i] = {k: np.zeros_like(v) for k, v in coeff[i].items()}
        
    return pywt.waverecn(coeff, wavelet, mode='zero')
    