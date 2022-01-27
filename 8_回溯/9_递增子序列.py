"""
    题目描述:
        给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。
        你可以按 任意顺序 返回答案。

        数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
    
    提示:
        1 <= nums.length <= 15
        -100 <= nums[i] <= 100

    链接: https://leetcode-cn.com/problems/increasing-subsequences
"""

from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
            思路1:
                回溯 + 剪枝搜索所有空间

            注意点:
                1. 递增子序列不可重复，数组中有重复元素，涉及到去重问题；
                    
                    由于本题为寻找自增子序列，因此不可以采用之前的排序去重的思想；
                    根据树形示意图可知，同层中不能出现相同的元素，可以采用哈希(set)来去重；
                    由于题目中给出了数组中值的范围，因此可以用数组来模拟哈希。

                2. 数字相同视为一种递增，递增子序列最小为2，因此本题记录的是所有节点，而非仅仅叶子节点
        """

        result, path = [], []

        def _backtracking(nums, begin_idx):

            nonlocal result, path

            if len(path) > 1:
                result.append(path[:])
            
            map = [False] * 201  # 原范围为 -100 ~ 100， 201个数
            for idx in range(begin_idx, len(nums)):
                if map[nums[idx]+100] == True:
                    # 同层去重
                    continue
                
                if len(path) > 0 and path[-1] > nums[idx]:
                    # 递增
                    continue
                
                path.append(nums[idx])
                map[nums[idx]+100] = True  # 标记

                _backtracking(nums, idx+1)

                path.pop()

        _backtracking(nums, 0)
        return result