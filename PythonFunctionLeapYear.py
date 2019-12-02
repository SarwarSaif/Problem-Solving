# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:52:09 2018

@author: majaa
"""

def is_leap(year):
    leap=False
    
    if (year%4==0):
        leap=True
        if(year%100==0):
            leap=False
            if(year%400==0):
                leap=True
    
    return leap

year=int(input())
print(is_leap(year))