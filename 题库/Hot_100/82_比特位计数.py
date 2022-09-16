"""
    题目描述:
        给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，
        计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
    
    在O(n)内解决。
"""
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
            暴力: 对每个数进行二进制位1的个数求解
            使用 x & x-1 去除最后一位 1 的技巧；
            O (nlogn)
        """
        pass

    def countBits(self, n: int) -> List[int]:
        """
            动态规划: 最高有效位；
            由于 x & x-1 仅去掉了 x 最后一位 1，因此 x 在 x & x-1 bit 位的基础上加 1即可。
            特殊情况在于，x 为 1时，x-1 为 0， x & x-1 = x，不会比 x 小，因此要加入初始化中。
        """
        if n == 0:
            return [0]

        bits = [0, 1]
        for i in range(2, n+1):
            bits.append(bits[i & (i-1)] + 1)
        
        return bits
    
    def countBits(self, n: int) -> List[int]:
        """
            动态规划: 最低有效位
            i >> 1会把最低位去掉，因此i >> 1 也是比i小的，同样也是在前面的数组里算过。
            当 i 的最低位是 0，则 i 中 1 的个数和 i >> 1 中1的个数相同；
            当 i 的最低位是 1，i 中 1 的个数是 i >> 1中 1 的个数再加 1
        """
        bits = [0] * (n+1)

        for i in range(n+1):
            bits[i] = bits[i >> 1] + (i & 1)  # 判断 i 的最低位是否为 1
        
        return bits