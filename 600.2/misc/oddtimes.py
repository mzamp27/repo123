# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:42:18 2018

@author: mzamp
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    sortedcopyL = sorted(L, key = None, reverse = True)
    
     
    if sortedcopyL == []:         
        return None
    elif sortedcopyL.count(sortedcopyL[0])%2 != 0:
        return sortedcopyL[0]
    else:
        for i in range(sortedcopyL.count(sortedcopyL[0])):
            sortedcopyL.remove(sortedcopyL[0])
        return largest_odd_times(sortedcopyL)
        