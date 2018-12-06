# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

epsilon = 0.01
y= 54.0
guess = y/2.0
numGuesses = 0


while abs(guess*guess - y) >= epsilon:
    numGuesses +=1
    guess = guess - (((guess**2)-y)/(2*guess))
    decimal = (guess*guess - y)
    print (guess)
    print (decimal)
    