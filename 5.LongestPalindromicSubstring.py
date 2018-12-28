"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start, end = 0, 0
        for i in range(len(s)):
            length = max(self.lengthOfSubstring(s, i, i), self.lengthOfSubstring(s, i, i + 1))
            if length > end - start:
                start = i - (length - 1) / 2
                end = i + length / 2
        return s[start: end + 1]

    def lengthOfSubstring(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1