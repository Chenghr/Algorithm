"""
    写一个函数，求两个整数之和，
    要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
"""

class Solution:
    def add(self, a: int, b: int) -> int:
        """
            对 a + b 分成两部分考虑: 不进位加法 + 进位
            x ^ y: 不进位加法
            (x & y) << 1 : 获得进位

            注意本题 a, b 可能为负数
            Python，Java 等语言中的数字都是以 补码 形式存储的。
            但 Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
            因此需要手动提取负数的补码。
            负数的补码则是将其对应正数按位取反再加1。
        """
        
        x = 0xffffffff
        a, b = a & x, b & x  # 舍去此数字 32 位以上的数字（将 32 位以上都变为 00 ）

        while b != 0:
            c = ((a & b) << 1) & x # 获得进位
            a = a ^ b  # 不进位加法
            b = c
        
        # 0x7fffffff 是最大的正数的补码 
        # ~(a ^ 0xffffffff) 是将 32 位以上的位取反，1 至 32 位不变, 处理补码 a 为负数的情况
        return a if a <= 0x7fffffff else ~(a ^ x)