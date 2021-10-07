### Problem link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    # get the length of the string
    n = len(string)
    # If length is 1, print the string
    if n==1:
        print(string)
    else:
        # Divide the string into n/k substrings
        for i in range(0, n, k):
            substring = string[i:i+k]
            # As order of the subsequence matters, we can use dict to remove duplicate characters
            result = "".join(dict.fromkeys(substring))
            print(result)
        if (n%k!=0):
            #print the excess part
            left_substring = string[(n-(n%k)):n]
            result = "".join(dict.fromkeys(left_substring))
            print(result)      

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
