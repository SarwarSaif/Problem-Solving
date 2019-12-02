# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:57:35 2018

@author: majaa

ABCBDAB

BDCABA
"""
import array as arr

def LCS_Strings(X,Y):
    #Get the length of X and Y
    m,n=len(X),len(Y)
    
    #return If we reach to the end of either sequence
    if m==0 or n==0 :
        
        j = [""]
        print("ashc")
        return j
    
   
    if X[m-1] == Y[n-1]:
        
        
        lcs.append( LCS_Strings(X[:m-1] , Y[:n-1]) )
        
        for i in range( len(lcs) ):
            #print(type(lcs[i]))
            #print(type(X[m - 1]))
            lcs[i]= "".join(lcs[i] ) +  X[m - 1] 
			
        return lcs
    
    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS_Strings(X[:m-1] , Y[:n])
    
    if lookup[m][n - 1] > lookup[m - 1][n]:
        return LCS_Strings(X[:m] , Y[:n-1])
    
    
    top= LCS_Strings(X[:m-1] , Y[:n]) 
    left= LCS_Strings(X[:m] , Y[:n-1]) 
    print("top and left : ",top,left)
    return top
    
   
 

def LCS_Length(X,Y):
    m,n=len(X),len(Y)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                lookup[i][j] = lookup[i-1][j-1]+1
            else:
                lookup[i][j]= max(lookup[i-1][j], lookup[i][j-1])


if __name__ == '__main__':
    X, Y = input(),input()
    global lookup
    lookup=[[0 for x in range(len(Y)+1)] for y in range(len(X)+1)] 
    lList=[]
    global lcs
    #flag=0
    lcs=[]
    print(lookup)
    maxL = LCS_Length(X,Y)
    
    lList.append(LCS_Strings(X,Y) )
    print(lList)
    #print("Length of LCS is ",maxL)
    #print(LCS_Strings(X,Y))
    """
    for k in lookup.keys():
        if lookup[k]== 4:
            lList.append(k.split("|"))
    print(lList)
    #print(lList[0].split("|"))
    """
    
    
    