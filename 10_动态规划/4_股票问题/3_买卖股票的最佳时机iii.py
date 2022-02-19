"""
    题目描述:
        给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

        注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            动态规划:
                本题的重点在于分清一天的五个状态:
                    没有操作；第一次买入；第一次卖出；第二次买入；第二次卖出
                对应 dp[i][j] 中 j 的取值范围为 0 ~ 4
            
            1. dp[i][j]: 第 i 天第 j 个状态剩余的最大资金；
            2. 递推:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
                dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
                dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
            3. 初始化:
                dp[0][0] = 0; 
                dp[0][1] = -prices[0]; dp[0][2] = 0;  # 这里要注意
                dp[0][3] = -prices[0]; dp[0][4] = 0;  
            4. 遍历顺序:
                从前向后
            
            本题可以拓展到限定指定交易次数的最大收益问题。
        """
        dp = [[0]*5 for _ in range(len(prices))]

        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[-1][4]