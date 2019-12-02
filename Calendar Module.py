# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:20:23 2018

@author: majaa
"""
import calendar
if __name__ == '__main__':
    
    user_input = input().split()
    m = int(user_input[0])
    d = int(user_input[1])
    y = int(user_input[2])
    print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
    #first calendar.weekday(y,m,d) returns the number of the day e.g: returns 6 for sunday
    #calendar.day_name returns the days name in an array
    #list(calendar.day_name) returns ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    #then we get list(calendar.day_name)[6] we get the day name in 6th index
    #then turn them into upper case letters by apply ".upper()" at the end
    
    #print(calendar.weekday(y, m, d))
    #print(list(calendar.day_name)[calendar.weekday(y, m, d)])
    