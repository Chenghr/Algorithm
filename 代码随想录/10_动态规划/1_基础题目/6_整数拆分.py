"""
    题目描述:
        给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
        返回 你可以获得的最大乘积 。

    链接: https://leetcode-cn.com/problems/integer-break/
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        """
            1. dp[i]: 分拆数字 i 可以得到的最大乘积；
            2. 递推公式:
                对于数字 i ，可以遍历 1 到 i-1；
                中间每个数可以选择分拆或者不继续分拆，从中选择较大的值；
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j]), j in (1, i-1)
            3. 初始化:
                n >= 2; 因此 dp[2] = 1, 为了合理，dp[0] = dp[1] = 1
            4. 遍历顺序:
                dp[i] 取决于 1 ~ i-1 之间的值，因此从前向后遍历
        """
        dp = [1] * (n+1)

        # 注意起始下标
        for i in range(3, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))
        
        return dp[n]