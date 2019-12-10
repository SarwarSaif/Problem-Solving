"""
Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable.
Lists are dynamic.
"""

my_list = [29, 45, 67, 89]

### use append
my_list.append(45)
print(my_list)

my_list.append([56, 67, 55])
print(my_list)

## use extend 
my_list.extend([89, 34])
print(my_list)

## use insert
my_list.insert(1, 454)
print(my_list)


my_list.insert(7, 254)
print(my_list)

my_list[6].insert(1, 254)
print(my_list)

## use remove
my_list.remove(254)
print(my_list)

## use pop
my_list.pop(1)
print(my_list)

my_list.pop()
print(my_list)

## use del
del my_list[4:]
print(my_list)

## use built-in function
print(min(my_list))
print(max(my_list))
print(sum(my_list))
my_list.sort()
print(my_list)