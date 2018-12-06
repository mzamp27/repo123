# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:27:28 2018

@author: mzamp
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
 
    if exp == 0:
        return 1
    result = (base)
    while exp>1:
       result = result*base
       exp -= 1
    return result