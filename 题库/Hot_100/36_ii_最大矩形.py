"""
    题目描述:
        给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，
        找出只包含 1 的最大矩形，并返回其面积。

    链接: https://leetcode-cn.com/problems/maximal-rectangle/
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
             本题前置题目: 柱状图中最大的矩形
                https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
            
            dp + 单调栈
            1. 按层构造柱状图；
            2. 利用单调栈求解每层的最大矩形面积；最后选择最大值。
        """
        # 转化为柱状图
        for j in range(len(matrix[0])):
            matrix[0][j] = int(matrix[0][j])

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i-1][j] > 0 and matrix[i][j] == '1':
                    matrix[i][j] = matrix[i-1][j] + int(matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j])
        
        maxArea = 0
        for i in range(len(matrix)):
            
            matrix[i].append(0)  # 插入哨兵，保证不越界
            matrix[i].insert(0, 0)

            stack = [0]  # 单调栈；从栈顶到栈底降序; 存下标

            for j in range(1, len(matrix[i])):
                while stack and matrix[i][stack[-1]] > matrix[i][j]:
                    index = stack.pop()
                    curArea = matrix[i][index] * (j-stack[-1]-1)

                    maxArea = max(maxArea, curArea)

                stack.append(j)

        return maxArea

a = Solution()
ans = a.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(ans)