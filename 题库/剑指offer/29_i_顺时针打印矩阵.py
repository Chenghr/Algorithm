"""
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """优化解法
            分别记录上下左右四个边界，然后遍历完判断是否越界
        """
        if not matrix:  # 边界判断
            return []

        # 边界记录
        l, r, t, b  = 0, len(matrix[0]) - 1, 0, len(matrix) - 1  
        res = []  

        while True:
            for i in range(l, r + 1):  # left to right
                res.append(matrix[t][i])
            t += 1
            if t > b: break

            for i in range(t, b + 1):  # top to bottom
                res.append(matrix[i][r]) 
            r -= 1
            if l > r: break

            for i in range(r, l - 1, -1):  # right to left
                res.append(matrix[b][i]) 
            b -= 1
            if t > b: break

            for i in range(b, t - 1, -1):  # bottom to top
                res.append(matrix[i][l]) 
            l += 1
            if l > r: break

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            确定好每次遍历的边界条件即可。
            注意矩阵的行列不一定相同。
        """
        if len(matrix) == 0:  # 注意空值的处理
            return []

        ans = []

        for i in range(min(len(matrix)//2, len(matrix[0])//2)):
            # 先将外围的可以遍历的遍历完
            for col in range(i, len(matrix[0])-i-1):
                ans.append(matrix[i][col])

            for row in range(i, len(matrix)-i-1):
                ans.append(matrix[row][len(matrix[0])-i-1])
            
            for col in range(len(matrix[0])-i-1, i, -1):
                ans.append(matrix[len(matrix)-i-1][col])
            
            for row in range(len(matrix)-i-1, i, -1):
                ans.append(matrix[row][i])

        if len(matrix) <= len(matrix[0]) and len(matrix) % 2 != 0:
            row = len(matrix)//2
            for col in range(row, len(matrix[0])-row):
                ans.append(matrix[row][col])

        if len(matrix) > len(matrix[0]) and len(matrix[0]) % 2 != 0:
            col = len(matrix[0])//2
            for row in range(col, len(matrix)-col):
                ans.append(matrix[row][col])
        
        return ans