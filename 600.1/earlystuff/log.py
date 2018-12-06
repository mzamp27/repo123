# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:17:10 2018

@author: mzamp
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    a = b
    i = 1
    if b < x:   
        while a*b <= x:
            b = a * b
            i += 1
        return i
    elif b > x:
        return 0
    else:
        return 1
        