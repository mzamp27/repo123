# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:42:18 2018

@author: mzamp
"""

''' Ultimate Masters Profit Calculator
lowest available cost of version of card used'''
import random


''' Mythic List:'''
Mythicdict = {
    'Tarmogoyf' : 50,
    'Lilliana_of_the_Veil' : 60,
    'Temporal_Manipulation' :  55,
    'Karn_Liberated' : 60,
    'Cavern_of_Souls' : 52,
    'Snapcaster_Mage' : 45,
    'Karakas' : 40,
    'Dark_Depths' : 30,
    'Mana_Vault' : 15,
    'Bitterblossom' : 33,
    'Emrakul' : 25,
    'Kozilek' : 24,
    'Ulamog' : 19,
    'Leovold' : 16,
    'Vengevine' : 23,
    'Mikaeus' : 12,
    'Platinum_Emperion' : 10,
    'Sigarda' : 12,
    'Baelfire_Dragon' : 11,
    'Lord_of_extinction' : 9}
    
    
    
    
''' Rare List:''' 
Raredict = {   
    'Engineered_Explosives' : 38,
    'Noble_Heirarch' : 50,
    'Ancient_Tomb' : 24,
    'Celestial_Collonade' : 30,
    'Demonic_Tutor' : 25,
    'Goryos_Vengence' : 22,
    'Through_the_Breach' : 22,
    'Gaddock_Teeg' : 24,
    'Urborg' : 15,
    'Life_from_the_loam' : 18,
    'Reanimate' : 13,
    'Fulminator_Mage' : 12,
    'Maelstrom_Pulse' : 12,
    'Entomb' : 13,
    'Creeping_tar_pit' : 10,
    'Raging_Ravine' : 8,
    'Lavaclaw_Reaches' : 2,
    'Tasigur' : 2,
    'Stirring_Wildwood' : 1,
    
    'Gamble' : 7,
    'All_is_Dust' : 12,
    'Eldrazi_conscription' : 8,
    'Glen_eldra' : 19,
    'Phyrexian_altar' : 35,
    'Phyrexian_tower' : 30,
    'Runed_halo' : 14,
    'Squee' : 3,
    'Visions_of_beyond' : 4,
    'Vexing_Devil' : 7,
    'Wall_of_reverance' : 2,
    

#Unknown Rares estimates
 
    'a' : 1,
    'b' : 1,
    'c' : 1,
    'd' : 1,
    'e' : 1,
    'f' : 1,
    'g' : 1,
    'h' : 1,
    'i' : 2,
    'j' : 2,
    'k' : 2,
    'l' : 2,
    'm' : 2,
    'n' : 2,
    'o' : 2,
    'p' : 2,
    'q' : 3,
    'r' : 3,
    's' : 3,
    't' : 3,
    'u' : 4,
    'v' : 4,
    'w' : 4}
    
    
    
    
''' Uncommon List'''
   # Eternal_Witness = 3
    #Kitchen_Finks = 4 
    
def simulatebox():
    mythicspicked = []
    for i in range(2):
        mpick = random.choice(list(Mythicdict.keys()))
        while mpick in mythicspicked:
            mpick = random.choice(list(Mythicdict.keys()))
        mythicspicked.append(mpick)
    rarespicked = []
    for i in range(22):
        rpick = random.choice(list(Raredict.keys()))
        while rpick in rarespicked:
            rpick = random.choice(list(Raredict.keys()))
        rarespicked.append(rpick)
    #boxtopper = random.choice(list(Mythicdict.items()))
    #foilrare
    #foils
    valuetotalm = 0
    valuetotalr = 0
    for i in mythicspicked:
        valuetotalm += Mythicdict[i] 
    for i in rarespicked:
        valuetotalr += Raredict[i]
    finaltotal =  (valuetotalm + valuetotalr) 
    
    
    #return mythicspicked,rarespicked,finaltotal
    return  finaltotal
     
def simulatemulti(n):
    
    valueboxes = 0
    for i in range(n):
        valueboxes += simulatebox()

    return valueboxes/n


     