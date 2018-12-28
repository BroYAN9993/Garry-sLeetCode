"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        slow = pre
        if pre.next and pre.next.next:
            fast = pre.next.next
        else:
            return head
        while fast:
            temp = fast.next
            fast.next = slow.next
            slow.next = fast
            slow = fast.next
            slow.next = temp
            if slow.next:
                fast = slow.next.next
            else:
                break
        return pre.next