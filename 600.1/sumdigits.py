# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:48:57 2018

@author: mzamp
"""

def sumDigits(N):
    
   
   if (N) < 10:
       return N
   
   else:
       return (N % 10) + sumDigits(N//10)
           
       