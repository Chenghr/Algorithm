"""
    题目描述:
        给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

        不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
        元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

    链接: https://leetcode-cn.com/problems/remove-element
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            采用双指针，一趟遍历完成数组的原地修改；
        """
        left = 0

        for right in range(len(nums)):

            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left