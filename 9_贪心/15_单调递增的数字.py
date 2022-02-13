"""
    题目描述:
        当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
        给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

    链接: https://leetcode-cn.com/problems/monotone-increasing-digits
"""

from typing import List

class Solution:

    def monotoneIncreasingDigits(self, n: int) -> int:
        """
            初步考虑暴力搜索；然后不可避免的超时
            然后考虑对暴力搜索的逻辑进行优化；
        """
        a = list(str(n))

        for i in range(len(a)-1, 0, -1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i) 
                
        return int("".join(a)) 