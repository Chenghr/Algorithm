"""
    题目描述:
        你是一个专业的小偷，计划偷窃沿街的房屋。
        每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统;
        如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

        给定一个代表每个房屋存放金额的非负整数数组，
        计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

    链接: https://leetcode-cn.com/problems/house-robber
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            1. dp[j]: 前 j 个房屋可偷得的最高金额；
            2. 对于第 j 个房屋，有偷和不偷两种情况，选择其中较大的那个;
                dp[j] = max(dp[j-1], dp[j-2] + nums[j])
            3. dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
            4. 从前到后
        """
        dp = [0] * (len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for j in range(2, len(nums)):
            dp[j] = max(dp[j-1], dp[j-2]+nums[j])
        
        return dp[-1]