"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

提示：
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

https://leetcode-cn.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 暴力求解，两层循环遍历 -> O(n^2)
        for idx1 in range(len(nums)-1):
            # 注意range是左闭右开
            for idx2 in range(idx1+1, len(nums)):

                if nums[idx2] == target - nums[idx1]:
                    return [idx1, idx2]
        
        return [-1, -1]
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 哈希，dict, O(n)

        # 记录数组中的数及其对应的下标
        record = dict()

        for idx, val in enumerate(nums):

            if target - val not in record:
                record[val] = idx
            else:
                return [record[target-val], idx]
        
        return [-1, -1]