"""
    题目描述:
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
        设计一个算法来计算你所能获取的最大利润。

        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""

"""
    股票只能买卖一次；

    暴力:
        两层循环找最优间距。 O(n*2)

    贪心:
        股票只买卖一次，向左取最小值，向右取最大值，差值即为最大利润。
    
    动态规划:
        1. dp[i][0]: 表示第i天持有股票所得最多现金;
            dp[i][1] 表示第i天不持有股票所得最多现金;

            “持有”不代表就是当天“买入”, 也有可能是昨天就买入了，今天保持持有的状态
        
        2. 递推: 
            dp[i][0] = max(dp[i - 1][0], -prices[i]);  # 只能买卖一次
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0]);

        3. 初始化:
            dp[0][0] -= prices[0]; dp[0][1] = 0;

        4. 遍历顺序:
            从前向后遍历。

        本题返回 dp[-1][1], 
        因为本题中不持有股票状态所得金钱一定比持有股票状态得到的多.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """动态规划；另外本题还可以使用动态数组压缩空间
        """
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] -= prices[0]

        for i in range(1, len(prices)):
            # 持有的最大利益
            dp[i][0] = max(dp[i-1][0], -prices[i])
            # 不持有的最大利益
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[i])
        
        return dp[-1][1]
    
    def maxProfit(self, prices: List[int]) -> int:
        """贪心
        """
        min_price = float('inf')
        max_gain = 0

        for price in prices:
            min_price = min(min_price, price)
            max_gain = max(max_gain, price-min_price)
        
        return max_gain