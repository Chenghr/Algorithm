from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            题目描述:
                给你一个整数数组 nums ，数组中的元素 互不相同 。
                返回该数组所有可能的子集（幂集）。

                解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
            
            提示:
                1 <= nums.length <= 10
                -10 <= nums[i] <= 10
                nums 中的所有元素 互不相同
            
            链接: https://leetcode-cn.com/problems/subsets/
        """
        # 幂集中必含有空集
        result, path = [[]], []

        def _backtracking(nums, begin_idx):

            for idx in range(begin_idx, len(nums)):
                path.append(nums[idx])
                result.append(path.copy())  # 记录所有节点

                _backtracking(nums, idx+1)

                path.pop()
        
        _backtracking(nums, 0)

        return result
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            在上一题的基础上, nums中可能含有重复元素
            链接: https://leetcode-cn.com/problems/subsets-ii/

            思路:
                对 nums 先进行排序，在加上 used 数组进行标记
        """
        
        result, path = [], []

        def _backtracking(nums, begin_idx, used):
            nonlocal result, path

            # 记录每个节点，初始为空集
            result.append(path.copy())

            for idx in range(begin_idx, len(nums)):
                if idx > 0 and nums[idx] == nums[idx-1] and used[idx-1] == False:
                    continue

                path.append(nums[idx])
                used[idx] = True

                _backtracking(nums, idx+1, used)

                path.pop()
                used[idx] = False

        used = [False] * len(nums)
        nums.sort()

        _backtracking(nums, 0, used)

        return result
    
    def subsetsWithDup_1(self, nums: List[int]) -> List[List[int]]:
        """
            避免使用 used 数组
        """
        result, path = [], []

        def _backtracking(nums, begin_idx):
            nonlocal result, path

            # 记录每个节点，初始为空集
            result.append(path[:])

            for idx in range(begin_idx, len(nums)):
                if idx > begin_idx and nums[idx] == nums[idx-1]:
                    continue

                path.append(nums[idx])

                _backtracking(nums, idx+1)

                path.pop()

        nums.sort()

        _backtracking(nums, 0)

        return result