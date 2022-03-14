"""
    题目描述:
        假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。
        由于道路的限制，车只能向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

        这儿有一份乘客行程计划表 trips[][]，
        其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：
            必须接送的乘客数量；
            乘客的上车地点；
            以及乘客的下车地点。
        
        这些给出的地点位置是从你的 初始 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

        请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所有乘客的任务
        （当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。

    链接: https://leetcode-cn.com/problems/car-pooling
"""

from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
            将道路上的节点视为一个数组；根据题意终点下标最大小于1000；因此数组上限为 1000；
            数组内元素为当前节点车上乘客数；
            上下客的过程可以转化为对数组的区间内元素增减操作；
            检查增减后数组内元素是否超过最大容量即可。

            可以应用差分数组的技巧。
        """
        # 构造差分数组，初始全为 0
        diff = [0] * 1001
        
        # 更新差分数组
        for trip in trips:
            diff[trip[1]] += trip[0]
            diff[trip[2]] -= trip[0]
        
        # 还原原始数组
        people = [diff[0]] * len(diff)

        for i in range(1, len(diff)):
            people[i] = people[i-1] + diff[i]

        if max(people) > capacity:
            return False
        
        return True

