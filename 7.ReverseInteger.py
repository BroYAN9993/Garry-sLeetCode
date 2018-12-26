"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        while x:
            pop = x % 10
            x /= 10
            if rev > (2 ** 31 - 1) / 10 or (rev == (2 ** 31 - 1) / 10 and pop > 7):
                return 0
            if rev < -2 ** 31 / 10 or (rev == -2 ** 31 / 10 and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev