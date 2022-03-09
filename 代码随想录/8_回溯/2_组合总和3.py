"""
    题目描述:
        找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

    说明:
        所有数字都是正整数。
        解集不能包含重复的组合。 

    链接: https://leetcode-cn.com/problems/combination-sum-iii
"""
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        """
        result, path = [], []

        def _backtracking(k, n, begin):

            if len(path) == k:

                if sum(path) == n:
                    result.append(path.copy())
                return
            
            for num in range(begin, 10):
                path.append(num)

                if n - sum(path) <= sum(list(range(num+1, 10))):
                    # 剪枝
                    _backtracking(k, n, num+1)

                path.pop()
        
        _backtracking(k, n, 1)
        return result
    
example = Solution()

result = example.combinationSum3(9, 45)

print(result)