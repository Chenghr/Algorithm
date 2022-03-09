"""
    题目描述:
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足:
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。

    提示:
        1 <= s.length <= 104
        s 仅由括号 '()[]{}' 组成

    链接: https://leetcode-cn.com/problems/valid-parentheses
"""
class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []

        for char in s:
            if char == '(' or char == '[' or char =='{':
                char_stack.append(char)

            elif char == ')' :
                if len(char_stack) > 0 and char_stack[-1] == '(':
                    pop = char_stack.pop()
                else:
                    return False

            elif char == ']' :
                if len(char_stack) > 0 and char_stack[-1] == '[':
                    pop = char_stack.pop()
                else:
                    return False

            elif char == '}' :
                if len(char_stack) > 0 and char_stack[-1] == '{':
                    pop = char_stack.pop()
                else:
                    return False
        
        if len(char_stack) == 0:
            return True

        return False
                    