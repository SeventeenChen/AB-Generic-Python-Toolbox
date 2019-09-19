# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:12:04 2019

@author: beimx004
"""
import numpy as np
from scipy.signal import lfilter

def tdFilterFunc(par,x):
    
    coeffDimensions = len(par['coeffNum'].shape)
    
    if coeffDimensions == 1:
        nCh = 1;
    elif coeffDimensions == 2:
        nCh = par['coeffNum'].shape[0]
    else:
        raise ValueError('Filter coefficients must be organized in a vector or 2d matrix!')

    
    
    
    
    
    if nCh > 1:
        Y = np.zeros((nCh,x.size))
        for iCh in np.arange(nCh):
            Y[iCh,:] = lfilter(par['coeffNum'][iCh,:],par['coeffDenom'][iCh,:],x)
    else:
        Y = np.zeros((x.size))
        Y = lfilter(par['coeffNum'],par['coeffDenom'],x)
                
        
    return Y
    
    