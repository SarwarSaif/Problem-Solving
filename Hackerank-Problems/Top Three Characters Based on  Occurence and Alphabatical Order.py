### Problem link: https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    # Create a occurence counter for the string
    occurance_counter = Counter(s)
    # Sort the items in the occurance dict using "key = lambda x: (-x[1], x[0])" which allows to reverse sort using the occurance count and then sort by alphabet. 
    for key, val in sorted(occurance_counter.items(), key= lambda x: (-x[1],x[0]))[:3]:
        print(key, val)
