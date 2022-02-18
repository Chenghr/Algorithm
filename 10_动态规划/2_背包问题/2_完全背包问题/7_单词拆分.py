"""
    题目描述:
        给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
        请你判断是否可以利用字典中出现的单词拼接出 s 。

    注意: 不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

    链接: https://leetcode-cn.com/problems/word-break
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。
            拆分时可以重复使用字典中的单词，说明就是一个完全背包。

            1. dp[j]: 在 s 上能否到达第 j 个下标, bool;
            2. 递推:
                if not dp[j]:
                    if dp[j - len(word[i])] and s[j-len(word[i]): j] == word[i]:
                        dp[j] = True
                
            3. dp[0] = True, dp[j] = False
            4. 完全背包问题的遍历形式 -- wrong
                本题必须要先遍历背包容量，再遍历物品；

                如果要是外层for循环遍历物品，内层for遍历背包，
                就需要把所有的子串都预先放在一个容器里。好像很麻烦。。。

        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # 本题必须要先遍历背包容量，再遍历物品
        for j in range(len(s)+1):
            for word in wordDict:
                if j >= len(word) and not dp[j]:
                    if  dp[j-len(word)] and s[j-len(word): j] == word:
                        dp[j] = True

        # for word in wordDict:
        #     for j in range(len(word), len(s)+1):
        #         if not dp[j]:
        #             if  dp[j-len(word)] and s[j-len(word): j] == word:
        #                 dp[j] = True
        # 这样写会报错，eg: "applepenapple", ["apple","pen"]
        
        return dp[len(s)]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
            另外本题还可以采用递归的方式来做；
            在递归中会有很多重复计算，我们可以使用数组保存递归过程中的计算结果，这种方法称之为记忆化递归。
        """
        memory = [-1] * len(s)

        def backtracking(startIndex: int) -> bool:
            nonlocal s, wordDict, memory

            if startIndex >= len(s):
                return True
            
            if memory[startIndex] != -1:
                #  如果memory[startIndex]不是初始值了，直接使用其结果
                if memory[startIndex] == 1:
                    return True
                else:
                    return False
            
            for i in range(startIndex, len(s)):
                word = s[startIndex: i-startIndex+1]

                if word in wordDict and backtracking(i+1):
                    memory[startIndex] = 1
                    return True
            
            memory[startIndex] = 0
            return False

        return backtracking(0)

example = Solution()
result = example.wordBreak("applepenapple", ["apple","pen"])
print(result)
