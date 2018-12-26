"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = head
        carry = 0
        while p1 or p2:
            if p1 and p2:
                sum = p1.val + p2.val + carry
                carry = sum / 10
                sum -= carry * 10
                p3.next = ListNode(sum)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 is None:
                sum = p2.val + carry
                carry = sum / 10
                sum -= carry * 10
                p3.next = ListNode(sum)
                p2 = p2.next
                p3 = p3.next
            elif p2 is None:
                sum = p1.val + carry
                carry = sum / 10
                sum -= carry * 10
                p3.next = ListNode(sum)
                p1 = p1.next
                p3 = p3.next
        if carry:
            p3.next = ListNode(carry)
        return head.next