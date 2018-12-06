# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:21:04 2018

@author: mzamp
"""

f = open('julytemps.txt',mode = 'w')
f.write('''Boston July Temperatures''')
f.close()

 
f = open('julytemps.txt', mode = 'r')
#data = f.read()
#for i in range(len(data)):
#    print (data[i])
for line in f:
    print(line)