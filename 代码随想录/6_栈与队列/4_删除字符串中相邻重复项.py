"""
    题目描述:
        给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
        在 S 上反复执行重复项删除操作，直到无法继续删除。
        在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

    提示:
        1 <= S.length <= 20000
        S 仅由小写英文字母组成。

    链接: https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        char_stack = []

        for char in s:
            if len(char_stack) == 0 or char_stack[-1] != char:
                char_stack.append(char)
            else:
                pop = char_stack.pop()
        
        return "".join(char_stack)