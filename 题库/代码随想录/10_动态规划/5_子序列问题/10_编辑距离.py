"""
    题目描述:
        给你两个单词 word1 和 word2， 
        请返回将 word1 转换成 word2 所使用的最少操作数。

        你可以对一个单词进行如下三种操作:
            插入一个字符
            删除一个字符
            替换一个字符
    
    链接: https://leetcode-cn.com/problems/edit-distance
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            1. dp[i][j]:
                以 i-1 为结尾的字符串 word1，转换为以 j-1 位结尾的字符串 word2，
                所需要编辑的最少次数。
            
            2. 递推:
                首先要明确一点:
                    添加元素和删除元素操作数相同;
                    word2添加一个元素，相当于word1删除一个元素;
                    例如 word1 = "ad" ，word2 = "a"，word1删除元素'd' 和 word2添加一个元素'd'，
                    变成word1="a", word2="ad"， 最终的操作数是一样。
                
                if word1[i - 1] == word2[j - 1]:
                    不用任何编辑
                    dp[i][j] = dp[i - 1][j - 1];
                else:
                    case1: 
                        word1 删除一个元素; 就是以下标 i - 2 为结尾的 word1 与 j-1 为结尾的 word2 的最近编辑距离再加上一个操作。
                        dp[i][j] = dp[i-1][j] + 1
                    case2:
                        word2删除一个元素; 就是以下标 i - 1 为结尾的 word1 与 j-2 为结尾的 word2 的最近编辑距离再加上一个操作。
                        dp[i][j] = dp[i][j-1] + 1
                    case3:
                        word1 替换 word1[i - 1]，使其与 word2[j - 1] 相同，此时不用增加元素，
                        那么以下标 i-2 为结尾的 word1 与 j-2 为结尾的 word2 的最近编辑距离加上一个替换元素的操作;
                        dp[i][j] = dp[i-1][j-1] + 1
            
            3. 初始化
                dp[i][0] = i; dp[0][j] = j

            4. 遍历顺序:
                从上到下，从左到右
        """ 

        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0] = i

        for j in range(len(word2)+1):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

        return dp[-1][-1]        