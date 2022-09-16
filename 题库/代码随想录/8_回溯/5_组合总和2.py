"""
    题目描述:
        给定一个候选人编号的集合 candidates 和一个目标数 target ，
        找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的每个数字在每个组合中只能使用 一次 。

    注意: 解集不能包含重复的组合。 
    
    提示:
        1 <= candidates.length <= 100
        1 <= candidates[i] <= 50
        1 <= target <= 30

    链接: https://leetcode-cn.com/problems/combination-sum-ii
"""

"""
    本题难点:
        1. 集合中含有重复元素
        2. 解集合不可包含重复的组合
            朴素想法是先求出所有的组合然后再去重，但是这样容易超时，应该尽量在搜素的过程中就去重

    进一步分析:
        所谓去重，其实就是使用过的元素不能重复选取;
        将回溯问题抽象成一棵树，“使用过”在这个树形结构上是有两个维度的，
        一个维度是同一树枝上使用过，一个维度是同一树层上使用过。
        
        题目要求，元素在同一个组合内是可以重复的，怎么重复都没事，但两个组合不能相同。
        所以我们要去重的是同一树层上的“使用过”，同一树枝上的都是一个组合里的元素，不用去重。

        强调一下，树层去重的话，需要对数组排序
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            先对 candidates 排序；增加一个 used 数组，元素是否使用过；
            当 candidates[i-1] == candidates[i] 时，
                if used[i-1] == False:
                    表明上一次层级回溯中使用了，本次直接跳过；
                if used[i-1] == True:
                    表明父节点中选中了，本次是在一个树枝上的，还可以继续使用；
        """

        result, path = [], []

        def _backtracking(candidates, target, begin_idx, used):
            nonlocal result, path

            # 递归终止条件
            if sum(path) == target:
                result.append(path.copy())
                return
            elif sum(path) > target:
                return
            
            # 单层搜索逻辑
            for idx in range(begin_idx, len(candidates)):
                if idx > 0 and candidates[idx-1] == candidates[idx] and used[idx-1] == False:
                    continue
            
                path.append(candidates[idx])
                used[idx] = True

                _backtracking(candidates, target, idx+1, used)

                path.pop()
                used[idx] = False
            
        candidates.sort()
        used = [False] * len(candidates)

        _backtracking(candidates, target, 0, used)

        return result
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            对上面进一步做优化，不用 used 数组，使用 begin_idx 去重
            另外增加剪枝操作
        """
        result, path = [], []

        def _backtracking(candidates, target, begin_idx):
            nonlocal result, path

            # 递归终止条件
            if sum(path) == target:
                result.append(path.copy())
                return
            
            # 单层搜索逻辑
            for idx in range(begin_idx, len(candidates)):
                if idx > begin_idx and candidates[idx-1] == candidates[idx]:
                    # 层级去重
                    continue

                if sum(path) + candidates[idx] > target:
                    # candidates 递增排列，剪枝操作
                    return 

                path.append(candidates[idx])

                _backtracking(candidates, target, idx+1)

                path.pop()
            
        candidates.sort()

        _backtracking(candidates, target, 0)

        return result
