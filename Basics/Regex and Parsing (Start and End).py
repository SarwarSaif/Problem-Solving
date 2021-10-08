### Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
S = input()
k = input()
# Given string S and k
# Find all possible indices of the start and end of string k in S
# Check if len is same and equal
pattern = re.compile(k)
m = pattern.search(S)
if not m: print("(-1, -1)") # While there is no pattern
while m: # When there is a pattern.
    print("({0}, {1})".format(m.start(),m.end()-1))
    m = pattern.search(S,m.start()+1) # Search again by starting from next start
    
# Regex and parsing
# import re
# m = re.search(r'\d+', '101234')
"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.
https://www.guru99.com/python-regular-expressions-complete-tutorial.html
https://stackoverflow.com/questions/32680030/match-text-between-two-strings-with-regular-expression
"""
