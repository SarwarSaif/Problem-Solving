# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 02:30:19 2018

@author: majaa
"""

import re

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

for i in range(int(input())):
    print(isvalidregex(input()))