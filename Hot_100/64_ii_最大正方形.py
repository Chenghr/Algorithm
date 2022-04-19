"""
    题目描述:
        在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
    
    链接: https://leetcode-cn.com/problems/maximal-square/
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
            动态规划

            1. dp[i][j]
                以 i, j 为右下角顶点的正方形的最长边长；

            2. 递推
                if matrix[i][j] = '1':
                    dp[i][j] = min(左，上，左上) + 1;
                理解:
                    三者包含的正方形面积的并集（可以画图上色）与 matrix[i][j] 一起能够构成的最大正方形。
                
                特例理解:
                    min(2, 2, 2) 说明三者构成的面积刚好是一个九宫格缺失右下角的形状，补上 matrix[i][j] 就是一个 3x3 的正方形;
                    min(1, 2, 2) 中，三者构成的面积收到 1 的影响，将是一个九宫格缺失左下角和右下角的形状（倒“土”型），补上 matrix[i][j] 最多只能构成 2x2 的正方形
            ......
        """
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        maxLen = 0
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            maxLen = max(maxLen, dp[0][j])

        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            maxLen = max(maxLen, dp[i][0])
        
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1
                    maxLen = max(maxLen, dp[i][j])
        
        return maxLen * maxLen
        
