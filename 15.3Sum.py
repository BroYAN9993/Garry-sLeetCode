"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        solu = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            dict = {}
            while j < len(nums):
                num = -nums[i] - nums[j]
                if num not in dict:
                    dict[nums[j]] = j
                    j += 1
                else:
                    solu.append([nums[i], num, nums[j]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
        return solu