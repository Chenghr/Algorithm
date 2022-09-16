"""统计一个数字在排序数组中出现的次数。
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            nums 是一个非递减数组；
            有序数组中查找数，使用二分查找；

            分别查找 nums 中 target 的左边界和右边界；相减即可。

            进一步的效率优化:
                查找完右边界后，可用 nums[j] = j 判断数组中是否包含 target ，
                若不包含则直接提前返回 0，无需后续查找左边界。
                查找完右边界后，左边界 left 一定在闭区间 [0, j] 中，因此直接从此区间开始二分查找即可。
        """
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)

        return right - left + 1 if left != -1 else 0
    
    def searchLeft(self, nums, target):
        if len(nums) == 0:  # 边界条件
            return -1

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        
        return left if 0 <= left < len(nums) else -1
    
    def searchRight(self, nums, target):
        if len(nums) == 0:  # 边界条件
            return -1

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid 
        
        return left - 1 if 1 <= left <= len(nums) else -1