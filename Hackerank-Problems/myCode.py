# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 18:22:37 2018

@author: majaa
"""

import sys

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
   
    for i, v in enumerate(argv):
        
        f = open(sys.argv[1],"r")
        contents = f.read()
        f.close()
        s=contents
        lps = ""
        #flag=0
        #A=reversed(s[:len(s)-3])
        if(s[len(s)-4::-1]==s[0:len(s)-3]):
          lps=s
        else:
          for i in range(len(s)):
              # odd case, like "343"
              tmp = expand(s, i, i)
              if len(tmp) > len(lps):
                  lps = tmp
              # even case, like "3443"
              tmp = expand(s, i, i+1)
              if len(tmp) > len(lps):
                  lps = tmp
        
        print(lps)
        
        
def expand(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left+1:right]

if __name__ == '__main__':
    main(sys.argv[1:])
