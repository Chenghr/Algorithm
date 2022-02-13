"""
    题目描述:
        给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。
        返回 需要移除区间的最小数量，使剩余区间互不重叠 。

    链接: https://leetcode-cn.com/problems/non-overlapping-intervals
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            按终点排序，遇到重复的区间则删除
        """
        intervals.sort(key=lambda x: x[1])

        min_begin, count = intervals[0][1], 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < min_begin:
                # 需要移除
                count += 1
            else:
                min_begin = intervals[i][1]
        
        return count

        """
        题解思路:
            按照右边界排序，从左向右记录非交叉区间的个数。
            最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了。
            问题就是要求非交叉区间的最大个数。

            局部最优: 优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉。
            全局最优: 选取最多的非交叉区间。

            每次取非交叉区间的时候，都是可右边界最小的来做分割点（这样留给下一个区间的空间就越大）
        """