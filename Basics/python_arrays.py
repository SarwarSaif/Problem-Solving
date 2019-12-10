from array import *

vals = array('i', [5, 6, 3, -45])

copied_vals = array(vals.typecode, (a for a in vals))

for val in copied_vals:
    print(val) 


new_arr = array('i', [])

n = int(input("Enter the length of the array: "))

for i in range(n):
    new_arr.append(int(input("Enter a value: ")))

print(new_arr)

#### Doesn't support multi-dimensional array