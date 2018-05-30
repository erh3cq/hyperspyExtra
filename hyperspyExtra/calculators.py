# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:09:25 2018

@author: Eric Hoglund
"""

def bragg_reflection(hkl, lattice, units='A-'):
    if isinstance(hkl, int):
        N = hkl
    elif isinstance(hkl, list) and lne(hkl)==3:
        N = hkl[0]**2 + hkl[1]**2 + hkl[2]**2
    else:
        raise Exception('hkl should be an integer N or a list with length three.')
    
    
if __name__ == "__main__":
    print(len([0,1,2]))