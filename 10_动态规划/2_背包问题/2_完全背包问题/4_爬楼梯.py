"""
    题目描述:
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    
    链接: https://leetcode-cn.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
            除了普通的动态规划思路，本题还可以转化为完全背包问题；
            求解排列数。

            另外本题采用完全背包的解法，可以拓展到一次爬 m 阶楼梯的情况
        """
        nums = [1, 2]

        dp = [0] * (n + 1)
        dp[0] = 1

        for j in range(n + 1):
            for i in range(len(nums)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        
        return dp[n]