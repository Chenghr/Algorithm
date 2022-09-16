"""
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
"""

from queue import PriorityQueue
from heapq import *

class MedianFinder:
    """这种实现方式开销更小"""
    def __init__(self):
        self.large = [] # 小顶堆，保存较大的一半
        self.small = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.large) != len(self.small):
            heappush(self.large, num)
            heappush(self.small, -heappop(self.large))
        else:  # 默认加入大顶堆
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        return self.large[0] if len(self.large) != len(self.small) else (self.large[0] - self.small[0]) / 2.0


class MedianFinder:

    def __init__(self):
        """initialize your data structure here.
        """
        self.large = PriorityQueue()  # 存储较大的数，使用小顶堆
        self.small = PriorityQueue()  # 存储较小的数，使用大顶堆

    def addNum(self, num: int) -> None:
        # 保证两个堆之间的数差距不超过 1
        if self.large.qsize() <= self.small.qsize():  # 优先加入较大的一堆中
            self.small.put(-num)  #直接存相反数，避免额外的空间开销
            num_large = -self.small.get()  # 保证 small 中的数均小于 large 中的数
            self.large.put(num_large)
        else:
            self.large.put(num)
            num_small = self.large.get()  # 保证 small 中的数均小于 large 中的数
            self.small.put(-num_small)

    def findMedian(self) -> float:
        if self.small.qsize() == self.large.qsize():
            # 取均值
            small = -self.small.get()
            large = self.large.get()

            self.small.put(-small)
            self.large.put(large)

            return (small + large) / 2.0
        else:  # 默认加入较大的一堆中，因此直接从中获取中位数即可
            midNum = self.large.get()
            self.large.put(midNum)
            return midNum