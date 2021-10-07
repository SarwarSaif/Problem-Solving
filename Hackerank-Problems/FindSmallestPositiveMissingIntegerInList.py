# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # Smallest positive integer for a negative integer greater than 0 would be always 1
    # So if there is any negative integer in the list return 0
    # Lets sort the list at first
    # If all the values are negative
    m = max(set(A))
    if m<1:
        return 1
    #sorted_A = sorted(set(A), reverse=False)
    
    #print(sorted_A)
    l = [0] * m # create a list of 0 upto max value
    print(l)
    for n in set(A):
        l[n-1]=1
    print(l.index(0))
    return l.index(0)+1
    #pass
