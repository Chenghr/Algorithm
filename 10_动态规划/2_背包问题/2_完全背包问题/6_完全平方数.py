"""
    题目描述:
        给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

        完全平方数 是一个整数，其值等于另一个整数的平方；
        换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

    链接: https://leetcode-cn.com/problems/perfect-squares
"""

class Solution:
    def numSquares(self, n: int) -> int:
        """
            对于 <= n 的完全平方数；每个数视为数量不限的物品；
            背包容量为 n；
            本题转化为: 装满背包所需的最少物品数

            1. dp[j]:  装满容量 j 的背包所需的最少物品数
            2. dp[j] = min(dp[j], dp[j-nums[i]]+1)
            3. dp[0] = 0, dp[j] = float('inf')
            4. 先物品再背包容量，背包容量升序
        """
        nums = []

        for num in range(n+1):
            if int(int(num ** 0.5) ** 2) == num:
                nums.append(num)
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for num in nums:
            for j in range(num, n+1):
                dp[j] = min(dp[j], dp[j-num]+1)
        
        if dp[n] == float('inf'):
            return -1
        
        return dp[n]