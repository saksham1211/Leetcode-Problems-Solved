#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        temp=dummy
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next

        return dummy.next










# @lc code=end

