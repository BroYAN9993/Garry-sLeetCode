"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        ans = 2 ** 31 - 1
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            csum = nums[i] + nums[l] + nums[r]
            if csum == target:
                return target
            while r - l > 1:
                if csum == target:
                    return target
                if abs(target - nums[i] - nums[l + 1] - nums[r]) < abs(target - nums[i] - nums[l] - nums[r - 1]):
                    l += 1
                else:
                    r -= 1
                tsum = nums[i] + nums[l] + nums[r]
                if abs(tsum - target) < abs(csum - target):
                    csum = tsum
            if abs(csum - target) < abs(ans - target):
                ans = csum
        return ans