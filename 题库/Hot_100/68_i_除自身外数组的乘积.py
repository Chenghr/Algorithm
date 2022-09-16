"""
    题目描述:
        给你一个整数数组 nums，返回 数组 answer ，
        其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

        题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。

        请不要使用除法，且在 O(n) 时间复杂度内完成此题。

    链接: https://leetcode-cn.com/problems/product-of-array-except-self
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            除去自身的乘积 = i 前面所有数的乘积 * i 后面所有数的乘积
            优化空间，在算后面乘积的时候直接出结果
        """
        preProduct = [1] * len(nums)
        postProduct = [1] * len(nums)

        for i in range(1, len(nums)):
            preProduct[i] = nums[i-1] * preProduct[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postProduct[i] = nums[i+1] * postProduct[i+1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(preProduct[i] * postProduct[i])
        
        return ans
