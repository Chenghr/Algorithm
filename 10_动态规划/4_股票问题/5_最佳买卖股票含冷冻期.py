"""
    题目描述:
        给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。
        设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
        卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            每天有三个状态:
                0: 持有股票; 1: 不持有股票且处于冰冻期; 2: 不持有股票且不处于冰冻期

                dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
                dp[i][1] = dp[i-1][0] + prices[i]
                dp[i][2] = max(dp[i-1][2], dp[i-1][1])

                dp[0][0] = -prices[0]
                dp[0][1] = 0
                dp[0][2] = 0
        """
        dp = [[0, 0, 0] for _ in range(len(prices))]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        
        return max(dp[-1][1], dp[-1][2])
        """
            状态一: 买入股票状态（今天买入股票，或者是之前就买入了股票然后没有操作）
            
            卖出股票状态，这里就有两种卖出股票状态
                状态二: 两天前就卖出了股票，度过了冷冻期，一直没操作，今天保持卖出股票状态
                状态三: 今天卖出了股票

            状态四: 今天为冷冻期状态，但冷冻期状态不可持续，只有一天

            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i]);
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3]);
            dp[i][2] = dp[i - 1][0] + prices[i];
            dp[i][3] = dp[i - 1][2];
        """