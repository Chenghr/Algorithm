"""
    题目描述:
        给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

        字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
        （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    进阶:
        如果有大量输入的 S，称作 S1, S2, ... , Sk 
        其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

    链接: https://leetcode-cn.com/problems/is-subsequence
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
            简单思路:
                判断 s 和 t 的最长公共子序列，如果长度等于 len(s)，则 s 为 t 的子序列。
            
            1. dp[i][j]:
                表示以下标 i-1 为结尾的字符串s，和以下标 j-1 为结尾的字符串t，相同子序列的长度为dp[i][j]。
            
            2. 递推:
                if (s[i - 1] == t[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 此时相当于t要删除元素，t如果把当前元素t[j - 1]删除
                    dp[i][j] = dp[i][j - 1]
            
            3. 初始化:
                dp[i][j] = 0
        """
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if (s[i - 1] == t[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 此时相当于t要删除元素，t如果把当前元素t[j - 1]删除
                    dp[i][j] = dp[i][j - 1]
        
        return dp[-1][-1] == len(s)
    
    def isSubsequence(self, s: str, t: str) -> bool:
        """
            本题还可以使用双指针的思路来实现；时间复杂度就是 O(n)
        """
        j = 0

        for i in range(len(t)):
            if j == len(s):
                break

            if t[i] == s[j]:
                j += 1
        
        return j == len(s)