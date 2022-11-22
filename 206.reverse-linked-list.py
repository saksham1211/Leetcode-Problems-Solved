#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reversell(head):
    if  head.next is None:
        return head

    new_head=reversell(head.next)
    new_tail=head.next
    new_tail.next=head
    head.next=None

    return new_head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        return reversell(head)
        
# @lc code=end

