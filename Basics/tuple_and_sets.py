"""
A tuple is a sequence of immutable Python objects. 
Tuples are sequences, just like lists. 
The differences between tuples and lists are, 
the tuples cannot be changed unlike lists and tuples use parentheses, 
whereas lists use square brackets.

Tuples are memory efficient and easy to debug 
but slower in case of appending but faster in case of iteration
"""
my_tuple = (45, 34, 23)
print(my_tuple)

### set is not ordered and not sorted but unique (no duplicates) values
### set uses Hash to make it faster
### set doesn't support indexes
my_set = {45, 43, 12}
print(my_set)
