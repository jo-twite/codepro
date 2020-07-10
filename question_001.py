import math

'''
You are given two linked-lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
   
    def list_to_int(self):
        (y, iter, i) = (0, self, 0)
        while(iter != None):
            y += iter.val * (10 ** i)
            iter = iter.next
            i += 1
        return y
    
    def int_to_list(self, n):
        a = [int(x) for x in str(n)]
        list = ListNode(a[0])
        iter = list
        del a[0]
        for i in a:
            iter.next = ListNode(i)
            iter = iter.next
        return list    

class Solution:

    def addTwoNumbers(self, l1, l2, c = 0):
        return ListNode(None).int_to_list(l1.list_to_int() + l2.list_to_int())        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
      print(result.val, "->")
      result = result.next
# 7 0 8
