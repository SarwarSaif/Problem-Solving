# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:45:47 2018

@author: majaa
"""

def split_and_join(line):
    line=list ( line.split(" ") )
    return "-".join(line)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)