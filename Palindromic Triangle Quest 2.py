# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 02:04:57 2018

@author: majaa
"""

if __name__ == '__main__':
    
    for i in range(1,int(input())+1): 
        print(pow(((pow(10,i)-1)//9),2))
        
"""
just use math's trick:

pow(1,2)=1 pow(11,2)=121 pow(111,2)=12321 pow(1111,2)=1234321 
and so on code will be 
:: for i in range(1,int(input())+1): print(pow(((pow(10,i)-1)//9),2))

OR,
for i in range(0,int(raw_input())): 
print [1, 121, 12321, 1234321, 123454321,
 12345654321, 1234567654321, 123456787654321,
 12345678987654321, 12345678910987654321][i]

"""