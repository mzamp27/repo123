# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:16:22 2018

@author: mzamp
"""

delta = 0.01

while True:
    repayment = round(((lower + upper)/2), 2)
    unpaidBalance = balance
    numberOfRepayments = 0
    
    if balance > delta:
        lower = repayment
        
    elif balance < -delta:
        upper = repayment
    
    else:
        break