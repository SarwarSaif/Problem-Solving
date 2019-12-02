# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:10:50 2018

@author: majaa
"""

if __name__=='__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr=[[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) != n)]
"""
1

1

1

2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
    """
    #print([[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) != n)])
    print(arr)
    """
    python x = int ( raw_input()) y = int ( raw_input()) 
    n = int ( raw_input()) 
    print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]
    p = 0 for i in range ( x + 1 ) : 
        for j in range( y + 1): 
            if i+j != n: 
                ar.append([]) ar[p] = [ i , j ] 
                p+=1 
    print ar 
    
    """