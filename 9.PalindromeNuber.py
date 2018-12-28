"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        if x < 10:
            return True
        rev = 0
        while rev < x:
            rev = rev * 10 + x % 10
            x /= 10
            if rev == x or rev == x / 10:
                return True
        return False