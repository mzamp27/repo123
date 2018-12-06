# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:40:34 2018

@author: mzamp
"""

def fastMaxVal(toConsider, avail, memo ={}):
    """ Assumes toConsider a list of all subjects, avail is the available weight,
    memo supplied by recursive calls.
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem
    and the subjects of that solution. """
        
    if(len(toConsider), avail) in memo:
       result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result =(0,())
    elif toConsider[0].getCost()>avail:
        #explore right branch
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake =\
            fastMaxVal(toConsider[1:],
                           avail-nextItem.getCost(),memo)
        withVal += nextItem.getValue()
        #explore right branch
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail, memo)
        
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal,withToTake + (next.Item,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result

def testMaxVal(foods, maxUnits, algorithm, printItems = True):
    print ('Menu Contains', len(foods), 'items')
    print ('Use a search tree to allocate', maxUnits, 'calories')
    
    val, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken =', val)
        for item in taken:
            print ('   ', item)
        