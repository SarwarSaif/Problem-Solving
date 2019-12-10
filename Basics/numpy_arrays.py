import numpy as np 

"""
Some Numpy functions:
array(), linspace(), logspace(),
arange(), zeros(), ones()
"""
arr = np.array([1, 3 , 1 , 6])
print(arr)

lin_arr = np.linspace(1, 10, 3) #the number of parts = 3 byDefault 50
print(lin_arr)

arange_arr = np.arange(1, 10, 3) # the number of steps = 3
print(arange_arr)

log_arr = np.logspace(1, 40, 5)
print(log_arr)

zeros_arr = np.zeros([10, 2], int)
print(zeros_arr)

## Copy a array in different location
copied_arr = log_arr.view() # Shallow copy: It changes if parent array is affected
print(copied_arr)
print(id(log_arr) == id(copied_arr))

## DeepCopy: It doesn't change with parent array chnges
deep_copied_array = log_arr.copy() # Deep copy