# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:14:02 2018

@author: mzamp
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x
