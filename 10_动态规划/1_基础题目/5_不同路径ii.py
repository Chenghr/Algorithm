"""
    题目描述:
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

        网格中的障碍物和空位置分别用 1 和 0 来表示。

    链接: https://leetcode-cn.com/problems/unique-paths-ii
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
            1. dp[i][j]，二维数组，到达(i, j)的路径数目;
            2. 递推公式:
                (i, j) 有障碍则 dp[i][j] = 0；
                否则: 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]; 
                
            3. 初始化:
                dp[0][i] = 1; dp[j][0] = 1; 
                含障碍的且包含之后的均置为0
            4. 遍历顺序:
                逐行遍历，除去边界 
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        # 初始化
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        if dp[0][0] == 0: 
            return 0  # 如果第一个格子就是障碍，return 0

        # 第一行
        for i in range(1, col):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i-1]

        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]

        # 递推
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """使用动态数组存储"""
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # 初始化dp数组
        # 该数组缓存当前行
        curr = [0] * n
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            curr[j] = 1
            
        for i in range(1, m): # 从第二行开始
            for j in range(n): # 从第一列开始，因为第一列可能有障碍物
                # 有障碍物处无法通行，状态就设成0
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    # 等价于
                    # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    curr[j] = curr[j] + curr[j - 1]
                # 隐含的状态更新
                # dp[i][0] = dp[i - 1][0]
        
        return curr[n - 1]