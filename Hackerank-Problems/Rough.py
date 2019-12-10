# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:40:38 2018

@author: majaa
"""

from datetime import datetime

FMT = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())) :
    t1 = datetime.strptime(input(), FMT)
    t2 = datetime.strptime(input(), FMT)
    print(abs(int((t1-t2).total_seconds())))
    #print((t1-t2))