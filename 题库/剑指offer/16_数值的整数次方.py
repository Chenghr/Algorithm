"""
    实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """update，利用位运算，比后面的快
        """
        def quickPow(x, n):
            ans = 1
            while n > 0:
                if n & 1:
                    ans *= x
                
                x *= x
                n = n >> 1
            
            return ans
        
        if n >= 0:
            return quickPow(x, n)
        return 1.0 / quickPow(x, -n)

    def myPow(self, x: float, n: int) -> float:
        """快速幂算法
            注意这里 的 n 有正负问题
        """
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
            
            x = x ** 2
            n  = n // 2
        
        return ans
