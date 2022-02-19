"""
    题目描述:
        给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
        在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。
        你也可以购买它，然后在 同一天 出售。
        返回 你能获得的 最大 利润

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            动态规划:
            1. dp 数组:
                dp[i][0]: 第 i 天持有股票获得的最大收益
                dp[i][1]: 第 i 天不持有股票获得的最大收益
            
            2. 递推:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] - price[i])
                dp[i][1] = max(dp[i-1][1], price[i] + dp[i-1][0])
            
            3. 初始化:
                dp[0][0] = -price[0]; dp[0][1] = 0
            
            4. 顺序:
                从前向后
        """
        dp = [[0, 0] for _ in range(2)]

        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[1][0] = max(dp[0][0], dp[0][1] - prices[i])
            dp[1][1] = max(dp[0][1], dp[0][0] + prices[i])

            dp[0] = dp[1]
        
        return dp[1][1]
    
    def maxProfit(self, prices: List[int]) -> int:
        """
            贪心: 
            利润可以分解，只拿正利润；
            假如第0天买入，第3天卖出，那么利润为: prices[3] - prices[0]。
            相当于(prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])。
        
            局部最优: 收集每天的正利润;
            全局最优: 求得最大利润。
        """