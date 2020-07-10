
""" A palindrome is a sequence of characters that
reads the same backwards and forwards.
Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""
def isPalindrome(s):
    if(len(s) == 1):
        return True
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

class Solution: 
    def longestPalindrome(self, s):
        if isPalindrome(s):
            return s
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                if isPalindrome(s[j: len(s) - i + j]):
                    return s[j: len(s) -i + j]
    
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar