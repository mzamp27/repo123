# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:27:26 2018

@author: mzamp
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)