# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:10:15 2018

@author: majaa
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))[:n]
    print(integer_list)
    t=tuple(integer_list)
    print(hash(t))