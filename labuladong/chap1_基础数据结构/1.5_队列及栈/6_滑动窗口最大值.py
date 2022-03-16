"""
    题目描述:
        给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
        返回滑动窗口中的最大值。

    提示:
        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        1 <= k <= nums.length
    
    链接: https://leetcode-cn.com/problems/sliding-window-maximum/
"""

from collections import deque

class Myque:
    """
        单调队列的实现:
            nums 中的每个元素最多也就被 push_back 和 pop_back 各一次，没有任何多余操作，
            所以整体的复杂度还是 O(n)。
        
        有辅助队列，空间复杂度为 O(k)。
    """
    def __init__(self):
        self._que = deque()
    
    def front(self):
        if not self._que:
            return self._que[0]
        
        raise ValueError('queue is empty()')
    
    def push(self, num):
        
        while self._que and self._que[-1] < num:
            _ = self._que.pop()

        self._que.append(num)

    def pop(self, num):
        if self._que and num == self._que[0]:
            _ = self._que.popleft()


class Solution:
    def maxSlidingWindow_violence(self, nums: list[int], k: int) -> list[int]:
        """
            维护一个单调队列，需要有如下功能:
                1. 向队列中添加元素；（窗口移动加入右边值）
                2. 删除队列中的指定元素；（窗口移动删除左边值）
                3. 获取队列中的最大值；（题目要求）
            
            根据 3 可知，单调队列的顺序为: 从队头到队尾单调递减
        """
        que = Myque()

        result = []

        for i in range(k):
            # 初始化滑动窗口
            que.push(nums[i])

        result.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])

            result.append(que.front())
        
        return result