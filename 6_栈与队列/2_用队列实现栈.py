"""
    题目描述:
        请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）
    
    实现 MyStack 类:
        - void push(int x) 将元素 x 压入栈顶。
        - int pop() 移除并返回栈顶元素。
        - int top() 返回栈顶元素。
        - boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

    注意:
        你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
        你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

    进阶:
        你能否实现每个操作均摊时间复杂度为 O(1) 的队列？

    链接: https://leetcode-cn.com/problems/implement-stack-using-queues
"""

"""
    思路:
        两个队列实现栈，第二个队列就是一个维护的作用；
        将第一个队列除了最后一个元素外其他元素均转移到第二个队列，将最后一个元素输出，再将其他元素转移回第一个队列，即实现栈。
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.queue_in = deque()  # 存所有数据
        self.queue_out = deque()  # 仅在 pop 时用到

    def push(self, x: int) -> None:
        """将元素 x 压入栈顶"""
        self.queue_in.append(x)

    def pop(self) -> int:
        """移除并返回栈顶元素
        
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
        
        tip: 这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
             stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None
        
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        
        # 交换in和out
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()    

    def top(self) -> int:
        """返回栈顶元素"""
        if self.empty():
            return None
        
        return self.queue_in[-1]

    def empty(self) -> bool:
        """如果栈是空的，返回 true ；否则，返回 false """

        if len(self.queue_in) == 0 and len(self.queue_out) == 0:
            return True

        return False
