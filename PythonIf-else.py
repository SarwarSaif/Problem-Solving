# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 23:10:19 2018

@author: majaa
"""

N=int(input())
check=N%2
if (check>0):
    print("Weird")
elif (not check and N>=2 and N<=5):
    print("Not Weird")
elif (not check and N>=6 and N<=20):
    print("Weird")
elif (not check and N>20):
    print("Not Weird")
    