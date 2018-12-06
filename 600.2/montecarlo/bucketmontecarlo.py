# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:24:39 2018

@author: mzamp
"""
import random
#You have a bucket with 3 red balls and 3 green balls. 
#Assume that once you draw a ball out of the bucket, you don't replace it. 
#What is the probability of drawing 3 balls of the same color?

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    
    
    samecolorcount = 0
    for i in range(numTrials):
        bucket = ['R','R','R','G','G','G']
        tmppulls = []
        for x in range(3):
            tmppulls.append(random.choice(bucket))
            bucket.remove(tmppulls[-1])
        if tmppulls.count('R') == 3 or tmppulls.count('G') == 3:
            samecolorcount += 1
    return (float(samecolorcount/numTrials))        