"""题目描述:

    请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

    实现 MyQueue 类：
        void push(int x) 将元素 x 推到队列的末尾
        int pop() 从队列的开头移除并返回元素
        int peek() 返回队列开头的元素
        boolean empty() 如果队列为空，返回 true ；否则，返回 false
     
    说明：
        你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
        你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
        提示：

    提示：
        1 <= x <= 9
        最多调用 100 次 push、pop、peek 和 empty
        假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

    进阶：
        你能否实现每个操作均摊时间复杂度为 O(1) 的队列？
        换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

    链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
"""

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """将元素 x 推到队列的末尾"""
        self.stack_in.append(x)

    def pop(self) -> int:
        """从队列的开头移除并返回元素"""
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        """返回队列开头的元素"""
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """如果队列为空，返回 true ；否则，返回 false"""

        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        
        return False
