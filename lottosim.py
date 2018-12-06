# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:28:04 2018

@author: mzamp
"""
import random

total_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44}
#winningnumber =  set(random.sample(total_set, 6))





def pick_number():
    ''' Returns a  single sorted pick of 6 lotto numbers in the range of  1-44 as a set'''
    
    
#    total_set = set()    
#    for i in range(44):
#        total_set.add(i+1)
#        
#     
#   
    global winningnumber
    return set(random.sample(total_set, 6))
        
        
def quick_pick(n, winner):
    '''  Returns a list of n amount of quickpicks each element in the list is a set'''

    if n == 0 :
        return ('Please enter an argument for n being 1 or greater')
    else:
        quickpicklist = []
        for i in range(n):
            checker = pick_number()
            if checker == winner:
                print ('Match found!', winner)
                return True
            else:   
                quickpicklist.append(checker)
            
            
    
    #print('Not found after', n, 'quickpicks checked.  Reiterating...')
    #print (winner)
    return False


def lottosim(nquicks, nsims, samequicks = False):
    
    winningnumber =  set(random.sample(total_set, 6))
    simcount = 0
    while quick_pick(nquicks, winningnumber) == False:
        simcount += 1
        winningnumber =  set(random.sample(total_set, 6))
        
        
    return simcount
    
    
    
    
#    if samequicks == True:
#        quickpicks = quick_pick(nquicks)
#        for i in range(nsims):
#            winner = pick_winning_number()
#            if winner in quickpicks:
#                print ('Congrats you got it!!', winner)
#                return True
#            else:
#                return False
#                
#            
#    else:    
#        for i in range(nsims):
#            winner = pick_winning_number()
#            quickpicks = quick_pick(nquicks)
#            
#            if winner in quickpicks:
#                print('Congrats!', 'Your quick pick had a winner!!', quickpicks, 'is matched YOU WON!!!', winner)
#                return True
#            else:
#               
#                return False
       

def lotto_until_won(qpicks):
    
    simcount = 0
    
    while lottosim(qpicks,1) != True:
        simcount +=1
    
    return simcount