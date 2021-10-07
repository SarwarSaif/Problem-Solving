### Problem Link: https://www.hackerrank.com/challenges/collections-counter/problem
def money_earned(X, shoe_left, N, desired_size, amount):
    # your code goes here
    #print(X, shoe_left, N, desired_size, amount)
    # If desired shoe size is available
    if shoe_left[desired_size]:
        # Sustract 1 shoe
        shoe_left[desired_size]=shoe_left[desired_size]-1
        return amount
    else: # If shoe size is not available no money earned. Thus return 0
        return 0
    
if __name__ == '__main__':
    X = int(input())
    shoe_size_list = map(int, input().split(" "))
    shoe_left = Counter(shoe_size_list)
    N = int(input())
    total_money_earned=0
    for i in range(0, N):
        lines = input().split(" ")
        
        desired_size, amount = int(lines[0]), int(lines[1])
        
        #print(X, shoe_size_list, N, desired_size, amount, shoe_left)
    
        total_money_earned = total_money_earned+money_earned(X, shoe_left, N, desired_size, amount)
    print(total_money_earned)
    
    
    ### TEST CASES
    """
    Input (stdin)
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

    Expected Output
200
    """
