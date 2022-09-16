"""
    题目描述:
        给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
        其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

    链接: https://leetcode-cn.com/problems/daily-temperatures
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            单调栈解法:
                - 单调栈里存放的元素是什么？
                    存放元素的下标i就可以了，如果需要使用对应的元素，直接T[i]就可以获取。

                - 单调栈里元素是递增呢？ 还是递减呢？(从栈头到栈底的顺序)
                    使用递增循序（再强调一下是指从栈头到栈底的顺序），
                    因为只有递增的时候，加入一个元素i，才知道栈顶元素在数组中右面第一个比栈顶元素大的元素是i
                
            使用单调栈主要有三个判断条件: 
                当前遍历的元素T[i]小于栈顶元素T[st.top()]的情况
                当前遍历的元素T[i]等于栈顶元素T[st.top()]的情况
                当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况

            链接: https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
        """
        result = [0] * len(temperatures)
        stack = [0]  # 递增栈，从栈头到栈底是增加的

        for i in range(1, len(temperatures)):
            if temperatures[i] < temperatures[stack[-1]]:
                # 当前遍历元素小于栈顶元素，入栈
                stack.append(i)
            elif temperatures[i] == temperatures[stack[-1]]:
                # 当前遍历元素等于栈顶元素，入栈
                stack.append(i)
            elif temperatures[i] > temperatures[stack[-1]]:
                # 当前遍历元素大于栈顶元素
                # 栈顶元素持续出栈，直到栈顶元素小于等于当前元素为止
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    result[idx] = i - idx
                
                stack.append(i)

        # stack 中剩余的下标，对应温度在右边均为最大，因此均为0，符合初始化值
        return result