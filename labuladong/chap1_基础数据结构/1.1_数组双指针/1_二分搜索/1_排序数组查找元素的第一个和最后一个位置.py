# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """使用二分查找，分别搜索左边界以及右边界即可；注意区间控制。
        """
        if len(nums) == 0:
            return [-1, -1]
        
        return [self.searchLeftBound(nums, target), self.searchRightBound(nums, target)]
    
    def searchLeftBound(slef, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            # 左闭右开
            mid = int((left + right) / 2)

            if nums[mid] == target:
                # 收缩右边界, 这里不能写 mid + 1
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        if left == len(nums) or nums[left] != target:
            return -1

        return left
    
    def searchRightBound(slef, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            # 左闭右开
            mid = int((left + right) / 2)

            if nums[mid] == target:
                # 收缩左边界
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        
        if left == 0 or nums[left-1] != target:
            return -1

        return left - 1
    