"""
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
    使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
"""

from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """双指针；
            从前向后找偶数，从后向前找奇数，找到了则交换。
            
            小技巧: 使用位运算优化判断奇偶性的时间；
                    x&1 位运算 等价于 x%2 取余运算，即皆可用于判断数字奇偶性。
        """
        left, right = 0, len(nums)-1

        while left < right:
            while left < right and nums[right] % 2 == 0:
                right -= 1
            
            while left < right and nums[left] % 2 == 1:
                left += 1
            
            nums[left], nums[right] = nums[right], nums[left]
        
        return nums