"""
    题目描述:
        给定一个二维矩阵 matrix，以下类型的多个请求:
            计算其子矩形范围内元素的总和，
            该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。

        实现 NumMatrix 类：
            - NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
            - int sumRegion(int row1, int col1, int row2, int col2) 
              返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。

    链接: https://leetcode-cn.com/problems/range-sum-query-2d-immutable
"""

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 

        preSum = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        # 构造前缀和矩阵
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                # 计算矩阵 [(0,0), (i,j)]的元素和
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + matrix[i-1][j-1] - preSum[i-1][j-1]

        self.preSum = preSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
            同样采用前缀和的思想，将每次的遍历查询替换成O(1)的时间复杂度。

            二维preSum数组，专门记录以原点为顶点的矩阵的元素之和，
            就可以用几次加减运算算出任何一个子矩阵的元素和   
        """
        return self.preSum[row2+1][col2+1] - self.preSum[row1][col2+1] - self.preSum[row2+1][col1] + self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)