"""
    题目描述:
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
        找出那个只出现了一次的元素。

        说明: 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

    链接: https://leetcode-cn.com/problems/single-number
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            使用额外空间:
                一趟遍历 + 哈希；O(n) + O(n)
            
            利用位运算——异或的性质: a^b^b = a
            可以实现一趟遍历，且无需额外空间。
        """
        ans = nums[0]

        for i in range(1, len(nums)):
            ans ^= nums[i]
        
        return ans