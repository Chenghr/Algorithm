"""
    题目描述:
        给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；
        整数 fee 代表了交易股票的手续费用。
        你可以无限次地完成交易，但是你每笔交易都需要付手续费。
        如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

        返回获得利润的最大值。
        注意: 这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        """
        dp = [[-prices[0], 0], [0, 0]]

        for i in range(1, len(prices)):
            dp[1][0] = max(dp[0][0], dp[0][1] - prices[i])
            dp[1][1] = max(dp[0][1], dp[0][0] + prices[i] - fee)

            dp[0] = dp[1]
        
        return dp[1][1]