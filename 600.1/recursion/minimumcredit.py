# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:56:45 2018

@author: mzamp
"""

balance = 3329
annualInterestRate = 0.2

monthlyPaymentRate = 0.04

monthlyinterest = (0.2/12)

payment = (10*(balance/120))+(balance*annualInterestRate/24)


for month in range(12):
    
    
    balance = balance - payment
    interest = (balance*monthlyinterest)
    balance = balance + interest
    
    print ("Month " + str(month + 1) + " Remaining Balance: " + str(round(balance,2)))
    
print ((round(payment/10))*10)