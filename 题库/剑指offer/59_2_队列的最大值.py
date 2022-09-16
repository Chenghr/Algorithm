"""
    请定义一个队列并实现函数 max_value 得到队列里的最大值，
    要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

    若队列为空，pop_front 和 max_value 需要返回 -1
"""

from queue import Queue
from collections import deque

class MaxQueue:

    def __init__(self):
        self.que = Queue()
        self.maxQue = deque()

    def max_value(self) -> int:
        if self.que.qsize() == 0:
            return -1
        
        return self.maxQue[0]

    def push_back(self, value: int) -> None:
        self.que.put(value)

        while self.maxQue and self.maxQue[-1] < value:
            _ = self.maxQue.pop()
        
        self.maxQue.append(value)

    def pop_front(self) -> int:
        if self.que.qsize() == 0:
            return -1
        
        val = self.que.get()
        
        if val == self.maxQue[0]:
            _ = self.maxQue.popleft()

        return val