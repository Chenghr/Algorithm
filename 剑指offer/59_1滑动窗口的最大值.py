"""
    给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
    你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""

from typing import List
from collections import deque

class MyQueue:
    def __init__(self) -> None:
        self.que = deque()
    
    def getMaxVal(self):
        if not self.que:
            raise ValueError('Queue is empty')
        
        return self.que[0]
    
    def put(self, val):
        while self.que and self.que[-1] < val:
            self.que.pop()
        
        self.que.append(val)
    
    def pop(self, val):
        if self.que and self.que[0] == val:
            self.que.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """单调队列
        """
        if not nums:  # 边界处理
            return []

        que = MyQueue()

        for i in range(k):
            que.put(nums[i])
        
        ans = [que.getMaxVal()]
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.put(nums[i])
            ans.append(que.getMaxVal())
        
        return ans