"""
    题目描述:
        编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。
        
        该矩阵具有以下特性：
            每行的元素从左到右升序排列。
            每列的元素从上到下升序排列。

    链接: https://leetcode-cn.com/problems/search-a-2d-matrix-ii
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            1. 暴力；
            2. 每行二分；
            3. Z 字形查找
                从整个矩阵的右上角开始枚举，假设当前枚举的数是 x:
                    如果 x 等于target，则说明我们找到了目标值，返回true；
                    如果 x 小于target，则 x左边的数一定都小于target，我们可以直接排除当前一整行的数；
                    如果 x 大于target，则 x 下边的数一定都大于target，我们可以直接排除当前一整列的数；
        """
        row, col = 0, len(matrix[0])-1

        while row < len(matrix) and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
        
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            对角线上的元素一定是单调递增的，因此可以先在对角线上二分查找，确定对应元素可能在的行和列；
            然后再对应的行和列中进行二分查找。
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            # 在矩阵内部搜索点
            return False
        
        index_diag = self.binarySearchMatrix(matrix, target)
        
        # 小于等于 target 的对角元素所在位置
        row = min(index_diag, len(matrix)-1)
        col = min(index_diag, len(matrix[0])-1)

        searchRow = min(row+1, len(matrix)-1)
        searchCol = min(col+1, len(matrix[0])-1)

        if matrix[row][col] == target:
            return True

        index_col = self.binarySearch(matrix[searchRow], target)
        if matrix[searchRow][index_col] == target:
            return True
        
        index_row = self.binarySearchCol(matrix, searchCol, target)
        if matrix[index_row][searchCol] == target:
            return True
        
        return False

    def binarySearchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        left, right = 0, max(m, n)

        while left < right:
            mid = (left + right) // 2

            row, col = min(mid, m-1), min(mid, n-1)

            if matrix[row][col] == target:
                return mid
            elif matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid

        return left

    def binarySearch(self, nums, target):
        """返回第一个小于等于 target 的下标
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        return left
    
    

    def binarySearchCol(self, matrix, col, target):
        left, right = 0, len(matrix)

        while left < right:
            mid = (left + right) // 2

            if matrix[mid][col] == target:
                return mid
            elif matrix[mid][col] < target:
                left = mid + 1
            else:
                right = mid
        
        return left