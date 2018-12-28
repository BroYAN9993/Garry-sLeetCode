"""
Example 1:

Input: "42"
Output: 42

Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        sign = 1
        num = 0
        start, end = -1, -1
        for i in range(len(str)):
            if str[i] != ' ':
                if str[i] == '+':
                    start = i + 1
                elif str[i] == '-':
                    start = i + 1
                    sign = -1
                elif str[i] in nums:
                    start = i
                else:
                    return 0
                break
        if start == -1 or start >= len(str):
            return 0
        for i in range(start, len(str)):
            if str[i] not in nums:
                end = i
                break
        if end == -1:
            end = len(str)
        for i in range(start, end):
            num = num * 10 + nums[str[i]]
        num *= sign
        if num >= -2 ** 31 and num <= 2 ** 31 - 1:
            return num
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return 2 ** 31 - 1