"""
    题目描述:
        给你一个整数数组 nums ，
        请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        子数组 是数组中的一个连续部分。
    
    链接: https://leetcode-cn.com/problems/maximum-subarray/
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            动态规划:
            1. dp[i]: 以第 i 个元素为最后一个元素的最大和；
            2. dp[i] = max(nums[i], dp[i-1] + nums[i])
        """
        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)