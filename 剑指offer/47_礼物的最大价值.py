"""
    在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
    你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
    给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
"""

from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """
            经典的动态规划题
            滚动数组，优化空间；

            本题可以进一步优化，直接在grid上初始化第一行和第一列的值，然后遍历递推。
        """
        dp = [0] * (len(grid[0]) + 1)

        for i in range(len(grid)):
            for j in range(1, len(grid[0])+1):
                dp[j] = max(dp[j], dp[j-1]) + grid[i][j-1]
        
        return dp[-1]