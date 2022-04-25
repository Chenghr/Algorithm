"""
    编写一个函数，输入是一个无符号整数（以二进制串的形式），
    返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
            1. 位运算
                n & (n-1)，其预算结果恰为把 n 的二进制位中的最低位的 1 变为 0 之后的结果。
                注意这里的时间复杂度是 O(logn);

            2. 直接循环检查给定整数 n 的二进制位的每一位是否为 1。

                具体代码中，当检查第 i 位时，我们可以让 n 与 2^i 进行与运算，
                当且仅当 n 的第 i 位为 1 时，运算结果不为 0。

        """
        count = 0

        while n > 0:
            count += 1
            n = n & (n-1)  # 消去 n 的最后一位 1

        return count

        # ret = sum(1 for i in range(32) if n & (1 << i)) 
        # return ret