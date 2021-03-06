"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapp = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for p in s:
            if p not in mapp:
                stack.append(p)
            elif stack and mapp[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if stack == [] else False
