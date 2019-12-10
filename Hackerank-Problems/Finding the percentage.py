# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:04:24 2018

@author: majaa
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #to assign multiple values we use * before *line
        #print(*line)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print("{0:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))