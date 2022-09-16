"""
    题目描述:
        在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
        由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。

        一支弓箭可以沿着 x 轴从不同点完全垂直地射出。
        在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 
        且满足  xstart ≤ x ≤ xend，则该气球会被引爆。
        可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。
        我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

        给你一个数组 points ，其中 points [i] = [xstart,xend] ，
        返回引爆所有气球所必须射出的最小弓箭数。

    链接: https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
"""

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
            贪心:
                局部最优: 当气球出现重叠，一起射，所用弓箭最少。
                全局最优: 把所有气球射爆所用弓箭最少。
                
            为了让气球尽可能的重叠，需要对数组进行排序.
        """
        points.sort(key=lambda x: x[1])

        arrow, max_end = 1, points[0][1]  # 最后射出去一支箭
        for p in points:
            if p[0] <= max_end:
                # 当前点还在这一箭的范围内
                max_end = min(max_end, p[1])
            else:
                arrow += 1
                max_end = p[1]
        
        return arrow
        