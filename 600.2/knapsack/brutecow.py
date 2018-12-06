# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 21:26:17 2018

@author: mzamp
"""


def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]



def brute_force_cow_transport(cdict, weightlimit):
    """Assumes cdict is a dictionary of cows as keys with weights as values
         get_partitions(L) generates all the combinations of cows possible
         weightlimit is the allotted weight allowed each trip"""
    #First check if either input is 0
    if cdict == {} or weightlimit == 0:
        result = []
        return result    

    #next check if all cows can go on one trip
    #create a list from the dict given 
    cowslist =  sorted(cdict.items(), key=lambda x: x[1], reverse = True)
    totalall = 0
    #iterate over list and add up weights into totalall
    for i in range(len(cowslist)):
        totalall += cowslist[i][1]
    if totalall <= weightlimit:
        #returns names as a list
        result = sorted(cdict.keys())
        return result
    
    #now create partitions of all possible combos 6 cows is 203 partitions 
    cowspart = [item for item in (get_partitions(sorted(cdict.keys())))]
    
    #prepare a list for referencing, 6 cows will hold 203 values
    totalpartsvallist = []       
    
    #i will get up to 202
    for i in range(len(cowspart)):
        #new list for each element this list clears for each combo 203 times
        partsvalslist1 = []
        
        
        #j will test amount of subsets in cowspart up to 6 sets for 6 single cows
        for j in range(len(cowspart[i])):                          
            partvalues = 0
             
            # k will test amount of cows per subset in j              
            for k in range(len(cowspart[i][j])):
               partvalues += (cdict.get(cowspart[i][j][k]))
               
            partsvalslist1.append(partvalues)
               
               
        totalpartsvallist.append(partsvalslist1)
    
    #compare totalpartsvallist to input weight
    maxweightdict = {}
    for i in range(len(totalpartsvallist)):
        if max(totalpartsvallist[i]) <= weightlimit:
            maxweightdict[i] = totalpartsvallist[i] 

    optimalchoices = sorted(maxweightdict.values(), key = len)
    optimalchoicedictkey = list(maxweightdict.keys())[list(maxweightdict.values()).index(optimalchoices[0])]
    #cowspart[optimalchoicedictkey]
    
    
    return (cowspart[optimalchoicedictkey])    

# cows = {'ana': 5, 'belle': 3, 'claire': 2, 'donnie': 6, 'elenor': 4, 'francis': 3}

    
#    for i in range(0,len(partition)):
#        for j in range(0,len(partition[i])):
#            num[i][j]=cows[partition[i][j]]
#            print(partition)
#            
#    #for i in range(len(maxdicttest.keys()):
     #maxdicttest.get(maxdicttest[i]) 
#    cowsleft = items.copy()
#    
#    itemsCopy =  sorted(cowsleft.items(), key=lambda x: x[1], reverse = True)
#    
#    result = []
#    tripcounter = len(itemsCopy)
#    
#    while cowsleft != {}:
#        
#        triplist = []
#        
#        
#        totalCost = 0.0
#        
#        for i in range(    (len(itemsCopy)- (len(itemsCopy)-(len(cowsleft))))):
#            
#            if (totalCost+itemsCopy[i][1]) <= maxCost:
#                triplist.append(itemsCopy[i][0])
#                totalCost += itemsCopy[i][1]
#                cowsleft.pop(itemsCopy[i][0],None)
#                
#                
#        tripcounter -= 1
#        result.append(triplist)
#        itemsCopy = sorted(cowsleft.items(), key=lambda x: x[1], reverse = True)
#    return (result)


