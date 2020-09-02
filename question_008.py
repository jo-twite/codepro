"""
You are given an array of integers.
Return an array of the same size where
the element at each index is the product of
all the elements in the original array except for
the element at that index.

For example, an input of [1, 2, 3, 4, 5]
should return [120, 60, 40, 30, 24].

You cannot use division in this problem.
"""

def products(nums):
    n = len(nums)
    v = n * [1]
    for i in range(n):
        for j in range(n):
            if j != i:
                v[i] *= nums[j]
    return v
              

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
