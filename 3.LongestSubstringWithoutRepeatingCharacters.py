"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        map = {}
        length = 0
        index = 0
        while index < len(s):
            if s[index] in map:
                length = max(len(map), length)
                index = map[s[index]] + 1
                map.clear()
            else:
                map[s[index]] = index
                index += 1
        if len(map):
            length = max(len(map), length)
        return length