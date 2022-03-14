"""
    题目描述:
        设计一个找到数据流中第 k 大元素的类（class）。
        注意是排序后的第 k 大元素，不是第 k 个不同的元素。

    请实现 KthLargest 类：
        KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
        int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

    链接: https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
"""

from typing import List
from queue import PriorityQueue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.pq = PriorityQueue()
        self.k = k

        for num in nums:
            self.pq.put(num)

            if self.pq.qsize() > k:
                _ = self.pq.get()


    def add(self, val: int) -> int:
        self.pq.put(val)
        
        if self.pq.qsize() > self.k:
            _ = self.pq.get()

        num = self.pq.get()
        self.pq.put(num)

        return num

