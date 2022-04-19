"""
    题目描述:
        设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

        实现 MinStack 类:
            MinStack() 初始化堆栈对象。
            void push(int val) 将元素val推入堆栈。
            void pop() 删除堆栈顶部的元素。
            int top() 获取堆栈顶部的元素。
            int getMin() 获取堆栈中的最小元素。

    链接: https://leetcode-cn.com/problems/min-stack
"""

class MinStack:
    """使用辅助栈的解法；记录当前最小值
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        _ = self.stack.pop()
        _ = self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")

        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")

        return self.minStack[-1]

class MinStack:
    """不使用额外空间，记录当前栈顶元素和最小值之间的距离
    """
    def __init__(self):
        self.stack = []
        self.minVal = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)  # 注意这里要添加 0，表示 diff
            self.minVal = val
        else:
            diff = val - self.minVal
            self.stack.append(diff)

            if diff < 0:
                self.minVal = val 

    def pop(self) -> None:
        if len(self.stack) == 0:
            return 
        
        if self.stack[-1] >= 0:
            _ = self.stack.pop()
        else:
            diff = self.stack.pop()
            self.minVal -= diff

    def top(self) -> int:
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")

        if self.stack[-1] < 0:
            topVal = self.minVal
        else:
            topVal = self.minVal + self.stack[-1]

        return topVal

    def getMin(self) -> int:
        if len(self.stack) == 0:
            raise IndexError("Stack is Empty")

        return self.minVal
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()