# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:21:02 2018

@author: mzamp
"""

#coin changing algo

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
    
    
    listtokeep = []
    elementtokeep = []
    for x in range(len(L)):
        if L[x] <= s:
            leftover = s % L[x]        
            multiplier = (s - leftover)/(L[x])
            elementtokeep.append(L[x])
            listtokeep.append(multiplier)
            s = s - (L[x]*multiplier)
            if s == 0:
                return sum(listtokeep)
            else:
                continue
        else:
            continue
    else:
        return ("no solution")