"""
    题目描述:
        给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        子数组 是数组中的一个连续部分。
    
    进阶: 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

    链接: https://leetcode-cn.com/problems/maximum-subarray/
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            暴力思路:
                两层 for 循环遍历所有的可能解，找出最大值。

            贪心的思路:
                局部最优:
                    当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”。
                从局部最优可以推出全局最优，选择最大“连续和”。

                关键在于: 不能让“连续和”为负数的时候加上下一个元素，而不是 不让“连续和”加上一个负数。
        """
        maxSum, curSum = nums[0], 0

        for num in nums:
            curSum += num

            if curSum > maxSum:
                maxSum = curSum

            if curSum < 0:
                # 可能全是负数，因此这个要放在后面
                curSum = 0
        
        return maxSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
            动态规划思路:
                1. dp数组及下标含义:
                    dp[i] 表示 包括下标i的最大连续子序列和；
                2. 递推公式:
                    dp[i]只有两个方向可以推出来:
                        dp[i - 1] + nums[i]，即: nums[i]加入当前连续子序列和
                        nums[i]，即: 从头开始计算当前连续子序列和

                    一定是取最大的，所以dp[i] = max(dp[i - 1] + nums[i], nums[i]);
                3. 初始化 dp 数组:
                    初始 dp[0] = nums[0]，即为本身的值
                4. 确定遍历方向:
                    dp[i] 由 dp[i-1] 决定，因此从前往后遍历
            
                进一步，选择最大的子序列和，只用保存 dp[i-1] 和 maxSum 即可
        """
        maxSum, dp_pre = nums[0], nums[0]

        for idx in range(1, len(nums)):
            dp_cur = max(dp_pre+nums[idx], nums[idx])
            maxSum = max(dp_cur, maxSum)
            dp_pre = dp_cur

        return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        """
            分治思路: 线段树思路
        """