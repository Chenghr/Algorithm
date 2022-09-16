"""
    题目描述:
        给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。
        请你从 nums 中找出并返回总和为 target 的元素组合的个数。

        题目数据保证答案符合 32 位整数范围。

        请注意，顺序不同的序列被视作不同的组合。

    链接: https://leetcode-cn.com/problems/combination-sum-iv
"""

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
            完全背包问题的排列组合求解；

            1. dp[j]: 装满容量为 j 的背包的最大排列数；
            2. dp[j] += dp[j - nums[i]]
            3. dp[0] = 1, dp[j] = 0
            4. 先遍历背包容量，再遍历物品
        """
        dp = [0 for _ in range(target+1)]

        dp[0] = 1

        for j in range(target + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        
        return dp[target]