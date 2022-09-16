"""
    输入两个整数序列，第一个序列表示栈的压入顺序，
    请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。

    例如，序列 {1,2,3,4,5} 是某栈的压栈序列，
    序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
    但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
"""

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """简化写法"""
        stack, i = [], 0
        
        for num in pushed:
            stack.append(num) # num 入栈

            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1

        return not stack


    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
            模拟栈的压入压出操作，判断最后能否满足序列即可。

            题目规定 栈的所有数字均不相等 ，因此在循环入栈中，每个元素出栈的位置的可能性是唯一的
            （若有重复数字，则具有多个可出栈的位置）。

            题目指出 pushed 是 popped 的排列 。
            因此，无需考虑 pushed 和 popped 长度不同 或 包含元素不同 的情况。
        """
        stack = []
        i, j = 0, 0

        while j < len(popped):
            if stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            elif i < len(pushed):
                stack.append(pushed[i])
                i += 1
            else:
                # 进栈序列结束了，并且出栈序列无法满足
                return False
        
        return True