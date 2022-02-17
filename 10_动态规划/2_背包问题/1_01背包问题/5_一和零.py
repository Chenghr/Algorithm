"""
    题目描述:
        给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
        请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

        如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

    链接: https://leetcode-cn.com/problems/ones-and-zeroes
"""

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
            首先遍历每个字符串，计算出含有 0 和 1 的个数，存储为 weight 数组
            每个字符串的价值为 1

            1. dp[i][j]: 最多含有 i 个0和 j 个1的背包拥有的最大价值；
            2. 递推:
                dp[i][j] = max(dp[i][j], dp[i-w[k][0]][j-w[k][1]] + 1)
            3. 初始化:
                全为 0 
            4. 遍历:
                str 从小到大，i，j 逆序
        """
        
        # dp = [[0]* (n+1)] * (m+1)
        # 注释的操作不可取，等于是将一维列表复制了 m+1 次，对任意一行的修改会导致所有行的修改，不可用
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        print(len(dp), len(dp[0]))
        for str in strs:
            zeros = str.count('0')
            ones = len(str) - zeros

            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        
        return dp[m][n]
    
example = Solution()
result = example.findMaxForm(["10","0001","111001","1","0"], 5, 3)
print(result)
