
"""
    一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
    在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
            排序数组的搜索问题，使用 二分法解决；
            根据题意数组可以划分为两部分: 
                左子数组: nums[i] == i, 右子数组: nums[i] != i
            缺失的元素即为 "右子数组" 首位元素对应的索引，因此本题即为使用 二分法查找右子数组的首位元素

            nums[mid] == m:
                右子数组的首位元素在 [mid+1, right）中
            num[mid] != m:
                左子数组的末位元素一定在 [left, mid)中
        """
        left, right = 0, len(nums)

        while left < right:  # 左闭右开
            mid = (left + right) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid  
        
        return left


    def missingNumber(self, nums: List[int]) -> int:
        """
            数组内部有序，假设每个位置都有一一对应关系，则 nums[i] == i 均成立；
            现在使用二分查找的思想:
                if nums[mid] == mid: 
                    说明 0 - mid 均满足对应条件；
                    left = mid + 1，去右半边找；
                else:
                    说明 left、right 区间内有不匹配的数，这时唯一能做的就是压缩右边的边界区间；
                    right - 1；
                最终 left 即为缺失值。
                
        """
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == mid:
                left = mid + 1
            else:
                right = right - 1
        
        return left