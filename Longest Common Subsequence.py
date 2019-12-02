# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:52:36 2018

@author: majaa


ABCBDAB

BDCABA

"""


def LCS(X,Y,lookup):
    #Get the length of X and Y
    m,n=len(X),len(Y)
    
    #return If we reach to the end of either sequence
    if m==0 or n==0 :
        return 0
    
    ###CONSTRUCT A KEY
    key = str(m) +"|"+ str(n)
    
    #If key have not already seen then,
    #store the unique key
    if key not in lookup.keys():
        #else if the end of two sequence matches check for next two 
        if X[m-1]==Y[n-1]:
            lookup[key] = LCS(X[:m-1] , Y[:n-1], lookup) + 1
            
        #else if last character don't match , use recursion again and get the max value     
        else:
            lookup[key] = max( LCS(X[:m] , Y[:n-1], lookup), LCS(X[:m-1] , Y[:n], lookup) )
    
    ##IF key already seen then return the value from the dictionary.......    
    return lookup[key]

if __name__ == '__main__':
    X, Y = input(),input()
    lookup={}
    print("Length of LCS is ",LCS(X,Y,lookup))
    
    
    
    
    
    