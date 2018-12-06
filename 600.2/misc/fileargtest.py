# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:54:47 2018

@author: mzamp
"""
from sys import argv


script,file = argv



print ('This is the script', script, 'opening the file' ,file)
f = open(file)
print (f.read())
