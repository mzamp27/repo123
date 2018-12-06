# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:55:01 2018

@author: mzamp
"""
L = [0, -10, 5, 6, -4]


def f(i):
    return i +2

def g(i):
    return i > 5



def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    i = 0
    mutlist = []
    L2 = L.copy()
    olength = len(L2)
    
    for i in range(olength):
       if (g(f(L2[i]))) == True:
           mutlist.append(L2[i])
       else:
           L.remove(L2[i])
    if len(mutlist) == 0:
        return -1 
    else:
        mutlist.sort(reverse = True)
        return mutlist[0]