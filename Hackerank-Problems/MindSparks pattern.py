# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:26:55 2018

@author: majaa
"""

thickness = int(input()) #This must be an odd number
c = 'M'

#Top tri angle
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c )

#Middle belt
for i in range(thickness//2):
    print( (c*thickness*3).ljust(thickness*3) )
    
#Bottom tri angle
for i in range(thickness):
    print(  (c+(c*(thickness-i-1)).ljust(thickness-1)).rjust(thickness*3)  )