# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 17:53:24 2018

@author: mzamp
"""

d = {1:10, 2:20, 3:30}


i = 0
j = 1





endlist = {}
klist = []
alist = []

    

for key in d:
    klist.append(key)

    if (d.values())[i] not in alist:
        alist.append(d.values())[i]
        endlist[alist[i]] = [klist[j]]
        i +=1
        j +=1
    else:
        endlist[alist[i]]= [klist[j]]
       

    



    
    

 
    
        
  