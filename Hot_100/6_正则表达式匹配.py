"""
    题目描述:
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
            '.' 匹配任意单个字符
            '*' 匹配零个或多个前面的那一个元素

        所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

    链接: https://leetcode-cn.com/problems/regular-expression-matching
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            动态规划:
            1. dp[i][j]:
                s 的前 i 个字符与 p 中的前 j 个字符是否匹配
            
            2. 递推公式:（本题难点）
                对于 * ，不要单独考虑，从字母 + * 的组合来考虑；
                
                case1: p[j] != '*'
                    dp[i][j] = (dp[i-1][j-1] & match(s[i], p[j]))
                
                case2: p[j] == '*'
                    # 考虑 s[i] 和 p[j-1] 的匹配关系
                    if not match(s[i], p[j-1]):
                        # * 可以将前一个字符消去:
                        dp[i][j] = dp[i][j-2]
                    
                    elif match(s[i], p[j-1]):
                        # 匹配后可以视为在 s 中删去 1 个字符，p 中不变（可以多次匹配）
                        # 特别的，匹配 0 次的情况也要考虑，且此时不等同于不匹配，eg: a, a*a; ba, bc*a;
                        dp[i][j] = dp[i][j] or dp[i][j-2]  # 匹配 0 次
                        dp[i][j] = dp[i][j] or dp[i-1][j]  # 匹配多次

            3. 初始化:
                 dp[0][0]:
                    True;  # 两个空字符串的匹配

                 dp[i][0]:
                    False,  # s 中前 i 个字符不可能为空字符串

                 dp[0][j]:
                    # s一个字符不选，考虑 p 中带 * 的情况，* 可以抵消前一个字符
                    if p[j-1] == '*':
                        dp[0][j] = dp[0][j-2]
                    
            4. 遍历顺序:
                从上到下，从左到右
        """
        def match(i, j):
            """判断 s 中第 i 个字符和 p 中第 j 个字符是否匹配，保证不越界
            """
            nonlocal s, p

            if p[j-1] == '.' or s[i-1] == p[j-1]:
                return True
            else:
                return False

        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        dp[0][0] = True

        for j in range(2, len(p)+1):
            # s一个字符不选，考虑p中带*的情况，因为*可以不匹配
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = (dp[i-1][j-1] & match(i, j))
                elif p[j-1] == '*':
                    if not match(i, j-1):
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = (dp[i][j-2] | dp[i-1][j])
        
        return dp[-1][-1]
        