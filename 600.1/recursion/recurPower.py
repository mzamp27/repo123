# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:39:35 2018

@author: mzamp
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*recurPower(base,exp-1)