"""
Given two arrays, write a function to compute their intersection -
the intersection means the numbers that are in both arrays.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.
"""

class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2
        v = []
        for i in a:
            if i in b:
                v.append(i)
                a = [x for x in a if x != i]
        return v

        

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]