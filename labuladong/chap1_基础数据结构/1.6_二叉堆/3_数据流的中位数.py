"""
    题目描述:
        中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

        设计一个支持以下两种操作的数据结构：
            void addNum(int num) - 从数据流中添加一个整数到数据结构中。
            double findMedian() - 返回目前所有元素的中位数。
    
    进阶:
        如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
        如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

    链接: https://leetcode-cn.com/problems/find-median-from-data-stream
"""

from queue import PriorityQueue

class MedianFinder:
    
    def __init__(self):
        # 注意 PriorityQueue 默认为小顶堆
        self.large = PriorityQueue()
        self.samll = PriorityQueue()  # 大顶堆

    def addNum(self, num: int) -> None:
        """
            保证两个堆中相差元素不超过1；
            保证 small 中所有元素均小于 large 中元素
        """
        if self.samll.qsize() < self.large.qsize():
            # 添加到 small 中
            self.large.put(num)
            samll_num = self.large.get()  # 保证元素大小限制
            self.samll.put((-samll_num, samll_num))
        else:
            self.samll.put((-num, num))
            big_num = self.samll.get()[1]  # 使用 -num 作为优先级，以实现大顶堆
            self.large.put(big_num)

    def findMedian(self) -> float:
        """
            核心思路: 使用两个优先级队列

            中位数的定义将整体数据分为了较小的一堆和较大的一堆；
            因此我们可以使用一个小顶堆和一个大顶堆分别存储两部分数据，
            计算中位数时如果 n 为奇数，元素多的堆的堆顶元素即为中位数；n 为偶数，则取两个堆的堆顶元素，计算平均数即可。

            具体的:
                大顶堆: 存储较小的数据那一堆，命名为 small
                小顶堆: 存储较小的数据那一堆，命名为 large
            
            另外我们要维护两个堆的元素数目相差不大于1；小顶堆中的元素均小于大顶堆中的元素；

            维护元素大小:
                往 large 里添加元素，不能直接添加，而是要先往 small 里添加，然后再把 small 的堆顶元素加到large中；
                向small中添加元素同理。
        """
        if self.samll.qsize() == self.large.qsize():
            left = self.samll.get()[1]
            right = self.large.get()

            self.samll.put((-left, left))
            self.large.put(right)
            
            return (left + right) / 2
        elif self.samll.qsize() < self.large.qsize():
            mediaNum = self.large.get()
            self.large.put(mediaNum)

            return mediaNum
        elif self.samll.qsize() < self.large.qsize():
            mediaNum = self.samll.get()[1]
            self.samll.put((-mediaNum, mediaNum))

            return mediaNum

from sortedcontainers import SortedList

class MedianFinder:
    """
        使用有序集合来维护；
        将有序集合视为自动排序的数组，使用双指针指向有序集合中的中位数元素即可。
    """
    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right
        
        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2

"""
    进阶一:
        如果数据流中所有整数都在 0 到 100 范围内，
        利用计数排序统计每一类数的数目，并使用双指针维护中位数；
    
    进阶二:
        如果数据流中 99% 的整数都在 0 到 100 范围内，
        那么我们依然利用计数排序统计每一类数的数量，并使用双指针维护中位数。
        
        对于超出范围的数，我们可以单独进行处理，建立两个数组，
        分别记录小于 0 的部分的数的数量，和大于 100 的部分的数的数量即可。
        当小部分时间，中位数不落在区间 [0,100] 中时，我们在对应的数组中暴力检查即可。
"""
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())