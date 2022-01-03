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

"""
    思路:
    1. 暴力破解, O(n*k)

    2. 进阶 -- 考虑高效的维护窗口内的值队列
        - 单调队列: 
            按照单调递增/递减维护的队列。

            a. 提供的接口: 
                que.pop(滑动窗口中移除元素的数值);
                que.push(滑动窗口添加元素的数值);
                que.front()返回最值(本题为最大值);

            b. 一些注意点:
                队列内部不是通过排序实现的有序，否则和优先级队列没有区别;
                队列没有必要维护窗口里的所有元素，只需要维护有可能成为窗口里最大值的元素就可以了，同时保证队里里的元素数值是由大到小的;

            c. 具体的操作:
                pop(value): 如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作;
                push(value): 如果push的元素value大于入口元素的数值，那么就将队列入口的元素弹出，
                             直到push元素的数值小于等于队列入口元素的数值为止;
                保持如上规则，每次窗口移动的时候，只要问que.front()就可以返回当前窗口的最大值。
            
            d. 实现:
                采用 list 实现; (list.pop()的时间复杂度为 O(n))
                采用 collections.deque 实现;
"""

from collections import deque

class MyQueue_list:
    """基于 list 实现单调队列"""
    def __init__(self):
        self.queue = []
    
    def pop(self, value):
        """如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作.
        """
        if value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        """
        如果push的元素value大于入口元素的数值, 那么就将队列入口的元素弹出;
        直到push元素的数值小于等于队列入口元素的数值为止;
        """
        while len(self.queue) > 0 and self.queue[-1] < value:
            # list.pop 的时间复杂度为 O(n), 这里可以使用双端队列
            self.queue.pop(-1)


        self.queue.append(value)

    def front(self):
        return self.queue[0]

class MyQueue_deque:
    """基于 deque 实现单调队列"""
    def __init__(self):
        self.queue = deque()
    
    def pop(self, value):
        """如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作.
        """
        if value == self.queue[0]:
            delValue = self.queue.popleft()
    
    def push(self, value):
        """
        如果push的元素value大于入口元素的数值, 那么就将队列入口的元素弹出;
        直到push元素的数值小于等于队列入口元素的数值为止;
        """
        while len(self.queue) > 0 and self.queue[-1] < value:
            delValue = self.queue.pop()
        
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow_violence(self, nums: list[int], k: int) -> list[int]:
        """暴力破解
        """
        def findMax(nums: list[int]) -> int:
            maxNum = nums[0]
            for num in nums:
                if num > maxNum:
                    maxNum = num 
            return maxNum
        
        result, length = [], len(nums)-k+1

        for start in range(length):
            windows = nums[start: start+k]
            maxNum = findMax(windows)
            result.append(maxNum)
        
        return result

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        # que = MyQueue_list()
        que = MyQueue_deque()
        result = []

        # 初始化单调队列
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    # nums = [1]
    # k = 1

    result = solution.maxSlidingWindow(nums, k)
    print(result)