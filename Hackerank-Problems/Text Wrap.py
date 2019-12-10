# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:57:35 2018

@author: majaa
"""

import textwrap
def wrap(string, max_width):
    print( "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)]) )
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)