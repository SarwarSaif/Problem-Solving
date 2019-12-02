# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:57:35 2018

@author: majaa
"""

def LCS_Strings(X,Y):
    #Get the length of X and Y
    m,n=len(X),len(Y)
    
    #return If we reach to the end of either sequence
    if m==0 or n==0 :
        return ""
    
    ###CONSTRUCT A KEY
    key1 = str(m-1) +"|"+ str(n)
    key2 = str(m) +"|"+ str(n-1)
    
    if X[m-1]==Y[n-1]:
        return LCS_Strings(X[:m-1] , Y[:n-1]) + X[m-1]
           
    if key1 > key2:
        return LCS_Strings(X[:m-1] , Y[:n])
    
    else:
        return LCS_Strings(X[:m] , Y[:n-1])
    


def LCS_Length(X,Y):
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
            lookup[key] = LCS_Length(X[:m-1] , Y[:n-1]) + 1
            
        #else if last character don't match , use recursion again and get the max value     
        else:
            lookup[key] = max( LCS_Length(X[:m] , Y[:n-1]), LCS_Length(X[:m-1] , Y[:n]) )
    
    ##IF key already seen then return the value from the dictionary.......    
    return lookup[key]

if __name__ == '__main__':
    X, Y = input(),input()
    global lookup
    lookup={}
    print("Length of LCS is ",LCS_Length(X,Y))
    print(LCS_Strings(X,Y))
    
    
    
    
    