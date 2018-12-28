"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) < 1:
            return []
        ans = ['']
        for i in range(len(digits)):
            tem = []
            for s1 in ans:
                for s2 in mapp[digits[i]]:
                    tem.append(s1 + s2)
            ans = tem
        return ans