#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from audioop import lin2adpcm


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in (list1, list2):
            return list1 or list2

        current=temp=ListNode(0)

        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next

            else:
                current.next=list2
                list2=list2.next

            current=current.next

        current.next=list1 or list2

        return temp.next





# @lc code=end

