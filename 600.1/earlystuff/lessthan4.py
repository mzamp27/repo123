# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:35:42 2018

@author: mzamp
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    
    fourlist = []
    for i in range(len(aList)):
        if len(aList[i]) <= 4:
            fourlist.append(aList[i])
    return fourlist        