"""
    题目描述:
        给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
    
    链接: https://leetcode-cn.com/problems/longest-valid-parentheses/
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            动态规划:
            
            1. dp[i]: 以下标 i 结尾的最长有效括号子串的长度；
            2. 递推公式:
                if s[i] == '(': dp[i] = 0
                if s[i] == ')':
                    # 向左找最近的合法左括号
                    j = i-1
                    while j > 0:
                        if dp[j] > 0: 
                            # 说明前面的连续 dp[j] 个字符不能动
                            j -= dp[j]
                        elif dp[j] == 0 and s[j] == '(':
                            # 找到合法的左括号；
                            dp[i] = dp[j-1] + (j-i+1)
                        elif dp[j] == 0 and s[j] == ')':
                            dp[i] = 0

            3. 初始化: 
                dp[0] = 0, dp[1] = 2/0，dp[i] = 0
            4. 递推方向:
                从前到后
        """
        """
            动态规划优化:
            
            上述递推公式优化一下，情况如下:
                if s[i] == '(': dp[i] = 0
                if s[i] == ')' and s[i-1] == '(': dp[i] = dp[i-2] + 2
                if s[i] == ')' and s[i-1] == ')': 
                    if s[i-dp[i-1]-1] == '(':
                        # 这里要注意 i-dp[i-1]-2 越界的处理
                        dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
        """
        if len(s) < 2:
            return 0

        dp = [0] * len(s)

        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
        
        maxLength = max(0, dp[1])
        for i in range(2, len(s)):
            if s[i] == ')':
                j = i-1
                while j > -1:
                    if dp[j] > 0:
                        # 跳过不可用括号
                        j -= dp[j]
                    elif s[j] == '(':
                        # 找到最近可用左括号
                        if j == 0:
                            dp[i] = i - j + 1
                        else:
                            dp[i] = dp[j-1] + i-j+1
                        
                        maxLength = max(maxLength, dp[i])
                        break
                    
                    elif s[j] == ')':
                        # 找到另一个非法右括号，则搜索结束
                        break
                
                # dp[i] 默认为0

        return maxLength
    
    def longestValidParentheses(self, s: str) -> int:
        """
            栈
            保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」
        """
        stack = []
        maxLength = 0

        # 找出每个字符的匹配下标，不含匹配项的下标为 0
        for i in range(len(s)):
            if len(stack) == 0 or s[i] == '(':
                stack.append(i)
            else:
                # 到来的是 ')'
                if s[stack[-1]] == '(':
                    # 以下标 i 结尾的最长有效括号长度的起点元素为栈顶元素的下标
                    stack.pop()
                    if len(stack) == 0:
                        maxLength = max(maxLength, i+1)
                    else:
                        maxLength = max(maxLength, i-stack[-1])
                else:
                    stack.append(i)
        
        return maxLength


