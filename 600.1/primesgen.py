# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:29:39 2018

@author: mzamp
"""

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
            
            
            
#for n in range(2, 10):
#    for x in range(2, n):
#        if n % x == 0:
#            print (n, 'equals', x, '*', n/x)
#            break
#    else:
#        print (n, 'is a prime number')
 