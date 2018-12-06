# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:17:27 2018

@author: mzamp
"""

def greedy_cow_transport(items, maxCost):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of items to numbers"""
    cowsleft = items.copy()
    
    itemsCopy =  sorted(cowsleft.items(), key=lambda x: x[1], reverse = True)
    
    result = []
    tripcounter = len(itemsCopy)
    
    while cowsleft != {}:
        
        triplist = []
        
        
        totalCost = 0.0
        
        for i in range(    (len(itemsCopy)- (len(itemsCopy)-(len(cowsleft))))):
            
            if (totalCost+itemsCopy[i][1]) <= maxCost:
                triplist.append(itemsCopy[i][0])
                totalCost += itemsCopy[i][1]
                cowsleft.pop(itemsCopy[i][0],None)
                
                
        tripcounter -= 1
        result.append(triplist)
        itemsCopy = sorted(cowsleft.items(), key=lambda x: x[1], reverse = True)
    return (result)
cows = {'ana': 5, 'belle': 3, 'claire': 2, 'donnie': 6, 'elenor': 4, 'francis': 3}
g1 = greedy_cow_transport(cows, 7)