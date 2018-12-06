# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 19:43:59 2018

@author: mzamp
"""

def fancy_divide(list_of_numbers, index):
   try: 
       denom = list_of_numbers[index]
       return [simple_divide(item, denom) for item in list_of_numbers]
   except ZeroDivisionError:
       return [list_of_numbers[0]]
       

def simple_divide(item, denom):
   return item / denom