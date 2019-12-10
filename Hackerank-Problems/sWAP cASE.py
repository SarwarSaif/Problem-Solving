# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 11:22:23 2018

@author: majaa
"""
"""
#First Type 
print ( ''.join([i.lower() if i.isupper() else i.upper() for i in input()]) )
"""
#Second type
#print("".join(map(str.swapcase, input())))
#Third type
#print(input().swapcase())

"""
    This is an axample of list comprehension.
    It just go straight to iterating over "raw_input"
"""

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)