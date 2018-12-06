# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:45:16 2018

@author: mzamp
"""

def fib(x):
    """assume x is an in >0
        returns Fibonacci of x"""
        
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
        