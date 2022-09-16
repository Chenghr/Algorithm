"""
    题目描述:
        给定一个整数 n ，返回 n! 结果中尾随零的数量。

        提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
    
    进阶: 你可以设计并实现对数时间复杂度的算法来解决此问题吗？

    链接: https://leetcode-cn.com/problems/factorial-trailing-zeroes/
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
            首先，两个数相乘结果末尾有 0，一定是因为两个数中有因子 2 和 5，因为 10 = 2 x 5。
            则问题转化为: 
                n! 最多可以分解出多少个因子 2 和 5 ？

            又因为每个偶数都能分解出因子 2，因子 2 肯定比因子 5 多得多。
            因此问题又转化为: 
                n! 最多可以分解出多少个因子 5 ？
            
            注意有的数字不只可以提供一个因子 5，例如 125 = 5*5*5，因此可以提供 3 个因子 5。
        """
        result = 0

        while n > 0:
            n = n // 5
            result += n
        
        return result

        
