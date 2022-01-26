"""
    题目描述:
        给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
        找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
        candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

        对于给定的输入，保证和为 target 的不同组合数少于 150 个。
    
    提示:
        1 <= candidates.length <= 30
        1 <= candidates[i] <= 200
        candidate 中的每个元素都 互不相同
        1 <= target <= 500

    链接: https://leetcode-cn.com/problems/combination-sum
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def _backtracking(start_idx):
            nonlocal result, path, candidates, target

            if sum(path) == target:
                result.append(path.copy())
                return
            elif sum(path) > target:
                return
            
            for idx in range(start_idx, len(candidates)):
                path.append(candidates[idx])
                _backtracking(idx)  # 允许重复拿取数字
                path.pop()
        
        # 这里由于提示内容，没加异常处理，例如总和为0等情况
        candidates.sort()  # 排序后更利于处理
        _backtracking(0)

        return result