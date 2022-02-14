"""
    题目描述:
        斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。
        该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。
        给定 n ，请计算 F(n) 。
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        f1 = 0
        f2 = 1

        for _ in range(2, n+1):
            temp = f1 + f2
            f1 = f2
            f2 = temp
        
        return f2