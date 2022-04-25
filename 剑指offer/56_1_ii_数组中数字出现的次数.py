"""
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
    请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""

from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """
        """
        ans = 0  # 得到 a ^ b
        for num in nums:
            ans ^= num
        
        # 确定 a ^ b 中不为 1 的位置
        temp = 1
        while ans & temp == 0:
            temp <<= 1
        
        x, y = 0, 0
        for num in nums:  # 根据 1 的位置分类
            if num & temp == 0:
                x ^= num
            else:
                y ^= num
        
        return [x, y]
