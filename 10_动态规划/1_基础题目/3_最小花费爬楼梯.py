"""
    题目描述:
        给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
        一旦你支付此费用，即可选择向上爬一个或者两个台阶。

        你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
        请你计算并返回达到楼梯顶部的最低花费。

    链接: https://leetcode-cn.com/problems/min-cost-climbing-stairs
"""

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
            1. dp 一维数组，dp[i] 表示到达第 i 层台阶的最少花费
            2. dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]), i >= 2
            3. dp[0] = 0, dp[1] = 0  # 可以选择下标为 0 或 1 的楼梯开始爬
            4. 从前向后遍历
        """
        # len(cost) >= 2
        dp = [0, 0]

        # 注意 dp 推导的起始位置
        for i in range(2, len(cost)+1):
            dp_cur = min(dp[0]+cost[i-2], dp[1]+cost[i-1])
            dp[0] = dp[1]
            dp[1] = dp_cur
        
        return dp[1]

example = Solution()
result = example.minCostClimbingStairs([10,15,20])
print(result)