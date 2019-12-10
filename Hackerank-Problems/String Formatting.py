# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 01:25:24 2018

@author: majaa
"""

#to learn more about formatting visit "https://pyformat.info/"
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    print(width)
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width) )
        print("{0:{width}d} ".format(i, width=width))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
