# https://leetcode-cn.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """使用二分搜索
        """
        left, right = 0, len(nums)

        while left < right:
            mid = int((left + right) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        return left