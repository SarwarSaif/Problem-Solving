from math import sqrt, ceil
num = int(input("Enter a number to check if it is Prime? "))

for i in range(2, ceil(sqrt(num))):
    if num % i == 0:
        print("Not Prime ")
        break
else:
    print("Prime ")