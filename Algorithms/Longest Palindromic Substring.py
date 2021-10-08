import time
def longestPalindrome2( s):
    res = ""
    if(s==s[::-1]): # Check if the String itself a palindrome
        res=s
        print("well",time.time()-t)
        
    else:
        print("Etar vitor")
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
        
    return s[l+1:r]



def findLongestPalindromicString(text): 
    N = len(text) 
    if N == 0: 
        return
    N = 2*N+1    # Position count 
    L = [0] * N 
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition 
    R = 2     # centerRightPosition 
    i = 0    # currentRightPosition 
    iMirror = 0     # currentLeftPosition 
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
   
    # Uncomment it to print LPS Length array 
    # printf("%d %d ", L[0], L[1]); 
    for i in range(2,N): 
       
        # get currentLeftPosition iMirror for currentRightPosition i 
        iMirror = 2*C-i 
        L[i] = 0
        diff = R - i 
        # If currentRightPosition i is within centerRightPosition R 
        if diff > 0: 
            L[i] = min(L[iMirror], diff) 
   
        # Attempt to expand palindrome centered at currentRightPosition i 
        # Here for odd positions, we compare characters and 
        # if match then increment LPS Length by ONE 
        # If even position, we just increment LPS by ONE without 
        # any character comparison 
        try: 
            while ((i+L[i]) < N and (i-L[i]) > 0) and (((i+L[i]+1) % 2 == 0) or (text[(i+L[i]+1)/2] == text[(i-L[i]-1)/2])): 
                L[i]+=1
        except Exception as e: 
            pass
   
        if L[i] > maxLPSLength:        # Track maxLPSLength 
            maxLPSLength = L[i] 
            maxLPSCenterPosition = i 
   
        # If palindrome centered at currentRightPosition i 
        # expand beyond centerRightPosition R, 
        # adjust centerPosition C based on expanded palindrome. 
        if i + L[i] > R: 
            C = i 
            R = i + L[i] 
   
    # Uncomment it to print LPS Length array 
    # printf("%d ", L[i]); 
    start = (maxLPSCenterPosition - maxLPSLength) / 2
    end = start + maxLPSLength - 1
    print ("LPS of string is " , text , " : ") 
    print (text[int(start):int(end)+1])
     



def longestPalSubstr(string): 
    maxLength = 1
  
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
  
    # One by one consider every character as center point of  
    # even and length palindromes 
    for i in range(1, length): 
        # Find the longest even length palindrome with center 
    # points as i-1 and i. 
        low = i - 1
        high = i 
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
        # Find the longest odd length palindrome with center  
        # point as i 
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            if high - low + 1 > maxLength: 
                start = low 
                maxLength = high - low + 1
            low -= 1
            high += 1
  
    print ("Longest palindrome substring is:")
    print (string[start:start + maxLength] )
  
    return maxLength 

def longestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        beg=0
        maxLen=0
        if(len(s)<1):
            print("1",s)
            return ""
        elif(len(s)==1):
            print("2",s)
            return s
        elif(len(set(s))==1):
            print("3",s)
            return s
        else:
            for i in range(len(s)):
                print("4",s,i,i,beg,maxLen)
                beg,maxLen = extend(s,i,i,beg,maxLen)
                print("5",s,i,i+1,beg,maxLen)
                beg,maxLen =  extend(s,i,i+1,beg,maxLen)
        return s[beg:beg+maxLen]

def longestPalindrome1( s):
        """
        :type s: str
        :rtype: str
        """
        beg=0
        maxLen=0
        
        if(len(s)<1):
            print("1",s)
            return ""
        elif(len(s)==1):
            print("2",s)
            return s
        elif(len(set(s))==1):
            print("3",s)
            return s
            
        else:
            for i in range(len(s)):
                print("4",s,i,i,beg,maxLen)
                beg,maxLen = extend(s,i,i,beg,maxLen)
                print("5",s,i,i+1,beg,maxLen)
                beg,maxLen =  extend(s,i,i+1,beg,maxLen)
        return s[beg:beg+maxLen]
    
def extend(s,start,end,beg,maxLen):
        while(start>=0 and end<len(s) and s[start]==s[end]):
            start=start-1
            end=end+1
            print("#6 ",s,start,end,beg,maxLen)
        if(maxLen<end-start-1):
            beg=start+1
            maxLen=end-start-1
            print("#7 ",s,start,end,beg,maxLen)
        return beg,maxLen


def longest(s):
    List1=s
    List2=s[len(s)::-1]
    #[x1 - x2 for (x1, x2) in zip(List1, List2)]
    print(List1)
    print(List2)
    #for i in range(len(s)):
        #if(List1[i]==List2[i]):
            
    
# Driver program to test above functions 
string = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111..."
t1=time.time()
#string="forgeeksskeegfor"
st=longestPalindrome2(string)
print("Time: ",time.time()-t1)
print ("Longest palindromic substring is:",st)
t2=time.time()
#print (longestPalindrome(string) )
print(time.time()-t2)
#print ("Length is: " + str(longestPalSubstr(string)) )
  











