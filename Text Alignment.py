# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:56:13 2018

@author: majaa
"""

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    
    #print(c*i) by multiplying i with c we get i no of H

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    #if u give even number like 10 and use center eith 5string then "  HHHHH   " 


#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    


#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    


#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


    