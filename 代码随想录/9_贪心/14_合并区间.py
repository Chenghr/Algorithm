"""
    题目描述:
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]。
        请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

    链接: https://leetcode-cn.com/problems/merge-intervals
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 按照开始下标，升序排列
        intervals.sort()

        result, start, end = [], intervals[0][0], intervals[0][1]

        for point in intervals:
            if point[0] <= end:
                end = max(end, point[1])
            else:
                result.append([start, end])
                start = point[0]
                end = point[1]

        result.append([start, end])

        return result