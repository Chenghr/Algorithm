"""
    题目描述:
        给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

        字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
        （例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

        题目数据保证答案符合 32 位带符号整数范围。

    链接: https://leetcode-cn.com/problems/distinct-subsequences
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            如果本题为连续序列，则考虑使用 KMP 算法；

            动态规划:
            1. dp 定义:
                dp[i][j]: 以 i-1 为结尾的 s 子序列中出现以 j-1 为结尾的 t 的个数为dp[i][j]。
            
            2. 递推公式:
                if s[i-1] == t[j-1]:
                    dp[i][j] 可以选择用 s[i-1] 参与匹配: dp[i-1][j-1]
                    dp[i][j] 也可以选择不用 s[i-1] 参与匹配: dp[i-1][j]
                    因此: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    eg: 'bagg', 'bag'
                else:
                    dp[i][j] 只能不用 s[i-1] 参与匹配，即:
                        dp[i][j] = dp[i-1][j]
            
            3. 初始化（抓住具体定义）:
                dp[i][0]: 以i-1为结尾的s可以随便删除元素，出现空字符串的个数; 均为 1
                dp[0][j]: 空字符串s可以随便删除元素，出现以j-1为结尾的字符串t的个数; 均为 0
                dp[0][0]: 空字符串s，可以删除0个元素，变成空字符串t; 为 1。
            
            4. 顺序:
                从上到下，从左到右
        """
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]