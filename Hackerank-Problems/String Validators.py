# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:24:29 2018

@author: majaa
"""

if __name__ == '__main__':
    s = input()
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print (any(method(c) for c in s))
    
    
"""
In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""

"""
I see eval as a hacky solution. eval should only ever be used with caution and there's usually 
a better solution. It's fragile (you may accidentally create invalid code) and can be 
dangerous (can offer ways for malicious code to be injected). 
It's also significantly slower, because the python code created by eval has to be 
recompiled on every iteration.

You can do this more cleanly and safely a couple of ways. You could use getattr(). 
But I prefer just using function references. 
Remember that class methods are just functions with an object as the 
first parameter - true in any OO language but directly visible and usable from Python.

for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print any(method(c) for c in s)
or

t = type(s)
for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print any(method(c) for c in s)
Eval is something to use for a quick hack but it's not a good habit.

"""