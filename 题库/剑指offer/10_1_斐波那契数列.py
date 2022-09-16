from typing import List

class Solution:
    def fib(self, n: int) -> int:
        """递推秀操作"""
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b  # 从右向左赋值的
        return a % 1000000007  # python 没有越界限制

    def fib(self, n: int) -> int:
        """dp递推"""
        if n <= 1:
            return n
        
        dp = [0, 1, 2]

        for i in range(2, n+1):
            dp[2] = (dp[0] + dp[1]) % 1000000007
            dp[0], dp[1] = dp[1], dp[2]
        
        return dp[2]

    def fib(self, n: int) -> int:
        """利用矩阵的快速幂计算
            [fn+1, fn] = [[1 1][1 0]] * [fn, fn-1]
        """
        MOD = 1000000007

        def multiply_martix(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c
        
        def martix_pow(a, n):
            ans = [[1, 0], [0, 1]] # 对角矩阵
            while n > 0:
                if n & 1:
                    ans = multiply_martix(ans, a)
                
                a = multiply_martix(a, a)
                n >>= 1
            return ans
        
        if n < 2:
            return n

        ans = martix_pow([[1, 1], [1, 0]], n-1)
        return ans[0][0]  # f(0) = 0, f(1) = 1