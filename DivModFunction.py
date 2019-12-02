# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:35:21 2018

@author: majaa
"""
if __name__ == '__main__':
    
    a=int(input())
    b=int(input())
    m,n=divmod(a,b)
    print(m)
    print(n)
    print ("(",m,", ",n,")",sep="")