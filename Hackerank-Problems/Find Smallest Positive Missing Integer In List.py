def solution(A):
    # write your code in Python 3.6
    # Smallest positive integer for a negative integer greater than 0 would be always 1 if 1 is not in the list
    
    # Get the maximum value in the list
    m = max(A) 
    if m<1: # If all the values are negative
        return 1
    # If all values are not negative
    else:
      # Create a list of all 0s where key is the numbers in the list
      l = [0] * m # create a list of 0 upto max value
    #sorted_A = sorted(set(A), reverse=False)
    
    #print(sorted_A)
    
    print(l)
    for n in set(A):
      # We need to track smallest positive integer
      if n>0:
        l[n-1]=1
    # If there is a missing integer between 1 to max(A)
    if sum(l)<m: # 
      missing_val = l.index(0)+1
    else: # There is no missing integer between 1 to max(A), so the smallest integer will be max(A)+1
      missing_val=m+1
    print(missing_val)
    return missing_val
    #pass

#### TEST CASES ####
A = [1, 3, 4, 6, 1, 2]
solution(A)
A = [-3, -1, -4]
solution(A)
A = [1, 3, 4, 6, -1, 2]
solution(A)
A = [1, 1, -1, 3, 4, 7, 9, 8, -8, 10, 6, -1, 2, 5]
solution(A)
A = [1, 2, 3]
solution(A)


