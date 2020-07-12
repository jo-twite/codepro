"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
"""

def sortNums(nums):
    if len(nums) == 0:
        return []
    m = min(nums)
    nums_k = list(filter(lambda a: a != m, nums))
    return (len(nums) - len(nums_k)) * [m] + sortNums(nums_k)


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
