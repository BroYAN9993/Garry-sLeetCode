"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        end = len(strs[0])
        pre = strs[0]
        for str in strs:
            end = min(end, len(str))
            while end > 0 and pre[: end] != str[: end]:
                end -= 1
            if end == 0:
                return ''
        return pre[: end]
