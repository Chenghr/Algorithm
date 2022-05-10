"""
    假设把某股票的价格按照时间先后顺序存储在数组中，
    请问买卖该股票一次可能获得的最大利润是多少？
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            贪心:
                左边找一个最小值，右边找一个最大值，差值即为最大利润。
        """
        if len(prices) == 0:
            return 0  # 处理边界条件

        minPrice, maxProfit = prices[0], 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        
        return maxProfit
    
    def maxProfit(self, prices: List[int]) -> int:
        """
            贪心:
                遍历整个数组，持续计算利润，当利润为负的时候，重置利润为0，当出现最大利润的时候，记录下最大利润
        """
        if len(prices) < 2:
            return 0

        curProfit, maxProfit = 0, 0

        for i in range(1, len(prices)):
            curProfit = curProfit + prices[i] - prices[i-1]

            curProfit = max(curProfit, 0)
            maxProfit = max(maxProfit, curProfit)
        
        return maxProfit
        
    
    def maxProfit(self, prices: List[int]) -> int:
        """
            动态规划:
                每天有两个状态: 持有或不持有。
                “持有”不代表就是当天“买入”, 也有可能是昨天就买入了，今天保持持有的状态

                dp[i][0]: 第 i 天持有股票所得利润
                dp[i][1]: 第 i 天不持有所得利润

                dp[i][0] = max(dp[i - 1][0], -prices[i]);  # 只能买卖一次
                dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);

                dp[0][0] -= prices[0]; dp[0][1] = 0;
        """