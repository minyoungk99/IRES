#Profile class create fake profiles

import matplotlib.pyplot as plt
import numpy as np

class fake_profile():
    '''Function to create a fake profile.
    
    Parameters
    ----------
    
    amp_arr : array_like
    Array or list of amplitudes for each gaussian component of a profile.
    
    mean_arr : array_like
    Array or list of means for each gaussian component of a profile.
    
    sd_arr : array_like
    Array or list of standard deviations for each gaussian component of a profile.
    
    period : float, optional
    Period of profile.
    
    nbins : int, optional
    Number of bins/samples in the profile.
    '''
    def __init__(self,amp_arr,mean_arr, sd_arr,period=100,nbins=512):
        self.amp = amp_arr
        self.mean_arr = mean_arr
        self.sd_arr = sd_arr
        self.nbins = nbins #phase bins
        self.p = period #in ms, not imp rn
        self.domain = np.linspace(0,self.p,num=self.nbins)
        self.d_profile = []
        #self.wn_sigma = wn_sigma

    def gaussian_pdf(self,domain,mu,sd):
        return (2*np.pi*sd**2)**(-1/2) * np.exp(-(domain-mu)**2 / (2*sd**2))

    def construct_profile(self,noise=False,wn_sigma=.03):
        '''Construct profile after initializing.
        
        Parameters
        ----------
        noise : bool, optional
        Set to True to add white noise to profile.
        
        wn_sigma : floab, optional
        Standard deviation of Gaussian white noise to be added.
        '''
        profile = np.zeros(self.nbins)
        for ind,m in enumerate(self.mean_arr):
            profile += self.amp[ind]*self.gaussian_pdf(self.domain, m, self.sd_arr[ind])
        
        self.wn_sigma = .03
        if noise:
            profile += np.random.randn(len(profile)) * wn_sigma #multiply by desired sigma
            
        self.profile = profile#/profile.sum()#normalize
    
    def derivative(self):
        '''Takes derivative of profile and saves in attribute d_profile.'''
        if len(self.profile) > 0:
            d_profile = []
            for i in range(len(self.profile)-1):
                d_profile.append((self.profile[i+1]-self.profile[i])/(self.p/self.nbins))
                
            self.d_profile = np.array(d_profile)
        else:
            print('Need to create profile array first!')
    
    def plot(self, derivative=False):
        '''To plot derivative, need to have called object.derivative() first'''
        if derivative:
            x = self.domain.tolist()
            del x[-1]
            plt.plot(x,self.d_profile)
            plt.xlabel("Time(ms)")
            plt.ylabel("Relative intensity Derivative")
            plt.title('Profile Derivative')
            plt.show()
        else:
            plt.plot(self.domain,self.profile)
            plt.xlabel("Time(ms)")
            plt.ylabel("Relative intensity")
            plt.title('Profile')
            plt.show()
            
    #possible speeding up by binary algorithm to choose values of crit
    def noise_stats(profile, N, err=0.5):  
        '''Compute sample mean and standard 
        deviation of off-pulse region given
        any profile. This method assumes
        1) Noise is Gaussian
        2) Profile is offset such that the true
        mean of said Gaussian noise is zero.
        This means when using this method on 
        ratio of profiles, one needs to do
        
        ratio = (profile1+1)/(profile2+1) 
        noise_stats(ratio-1)
        
        +1 to avoid dividing by zero
        
        N: Number to divide max value of 
        flux density by, hence choosing interval
        width to decrease critical flux density
        per loop
        
        err: Maximum range of skewness and 
        kurtosis about the values for a normal
        distribution.
        '''
        
        crit = np.max(profile)
        delta = crit/N
        kurt = st.kurtosis(profile)
        skew = st.skew(profile)
        
        while (np.abs(kurt) > err) or (np.abs(skew) > err):
            noise = [i for i in profile if np.abs(i) <= crit]
            kurt_p = kurt
            skew_p = skew
            kurt = st.kurtosis(noise)
            skew = st.skew(noise)
            crit -= delta
        
        plt.hist(noise,bins=100)
        plt.show()
        
        plt.plot(noise)
        plt.title('Critical flux density:{}'.format(crit))
        plt.show()
        print('length of noise:', len(noise))
        print("Delta: {}".format(delta))
        print('Previous kurtosis: {}'.format(kurt_p))
        print('Previous skew: {}'.format(skew_p))
        print("Final kurtosis: {}".format(kurt))
        print("Final skew: {}".format(skew))
        
        return np.mean(noise), np.std(noise)
    
