"""
    题目描述: 
        给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
        请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

        假设每一种面额的硬币有无限个。 
        题目数据保证结果符合 32 位带符号整数。

    链接: https://leetcode-cn.com/problems/coin-change-2
"""

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            典型的完全背包问题；
            背包容量: bag_size = amount
            物品重量: coins[i], 物品价值: coins[i]

            1. dp[i][j]:
                前 i 类 coin 装满 j 的最大方法数;
            2. 递推:
                dp[i][j] += dp[i-1][j- k*w[i]]; 0 <= k*w[i] <= j
            3. 初始化:
                dp[i][0] = 1; (什么也不装也视为一种方法)

                if j % w[0] == 0:
                    dp[0][j] = 1
                else:
                    dp[0][j] = 0

            4. 遍历顺序:
                先物品后容量，升序即可
        """
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        
        for i in range(len(coins)):
            dp[i][0] = 1

        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1

        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                for k in range(int(j / coins[i]) + 1):
                    # 注意这里要 ＋1，range 是左闭右开
                    dp[i][j] += dp[i-1][j - k*coins[i]]
        
        return dp[-1][-1]
    
    def change(self, amount: int, coins: List[int]) -> int:
        """
            采用一维 dp 数组
            1. dp[[j]:
                装满 j 的最大方法数;

            2. 递推:
                dp[j] += dp[j- w[i]];

            3. 初始化:
                dp[0] = 1, dp[j] = 0, j != 0;

            4. 遍历顺序:
                先物品后容量，升序遍历；(每次可以用第 i 类物品进行填充)

            注意一维数组和二维数组的不同:
            1. 初始化不同；
            2. 遍历的边界不同；
            3. 遍历顺序的变化。

            注意本题求得是组合数；必须要先物品后背包容量遍历；
            如果先背包容量再物品遍历，得到的是排列数，而非组合数。
        """
        dp = [0 for _ in range(amount + 1)]

        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        
        return dp[amount]