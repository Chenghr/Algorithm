"""
    题目描述:
        数字 n 代表生成括号的对数，
        请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

    链接: https://leetcode-cn.com/problems/generate-parentheses/
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """ 
            回溯法解决，存储路径；
        """
        path, result = [], []

        def _backtracking(n_left: int, n_right: int):
            if n_left > n or n_right > n_left:
                # 非法的情况
                return
            
            if n_left == n and n_right == n:
                # 找到一个结果
                result.append(''.join(path))
                return

            path.append('(')
            _backtracking(n_left+1, n_right)
            path.pop()  # 回溯

            path.append(')')
            _backtracking(n_left, n_right+1)
            path.pop()  # 回溯
        
        _backtracking(0, 0)
        return result

a = Solution()
ans = a.generateParenthesis(3)
print(ans)