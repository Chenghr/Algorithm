"""
    题目描述:
        给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，
        要求也按 非递减顺序 排序。
    
    进阶: 请你设计时间复杂度为 O(n) 的算法解决本问题

    链接: https://leetcode-cn.com/problems/squares-of-a-sorted-array/
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
            数组有序，因此可以先找到最小正值元素出现的下标，然后从这个下标向左右拓展，
            每次选择较小的元素填入新的数组。
        """
        if nums[0] >= 0:
            return [num**2 for num in nums]

        left, right = -1, len(nums)

        for idx, num in enumerate(nums):
            if num >= 0:
                right = idx
                break
        
        left = right - 1
        numSorted = []

        while left >=0 and right < len(nums):
            if nums[left] ** 2 <= nums[right] ** 2:
                numSorted.append(nums[left] ** 2)
                left -= 1
            else:
                numSorted.append(nums[right] ** 2)
                right += 1
        
        while left >= 0:
            numSorted.append(nums[left] ** 2)
            left -= 1
        
        while right < len(nums):
            numSorted.append(nums[right] ** 2)
            right += 1
        
        return numSorted

        """
            题解思路:
                换个角度想，排序后数组的最大值只能出现在原始数组的两端，最小值出现在数组中间；
                因此可以考虑采用双指针法，起始指向数组起点和终点，逆序填充排序后的数组；从两边向中间遍历。
        """
        
        