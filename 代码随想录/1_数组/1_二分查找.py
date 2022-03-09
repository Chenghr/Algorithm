"""
    题目描述:
        给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
        写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

    链接: https://leetcode-cn.com/problems/binary-search/
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            有序数组搜索指定元素，采用二分搜索的思想;
    
            二分搜索注意搜索区间的问题，左闭右开还是左闭右闭。

            注意本题中无重复元素，否则返回的下标可能不唯一。
        """
        left, right = 0, len(nums)

        while left < right:
            # 左闭右开
            mid = int((left + right) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            
        return -1