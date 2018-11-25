# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 03:39:50 2018

@author: dontworry
"""

def gensubset(L):
    if len(L)==0:
        return [[]]
    smaller=gensubset(L[:-1])
    res=[]
    key=L[-1:]
    for small in smaller:
        res.append(key+small)
        
    return smaller+res
L=[1,2,3,4] 
a=gensubset(L)
print (a)  