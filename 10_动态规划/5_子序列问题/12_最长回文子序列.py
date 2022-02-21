"""
    题目描述:
        给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

        子序列定义为: 不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

    链接: https://leetcode-cn.com/problems/longest-palindromic-subsequence
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
            1. dp[i][j]:
                [i, j] 内最长回文子序列长度；
            2. 递推:
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = 1
                    elif j - i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = dp[i+1][j-1]
            3. 初始化:
                dp[i][j] = 0
            4. 遍历顺序:
                从下到上，从左到右
        """
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = j - i + 1
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    # dp[i][j] = dp[i+1][j-1]
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        return dp[0][len(s)-1]