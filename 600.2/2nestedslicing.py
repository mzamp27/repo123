# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:34:10 2018

@author: mzamp
"""
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    
    copyofL = L.copy()
    
    largestsofar = sum(L)
    #bestsub = L
    
    
    #cut one off the front        
    for i in range(len(L)):
        if largestsofar < sum(L[i:]):
            largestsofar = sum(L[i:])
        copyofL = L[i:]
        
        #for each one cut off front cut one off back
        for j in range(len(copyofL)):                       
            if largestsofar < sum(copyofL[:(-j-1)]):                        
                largestsofar = sum(copyofL[:(-j-1)])
                #bestsub = L[:(-j-1)]
            
            
    return largestsofar