'''Class to store fitted param array and covx array per profile in gaussian fitting'''


class gaussfit():
    def __init__(self, profile, params, cov, mjd=None):
        self._profile = profile
        self._params = params
        self._cov = cov
        self._mjd = mjd
        
    @property
    def profile(self):
        return self._profile
    
    @property
    def params(self):
        return self._params
    
    @property
    def cov(self):
        return self._cov
    
    @property 
    def mjd(self):
        return self._mjd