# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 02:02:40 2018

@author: majaa
"""
def printNumber(n):
    for i in range(1,n+1):
        print(i, end = '')

if __name__ == '__main__' :
    n=int(input())
    printNumber(n)
    
    