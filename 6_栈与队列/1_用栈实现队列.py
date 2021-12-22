"""
    题目描述:
        请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）
    
    实现 MyQueue 类：
        - void push(int x) 将元素 x 推到队列的末尾
        - int pop() 从队列的开头移除并返回元素
        - int peek() 返回队列开头的元素
        - boolean empty() 如果队列为空，返回 true ；否则，返回 false
 

    说明：
        你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
        你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
         

    进阶：
        你能否实现每个操作均摊时间复杂度为 O(1) 的队列？

    链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
"""

"""
    思路:
        采用两个栈维护队列，stack_in 以及 stack_out
"""

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def _transfer(self):
        """将 stack_in 的元素转移到 stack_out 中"""

        for _ in range(len(self.stack_in)): 
            self.stack_out.append(self.stack_in.pop())

    def push(self, x: int) -> None:
        """将元素 x 推到队列的末尾"""
        self.stack_in.append(x)

    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        if self.empty:
            return None
        
        if len(self.stack_out) == 0:
            self._transfer()
        
        return self.stack_out.pop()

    def peek(self) -> int:
        """返回队列开头的元素"""
        if self.empty:
            return None
        
        if len(self.stack_out) == 0:
            self._transfer()
        
        return self.stack_out[-1]

    def empty(self) -> bool:
        """如果队列为空，返回 true ；否则，返回 false"""

        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True

        return False

