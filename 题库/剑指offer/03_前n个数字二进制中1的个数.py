"""
    给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
            n & (n-1): 消去 n 最后一位 1
            f(n) = f(n & (n-1)) + 1
            f(0) = 0
        """
        ans = [0] * (n+1)

        for i in range(1, n+1):
            ans[i] = ans[i & (i-1)] + 1
        
        return ans