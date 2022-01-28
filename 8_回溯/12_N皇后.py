"""
    题目描述:
        n 皇后问题 研究的是如何将 n 个皇后放置在 n*n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

        每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，
        该方案中 'Q' 和 '.' 分别代表了皇后和空位。

    链接: https://leetcode-cn.com/problems/n-queens
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            经典的回溯问题，加上
        """
        paths, path = [], []
    
        def check(j):
            nonlocal path
            for row, num in enumerate(path):
                if num == j or len(path)-row == abs(j-num):
                    return False
            
            return True

        def backtracking(k):
            nonlocal path

            if k == n+1:
                paths.append(path[:])
                return 
            
            for num in range(1, n+1):
                if not check(num):
                    continue

                path.append(num)
                backtracking(k+1)
                path.pop()
        
        def convert(paths, n):
            results = []

            for path in paths:
                result = []

                for col in path:
                    temp = ['.'] * n
                    temp[col-1] = 'Q'
                    result.append(''.join(temp))
                
                results.append(result)

            return results
        
        backtracking(1)
        results = convert(paths, n)

        return results
