"""
    题目描述:
        给定一个包含非负整数的 m x n 网格 grid ，
        请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

        说明：每次只能向下或者向右移动一步。
    
    链接: https://leetcode-cn.com/problems/minimum-path-sum/
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            经典的动态规划题目(每次移动步数限制的，不具备回溯性)
            1. dp[i][j]: 到达(i, j)的最小数字总和
            2. 递推:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
            3. 初始化:
                dp[0][0] = grid[0][0]
                dp[0][j] = dp[0][j-1] + grid[0][j]
                dp[i][0] = dp[i-1][0] + grid[i][0]
            4. 递推方向:
                左上角到右下角
        """
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        # 初始化
        dp[0][0] = grid[0][0]

        for j in range(1, len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
            应用滚动数组，压缩空间；
        """
        dp = [float('inf')] * (len(grid[0])+1)
        dp[1] = 0
        
        for i in range(len(grid)):
            for j in range(1, len(grid[0])+1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j-1] 
        
        return dp[-1]