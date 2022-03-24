"""
    题目描述:
        给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
        原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

        我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
        必须在不使用库的sort函数的情况下解决这个问题。

    进阶:
        你可以不使用代码库中的排序函数来解决这道题吗？
        你能想出一个仅使用常数空间的一趟扫描算法吗？

    链接: https://leetcode-cn.com/problems/sort-colors
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
            多指针法
            先使用双指针法，将 0 全移到左边；
            再使用双指针法，将 2 全移到右边；
        """
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] == 0:
                left += 1
            while left < right and nums[right] > 0:
                right -= 1
            
            nums[left], nums[right] = nums[right], nums[left]
        
        right = len(nums)-1
        while left < right:
            while left < right and nums[left] == 1:
                left += 1
            while left < right and nums[right] > 1:
                right -= 1
            
            nums[left], nums[right] = nums[right], nums[left]

        return 
    
    def sortColors(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.

            双指针法
                left: 指向左边第一个非 0 元素下标
                right: 指向右边第一个非 2 元素下标
            mid: 中间元素

            left, right = 0, len(nums)-1
            mid = 0
            从左到右遍历数组
                if nums[mid] == 2:
                    # 持续交换，直到 nums[right] != 2
                    change(mid, right); right -= 1
                if nums[mid] == 0:
                    # 由于先执行上一个if,因此mid指向元素不是0就是1
                    change(left, mid); left += 1
        """
        """
            方法2:
                p0 交换 0， p1 交换1
                从左向右遍历数组:
                    if nums[i] == 1:
                        swap(p1, i)
                    if nums[i] == 0:
                        swap(p0, i)
                        if p0 < p1:
                            swap(p1, i)  # 因为必定会将一个1交换出去
                swap 后默认增加了 1
        """
        left, right = 0, len(nums)-1
        mid = 0

        while mid <= right:
            while mid <= right and nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1

            mid += 1
        
        return