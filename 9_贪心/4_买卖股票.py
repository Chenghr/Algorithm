"""
    题目描述:
        给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。

        在每一天，你可能会决定购买和/或出售股票。
        你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
        返回 你能获得的 最大 利润 。

    链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            个人解法:
                价格波动，在波底买在波峰卖，注意判断最后一个价格时是否持有股票
        """
        gain, hold_price = 0, float('inf')

        for idx, price in enumerate(prices):
            if idx == len(prices)-1:
                if hold_price != float('inf'):
                    gain += price - hold_price

            else:
                if hold_price == float('inf'):
                    # 手上不持有股票
                    if price < prices[idx+1]:
                        hold_price = price
                else:
                    # 手中持有股票
                    if price > prices[idx+1]:
                        gain += price - hold_price
                        hold_price = float('inf')
        
        return gain
    
    def maxProfit(self, prices: List[int]) -> int:
        """
            贪心解法:
                把利润分解为每天为单位的维度，而不是从整体去考虑；
                我们只收集每天的正利润；正利润的空间即为股票买卖的区间，我们只用关注利润，不用考虑记录区间。
        """

        gain = 0

        for idx in range(1, len(prices)):
            gain_day = prices[idx] - prices[idx-1]

            if gain_day > 0:
                gain += gain_day
        
        return gain