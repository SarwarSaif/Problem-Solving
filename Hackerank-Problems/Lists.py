# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:35:38 2018

@author: majaa
"""
"""
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

if __name__ == '__main__' :
    
    arr=list()
    for i in range(int(input())):
        input_list=list(input().strip().split())
        #print(input_list[0])
        if(input_list[0]=='insert'):
            arr.insert(int(input_list[1]), int(input_list[2]))
        elif(input_list[0]=='print'):
            print(arr)
        elif(input_list[0]=='remove'):
            arr.remove(int(input_list[1]))
        elif(input_list[0]=='append'):   
            arr.append(int(input_list[1]))
        elif(input_list[0]=='sort'): 
            arr.sort()
        elif(input_list[0]=='pop'): 
            arr.pop()
        elif(input_list[0]=='reverse'):     
            arr.reverse()
            