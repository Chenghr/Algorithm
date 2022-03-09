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
            使用贪心策略，就是最低值买，最高值（如果算上手续费还盈利）就卖。

            买入日期: 
                遇到更低点就记录一下。
            卖出日期: 
                只要当前价格大于（最低价格+手续费），就可以收获利润，
                至于准确的卖出日期，就是连续收获利润区间里的最后一天（并不需要计算是具体哪一天）。
            
            做收获利润操作的时候其实有三种情况:
                情况一: 
                收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），
                所以后面要继续收获利润。

                情况二:
                前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。

                情况三: 
                不作操作，保持原有状态（买入，卖出，不买不卖）
        """
        gain = 0
        min_price = prices[0]  # 记录最低价格

        for price in prices:

            if price > min_price + fee:
                # 计算利润
                gain += price - min_price - fee

                # 情况一，没有真正卖出，这样下次再卖的时候会把上次减去的费用补上
                min_price = price - fee  

            if price < min_price:
                # 情况二，相当于卖出一次
                min_price = price
            
            if price > min_price and price <= min_price + fee:
                # 情况三，不买不卖
                continue
                
        return gain
