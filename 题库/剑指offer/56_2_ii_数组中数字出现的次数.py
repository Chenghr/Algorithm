"""
    在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。
    请找出那个只出现一次的数字。
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """按位求和，每位对3取余，最终留下来的就是出现一次的数字
        """
        counts = [0] * 32

        for num in nums:

            for j in range(32):  # 按位求和，结果逆序存储
                counts[j] += num & 1
                num >>= 1
        
        ans = 0
        for i in range(32):
            ans <<= 1
            ans = ans | (counts[31-i] % 3)  # 由于 counts 中逆序存储，因此要反向访问

        if counts[31] % 3 == 1:
            # 最高位为 1，说明是负数
            # python 额外处理负数的情况
            ans = ~(ans ^ 0xffffffff)

        return ans 