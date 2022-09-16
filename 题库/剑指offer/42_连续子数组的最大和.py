"""
    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。
    求所有子数组的和的最大值。

    要求时间复杂度为O(n)。
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """dp
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        
        return max(nums)
    
    def maxSubArray(self, nums: List[int]) -> int:
        """贪心
            当前最连续和为负数时丢弃
        """
        curSum, maxSum = 0, -float('inf')  # nums 中有全负数的情况

        for num in nums:
            curSum += num

            maxSum = max(maxSum, curSum)  # 先比较再重置

            if curSum < 0:
                curSum = 0  # 下个子序列从头开始
            
        return maxSum
