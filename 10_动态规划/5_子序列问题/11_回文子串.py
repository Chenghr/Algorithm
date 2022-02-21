"""
    题目描述:
        给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
        回文字符串 是正着读和倒过来读一样的字符串。
        子字符串 是字符串中的由连续字符组成的一个序列。 
        具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

    链接: https://leetcode-cn.com/problems/palindromic-substrings
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
            动态规划:
            1. dp[i][j] -> bool:
                区间范围 [i, j] (注意左闭右闭)的子串是否为回文子串
            
            2. 递推:
                if s[i] != s[j]:
                    dp[i][j] = False

                elif s[i] == s[j]:
                    if i == j: （只有一个字符）
                        dp[i][j] = True
                    elif j - i = 1: (两个相同字符)
                        dp[i][j] == True
                    elif j - i >= 2: 
                        dp[i][j] = dp[i+1][j-1]
            
            3. 初始化:
                dp[i][j] = False
            
            4. 遍历顺序:
                根据递推公式, dp[i][j] 依赖于 dp[i+1][j-1];
                因此遍历顺序为 从下到上，从左到右
        """

        dp = [[False] * len(s) for _ in range(len(s))]

        result = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                # 区间右边大于左边
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        result += 1
                        dp[i][j] = True
            
        return result
    
    def countSubstrings(self, s: str) -> int:
        """
            双指针法:
                首先确定回文串，就是找中心然后想两边扩散看是不是对称的就可以了。

                在遍历中心点的时候，要注意中心点有两种情况: 
                    一个元素可以作为中心点，两个元素也可以作为中心点。
        """

        def extend(s: str, i: int, j: int) -> int:
            # 以 [i, j]为中心，向两边拓展
            res = 0

            while i >= 0 and j <= len(s)-1 and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            
            return res
        
        result = 0

        for i in range(len(s)):
            result += extend(s, i, i)  # 以 i 为中心
            result += extend(s, i, i+1)  # 以 i，i+1 为中心
        
        return result
             