"""
    题目描述:
        给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
        每步可以删除任意一个字符串中的一个字符。
    
    链接: https://leetcode-cn.com/problems/delete-operation-for-two-strings/
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            将两个单词只通过删除操作变成相同的单词，求最小步数，即求两个单词的最长公共子序列；
            然后用两个单词的长度减去最长公共子序列的长度，结果相加即可。

            dp[i][j]: word1 中前 i-1 个字符和 word2 中前 j-1 个字符的最长公共子序列长度；
        """
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        steps = len(word1) + len(word2) - dp[-1][-1]*2

        return 
        
        """
            另一种思路:
            1. dp[i][j]:
                以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
            
            2. 递推:
                word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1];
                
                word1[i - 1] != word2[j - 1]:
                    case1: 删 word1[i - 1]，最少操作次数为 dp[i - 1][j] + 1;
                    case2: 删 word2[j - 1]，最少操作次数为 dp[i][j - 1] + 1;
                    case3: 同时删 word1[i - 1]和word2[j - 1]，操作的最少次数为 dp[i - 1][j - 1] + 2
                    取其中最小值。
            
            3. 初始化:
                dp[i][0] = i; dp[0][j] = j.
        """