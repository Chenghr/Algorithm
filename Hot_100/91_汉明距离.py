"""
    题目描述:
        两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
        给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
    
    链接: https://leetcode-cn.com/problems/hamming-distance/
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
            1. 将两个整数转化为 二进制数，较小的高位补0，然后逐位比较。
            2. 将两个整数按位异或，得到一个新的数，判断新的数二进制中1的个数（z & z-1）
        """
        z = x ^ y  # 异或，不同为1，相同为 0

        count = 0
        while z:
            z = z & (z-1)  # 消除 z 中最后一位 1
            count += 1
        
        return count