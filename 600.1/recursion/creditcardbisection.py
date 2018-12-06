# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:45:46 2018

@author: mzamp
"""

balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0

lower = balance/12
upper = (balance * (1 + monthlyInterestRate)**12)/12

repayment = (lower + upper)/2

delta = .01

unpaidBalance = balance

while unpaidBalance != 0.01:
    repayment = round(((lower + upper)/2), 2)
    unpaidBalance = balance
    
        
    for n in range(12):
       monthlyUnpaidBalance = unpaidBalance - repayment
       increment = monthlyUnpaidBalance * monthlyInterestRate
       unpaidBalance = monthlyUnpaidBalance + increment

    if unpaidBalance < -0.01:
        upper = repayment
    elif unpaidBalance > 0.01:
        lower = repayment
    else:
        unpaidBalance = 0.01 
        
print ('Lowest Payment: ' + str(repayment))