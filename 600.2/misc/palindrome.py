# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:25:50 2018

@author: mzamp
"""

def isPalindrome(aString):
    """ checks if a string is a pallindrone"""
    
    copy = aString
    if len(copy) == 0:
        return True
    elif len(copy) == 1:
        return True
    else:        
        for i in range(len(copy)):
            if copy[i] == copy[-i-1]:
                pass    
            else:
                return False
        return True        