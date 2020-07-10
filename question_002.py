"""
Given a string, find the length of the longest substring without repeating characters.
Can you find the solution in linear time?
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or s == None:
            return 0
        return 1 + Solution().lengthOfLongestSubstring(s.replace(s[0], ''))


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
