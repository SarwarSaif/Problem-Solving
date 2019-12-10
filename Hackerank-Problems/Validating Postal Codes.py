# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:27:55 2019

@author: majaa
"""

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.



import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) )

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)