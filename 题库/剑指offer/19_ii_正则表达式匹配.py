"""
    请实现一个函数用来匹配包含'. '和'*'的正则表达式。
    模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            动态规划
            dp[i][j]: s 中前 i 个字符 和 p 中前 j 个字符是否匹配；

            if s[i] == p[j] or p[j] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == '*':
                if s[i] == p[j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-2]  # '*'可以重复匹配，注意这里也可以不匹配
                else:
                    dp[i][j] = dp[i][j-2]  # '*' 取 0
            else:
                dp[i][j] = False
            
            dp[0][0] = True; 
            
            for j in range(1, len(p)+1):
                if j >= 2 and p[j] == '*':
                    dp[0][j] = dp[0][j-2]

            dp[i][0] = False
        """
        def match(i, j):
            nonlocal s, p

            if p[j-1] == '.' or s[i-1] == p[j-1]:
                return True

            return False

        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        dp[0][0] = True

        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    if not match(i, j-1):
                        dp[i][j] = dp[i][j-2]  # '*'前面的字符不匹配时，选择取 0
                    else:
                        # '*'前面的字符匹配，但是仍可以选择取 0 次或者多次，这里取 0 次不可省
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                else:
                    dp[i][j] = match(i, j) and dp[i-1][j-1]
        
        return dp[-1][-1]
