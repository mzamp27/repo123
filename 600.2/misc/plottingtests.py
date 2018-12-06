# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:54:56 2018

@author: mzamp
"""

import matplotlib.pyplot as plt

x = [3,5,7]
y = [5,7,4]

plt.plot(x,y)



def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    #append list virussize to trial list   
    triallists = []
    
    
    #x list is time values 0 - 300
    for x in range(numTrials):
    #y list is avg population among trials for each time step
        virussize = []
        viruslist = []
    #create instance and do 300 updates append each update to the list virussize
        for y in range(numViruses):
            viruslist.append(SimpleVirus(maxBirthProb,clearProb))
            
        patient = Patient(viruslist,maxPop)
        for i in range(300):
            virussize.append(patient.update())
        triallists.append(viruslist)    

    
    #zipfunction the trialavg list to get averages at each time step
    zippedlist = []
    for i in range(len(triallists[0])):
        zippedlist.append(zip())
    #plot x as 300 time steps, y is the resulting list from zipping trial avgs
    plt.plot(range(300), )