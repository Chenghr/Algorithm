"""
    题目描述:
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    
    链接: https://leetcode-cn.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
            1. dp 一维数组，dp[i] 表示上 i 层台阶的方法数
            2. dp[i] = dp[i-1] + dp[i-2], i >= 1
            3. dp[1] = 1, dp[2] = 2
            4. 从前向后遍历
        """
        if n <= 2:
            return n
        
        dp = [1, 2]

        for _ in range(3, n+1):
            sum = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = sum

        return dp[1]