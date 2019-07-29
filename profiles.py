'''profile class. Feed in information from .prof files and store
the information as profile() objects.'''

import numpy as np

class profile():
    def __init__(self, metadata, flux):
        self.__metadata(metadata)
        self.profile = np.array(flux)
    
    def __metadata(self,metadata):
        '''Private method to parse and store
        metadata'''
        x = metadata.split(' ')
        self.MJD = float(x[1])
        self.obs_sec = float(x[2])
        self.p = float(x[3])
        self.npulses = int(x[4])
        self.obs_freq = float(x[5])
        self.DM = float(x[6])
        self.nbins = int(x[7])
        self.domain = np.linspace(0, self.p, self.nbins)
        
