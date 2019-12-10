# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 01:13:59 2018

@author: majaa
"""
if __name__ == '__main__':
    n, m = map(int,input().split())
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))