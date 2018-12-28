"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        p1, p2, p3 = l1, l2, pre
        while p1 and p2:
            if p1.val < p2.val:
                temp = p1.next
                p1.next = None
                p3.next = p1
                p3 = p3.next
                p1 = temp
            else:
                temp = p2.next
                p2.next = None
                p3.next = p2
                p3 = p3.next
                p2 = temp
        if p1:
            p3.next = p1
        else:
            p3.next = p2
        return pre.next
