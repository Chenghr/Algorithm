"""
    输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
    如果有多对数字的和等于s，则输出任意一对即可。
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """双指针，左右逼近;

            可以进一步优化: 使用二分查找确定target 的初始下标位置。
        """
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
        
        return [-1, -1]
            