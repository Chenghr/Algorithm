"""
    题目描述:
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

        有效字符串需满足：
            左括号必须用相同类型的右括号闭合。
            左括号必须以正确的顺序闭合。

    链接: https://leetcode-cn.com/problems/valid-parentheses
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """使用栈，进行括号匹配
        """
        stack = []

        for char in s:
            if char == '(' or char =='[' or char=='{':
                stack.append(char)
            elif char == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0