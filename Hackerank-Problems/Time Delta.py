# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:39:50 2018

@author: majaa
"""

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    return abs(t1-t2)
if __name__ == '__main__':
    fptr = open('G:\CSE 4.1 Spring 2k18\CoderHoteChai\Hackerank practice problems\Python\timeDelta.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
