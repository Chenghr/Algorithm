"""
    题目描述:
        编写一个程序，通过填充空格来解决数独问题。

        数独的解法需 遵循如下规则:
            数字 1-9 在每一行只能出现一次。
            数字 1-9 在每一列只能出现一次。
            数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
        
        数独部分空格内已填入了数字，空白格用 '.' 表示。

    提示:
        board.length == 9
        board[i].length == 9
        board[i][j] 是一位数字或者 '.'
        题目数据 保证 输入数独仅有一个解

    链接: https://leetcode-cn.com/problems/sudoku-solver
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        self.backtracking(board)

        return
    
    def isValid(self, board, row, col, val) -> bool:
        # 检查行
        for str in board[row]:
            if str == '.':
                continue
            
            if val == int(str):
                return False

        # 检查列
        board_col = [board[i][col] for i in range(len(board))]
        for str in board_col:
            if str == '.':
                continue
            
            if val == int(str):
                return False

        # 检查九宫格
        row1 = int(row / 3)
        col1 = int(col / 3)
        board_mini = [board[i][col1*3:col1*3+4] for i in range(row1*3, (row1+1)*3)]

        for row in range(0, 3):
            for col in range(0, 3):
                if board_mini[row][col] == '.':
                    continue
            
                if val == int(board_mini[row][col]):
                    return False
        
        return True

    def backtracking(self, board: List[List[str]]) -> bool:
        """
            逐行逐列遍历棋盘，每个可放数字位置逐个试探，找到一个可行解即返回 True
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    continue

                for val in range(1, 10):
                    if self.isValid(board, row, col, val):
                        board[row][col] = str(val)

                        if self.backtracking(board):
                            return True
                        
                        board[row][col] = '.'
                # 1 ~ 9 都放不了，则当前找不到可行解
                return False
        
        # 遍历完没问题，则返回True
        return True 
