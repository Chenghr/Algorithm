"""
    题目描述:
        给你一个整数数组 coins ，表示不同面额的硬币；
        以及一个整数 amount ，表示总金额。

        计算并返回可以凑成总金额所需的 最少的硬币个数 。
        如果没有任何一种硬币组合能组成总金额，返回 -1 。

        你可以认为每种硬币的数量是无限的。

    链接: https://leetcode-cn.com/problems/coin-change
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            完全背包问题的变式:
            1. dp[j]: 装满容量 j 的背包所需最少硬币数;
            2. dp[j] = min(dp[j], dp[j - coins[i]]+1)
            3. dp[0] = 0, dp[j] = float('inf')
            4. 先物品再背包容量，背包容量顺序遍历
        """
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        if dp[amount] == float('inf'):
            return -1
            
        return dp[amount]