# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:01:26 2018

@author: mzamp
"""

balance = 42
annualInterestRate = 0.2

monthlyPaymentRate = 0.04

monthlyinterest = (0.2/12)


for month in range(12):
    
    payment = (balance*monthlyPaymentRate)
    balance = balance - payment
    interest = (balance*monthlyinterest)
    balance = balance + interest
    
    print ("Month " + str(month + 1) + " Remaining Balance: " + str(round(balance,2)))