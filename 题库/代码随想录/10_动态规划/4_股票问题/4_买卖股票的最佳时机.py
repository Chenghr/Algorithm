"""
    题目描述:
        给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

        注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
            每天有 2K + 1 个状态；

            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (-1)^j * price[i])
            
            初始化:
                dp[i][0] = 0
                dp[0][j] = (1 + (-1)^(j+1))prices[0]
        """
        if len(prices) == 0:
            return 0
            
        dp = [[0] * (2*k + 1) for _ in range(len(prices))]

        for j in range(2*k + 1):
            if j % 2 == 1:
                dp[0][j] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(1, 2*k + 1):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
        
        return dp[-1][-1]