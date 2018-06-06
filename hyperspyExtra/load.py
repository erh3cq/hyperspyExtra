# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:47:33 2018

@author: erhog
"""

from hyperspy.signals import Signal1D # as hs

def load_from_txt(file, x_units='nm'):
    import numpy as np
    x, HAADF = np.loadtxt(file).T
    HAADF = Signal1D(HAADF)
    HAADF.metadata.General.title = 'HAADF Intensity'
    
    if x_units == 'nm':
        x *= 10**9
        HAADF.axes_manager[0].units = 'nm'
    
    HAADF.axes_manager[0].offset = x[0]
    HAADF.axes_manager[0].scale = x[1]-x[0]
    return HAADF