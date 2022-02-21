"""
    题目描述:
        给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
        如果不存在 公共子序列 ，返回 0 。

        一个字符串的 子序列 是指这样一个新的字符串:
            它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
        两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

    链接: https://leetcode-cn.com/problems/longest-common-subsequence
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            1. dp[i][j]: text1中第 i 个字符、text2中第 j 个字符结尾的最长公共子序列;
            2. 递推
                if text1[i] == text[j]:
                    dp[i][j] = max(前 i-1 行 前 j-1 列 dp值) + 1
            3. 初始化:
                dp[i][j] = 0
            4. 顺序遍历
        """
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        col_max = [0] * (len(text2)+1)

        for i in range(1, len(text1)+1):
            for j in range(len(text2), 0, -1):
                # 避免 col_max 出现本轮覆盖的情况
                # eg:"abcba", "abcbcba"
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(col_max[:j]) + 1
                    col_max[j] = max(col_max[j], dp[i][j])


            # for j in range(1, len(text2)+1):
            #     if text1[i-1] == text2[j-1]:
            #         dp[i][j] = max(col_max[:j]) + 1
            #         col_max[j] = max(col_max[j], dp[i][j])

        return max(col_max)

        """
            1. dp[i][j]: 
                长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
            2. 递推:
                if (text1[i - 1] == text2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        """