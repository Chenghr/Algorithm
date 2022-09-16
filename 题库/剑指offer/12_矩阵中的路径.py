
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            存在性问题，选择深搜
            遍历棋盘，遇到word[0]的字符则深搜一次;

            Note: 直接修改 board 棋盘代替 visited 标记数组
        """
        def dfs(i, j, k) -> bool:
            nonlocal board

            if board[i][j] != word[k]:
                return False

            if k == len(word)-1:
                return True

            board[i][j] = ''

            for (nx, ny) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if dfs(nx, ny, k+1):
                        return True

            board[i][j] = word[k]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            存在性问题，选择深搜
            遍历棋盘，遇到word[0]的字符则深搜一次
        """

        def dfs(x, y, index) -> bool:
            nonlocal board, visited

            if board[x][y] != word[index]:
                return False

            if index == len(word)-1:
                return True

            visited[x][y] = True

            for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny]:
                    if dfs(nx, ny, index+1):
                        return True

            visited[x][y] = False

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False] * len(board[0]) for _ in range(len(board))]

                    if dfs(i, j, 0):
                        return True
        
        return False