"""
    题目描述:
        给你一个字符串 s，找到 s 中最长的回文子串。
    
    链接: https://leetcode-cn.com/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            分析:
                返回的是子串，不是长度；
                子串要求连续；而非子序列，注意二者差别。

            回文字符串可视为以一个或者两个字符为中心，向两边拓展的字符串；
            因此我们可以在一轮for循环中遍历s，向两边拓展；
        """

        def extend(s: str, left: int, right: int) -> int:

            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # 返回当前回文子串的长度
            return right - left - 1  

        max_length = 0
        begin, end = 0, 0

        for i in range(len(s)):

            len_1 = extend(s, i, i)

            if len_1 > max_length:
                max_length = len_1
                begin = i - int(len_1 / 2)
                end = i + int(len_1 / 2)

            if i != len(s)-1 and s[i] == s[i+1]:
                len_2 = extend(s, i, i+1)

                if len_2 > max_length:
                    max_length = len_2
                    begin = i - int((len_2 - 2)/2)
                    end = i + 1 + int((len_2 - 2)/2)

        return s[begin: end+1]
    
    def longestPalindrome(self, s: str) -> str:
        """
            动态数组；
            1. dp[i][j]: 下标 i 到 下标 j 是否为回文字符串
            2. 递推:
                if i == j:
                    dp[i][j] == true
                if j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                if j - i >= 2:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = False
            3. 初始化:
                dp[i][j] = False
            4. 遍历顺序:
                从下向上，从左到右
        """
        dp = [[False] * len(s) for _ in range(len(s))]

        max_length = 0
        begin, end = 0, 0

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = False
                
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    begin = i
                    end = j
        
        return s[begin: end+1]
