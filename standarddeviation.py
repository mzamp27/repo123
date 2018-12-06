# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 19:59:01 2018

@author: mzamp
"""

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for i in X:
        tot += (i-mean)**2
    std = (tot/len(X))**0.5
    return mean, std



#
#    # compute mean first
#    sumVals = 0
#    for s in L:
#        sumVals += len(s)
#    meanVals = sumVals / len(L)
#
#    # compute variance (average squared deviation from mean)
#    sumDevSquared = 0
#    for s in L:
#        sumDevSquared += (len(s) - meanVals)**2
#    variance = sumDevSquared / len(L)
#
#    # standard deviation is the square root of the variance
#    stdDev = variance**(.5)
#
#    return stdDev