"""
    把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
    输入n，打印出s的所有可能的值出现的概率。
    
    你需要用一个浮点数数组返回答案，
    其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
"""

from typing import List

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        """
            n 个骰子，候选值为 n ~ 6n，共有 5n+1 种
            
            1. dp[n][x] : n 个骰子和为 x 的概率；
            2. dp[n][x] += dp[n-1][x-j] * 1/6 (j in [1, 6])
                进一步的，dp[i][j] 只会对 dp[i+1][j+k]（k in [1, 6]） 起作用，每个增加自身概率 / 6 的量
                这样避免代码是否越界的判断
            3. 初始化 [1.0 / 6] * 6
            4. 从上到下，可以使用循环数组优化空间。

            O(n^2) + O(n)
        """
        dp = [1.0 / 6] * 6

        for i in range(2, n+1):
            temp = [0] * (5*i + 1)

            for j in range(len(dp)):
                for k in range(6):
                    temp[j+k] += dp[j] / 6
            
            dp = temp
        
        return dp