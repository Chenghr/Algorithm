"""
    题目描述:
        给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
        如果 word 存在于网格中，返回 true ；否则，返回 false 。

        单词必须按照字母顺序，通过相邻的单元格内的字母构成，
        其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

    链接: https://leetcode-cn.com/problems/word-search
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            回溯；暴力搜索
        """
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(x: int, y: int, index: int):
            nonlocal board, word, visited
            
            if visited[x][y] or board[x][y] != word[index]:
                return False
            else:
                visited[x][y] = True
            
            if index == len(word)-1:
                return True
            
            for (i, j) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if dfs(i, j, index+1):
                        return True

            visited[x][y] = False  # 回溯

            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y, 0):
                    return True

        return False
