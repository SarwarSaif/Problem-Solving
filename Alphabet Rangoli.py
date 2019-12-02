# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:49:31 2019

@author: majaa
"""
#import string ### import string library
#import time

def print_rangoli(size):
    #alpha = string.ascii_lowercase[0:size] ### store alpha with lower case alphabets
    from string import ascii_lowercase as alpha
    L = [] ## Create a list to store values per line
    for i in range (n): ### Loop n times
        s = "-".join(alpha[i:n]) ### Join the letter from i to n using '-'; ex: 'a-b-c-d-e'  
        #print((s[::-1] + s[1:]).center((4*n)-3, "-"))
        L.append( (s[::-1] + s[1:]).center(4*n-3, "-"))
        """
        (s[::-1] + s[1:]) this line used to make 'e-d-c-b-a-b-c-d-e' , 'e-d-c-b-c-d-e' 
        and then its centered using '-' to (4*n)-3 letters
        """
    print('\n'.join(L[:0:-1]+L)) ## "" L is practically middle to the end of rangoli. So first revert it from last to after the middle and add them
            
if __name__ == "__main__":
        
    n = int(input())    
    #tic = time.time()   
    print_rangoli(n)    
    #toc = time.time()
    #print("Ok")