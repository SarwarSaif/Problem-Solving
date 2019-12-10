# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:02:37 2018

@author: majaa
"""
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
    
