# @before-stub-for-debug-begin
from python3problem234 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''revsere the second half of the LL and comapre the elements.'''
        
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        left, right=head, prev

        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next

        return True

        

# @lc code=end

