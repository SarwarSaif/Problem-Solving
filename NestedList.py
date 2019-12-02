# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:30:26 2018

@author: majaa
"""


if __name__ == '__main__':
    marksheet=[]
    """
    for _ in range(int(input())):
        marksheet.append([input(),float(input())])
        
    """
    
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    second_lowest= sorted(list(set([marks for name, marks in marksheet])))[1]
    #list index started from 1
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_lowest]))
    #print(sorted(marksheet))
    
"""  
Testcase 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Testcase 2
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
  
    #initialising an empty list!
marksheet = [] 

#iterating through a for loop starting from zero, to some user input(default type string) 
  - that is converted to int
for i in range(0,int(input())): 
    #appending user input(some string) and another user input(a float value) as 
    a list to marksheet
    marksheet.append([raw_input(), float(input())]) 

#[marks for name, marks in marksheet] - get all marks from list
#set([marks for name, marks in marksheet]) - getting unique marks
#list(set([marks for name, marks in marksheet])) - converting it back to list
#sorting the result in decending order with reverse=True and getting the value as 
first index which would be the second largest.
second_highest = sorted(list(set([marks for name, marks in marksheet])),reverse=True)[1] 

#printing the name and mark of student that has the second largest mark by iterating through the sorted list.
#If the condition matches, the result list is appended to tuple  -`
[a for a,b in sorted(marksheet) if b == second_highest])` 
#now join the list with \n - newline to print name and mark of student with second 
    largest mark
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))





"""