a = 9 
b = 2

## Normal way
temp = a
a = b
b = temp
print("Swaped values ", a, b)

## Another way 
a = a + b
b = a - b
a = a - b 
print("Swaped values ", a, b)

## Another way without spending extra bits using XOR
a = a ^ b 
b = a ^ b
a = a ^ b 
print("Swaped values ", a, b)

## Python's way using Rotation Rot_Two
a, b = b, a
print("Swaped values ", a, b)

