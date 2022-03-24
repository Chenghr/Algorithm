"""
    题目描述:
        给定一个 n * n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
        你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

    链接: https://leetcode-cn.com/problems/rotate-image
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
            Do not return anything, modify matrix in-place instead.
            模拟题，确定好边界以及遍历顺序即可；
            
            i in range (int(n/2)):
                第 i 圈，每行有 n-2i 个元素；
                第 i 圈包括第 i 行，第 n-1-i 行，第 i 列，第 n-1-i 列；

        """
        n = len(matrix)
        for i in range(int(n/2)):
            # 逐圈替换
            for j in range(i, n-1-i):
                # 左闭右开
                # 模拟顺时针旋转
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
        
        return matrix