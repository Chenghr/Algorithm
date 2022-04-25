"""
    0,1,···,n-1这n个数字排成一个圆圈，
    从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。
    求出这个圆圈里剩下的最后一个数字。

    例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
    则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """使用数学推导 + dp

            长为 n 的序列会删除第 m%n 个元素，剩下长 n-1 的序列，继续删除；
            假设 n-1 的序列删除结果为 x,则 n 的序列的结果为 从 m % n 开始数的第 x 个元素:
                （m % n + x）% n = (m + x) % n
            
            上述分析可以改成 dp
            f(n, m) = (m + f(n-1, m)) % n
            f(1, m) = 0
        """
        if n == 1:
            return 0

        ans = 0
        for i in range(2, n+1):
            ans = (m + ans) % i  # 序列长为 i
        
        return ans

    def lastRemaining(self, n: int, m: int) -> int:
        """暴力模拟
        """
        tag, count = [True] * n, n

        num, step = 0, 1
        while count > 1:
            while step < m:
                num = (num+1) % n

                if tag[num]:
                    step += 1 

            tag[num] = False
            count -= 1
            step = 0

        return tag.index(True)