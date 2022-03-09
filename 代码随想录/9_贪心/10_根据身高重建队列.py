"""
    题目描述:
        假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
        每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面正好有 ki 个身高大于或等于 hi 的人。

        请你重新构造并返回输入数组 people 所表示的队列。
        返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性
        （queue[0] 是排在队列前面的人）。

    链接: https://leetcode-cn.com/problems/queue-reconstruction-by-height
"""

from typing import List
from collections import deque

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先对 people 按照身高降序排列，身高相同按照次数升序排列
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)

        result = []

        for item1 in people:

            if len(result) == 0:
                result.append(item1)
                continue

            count, index = 0, 0
            for i, item2 in enumerate(result):
                if item2[0] >= item1[0]:
                    count += 1
                
                if count == item1[1]:
                    index = i+1
                    break
            
            result.insert(index, item1)

        return result
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先对 people 按照身高降序排列，身高相同按照次数升序排列
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)

        que = []

        # 根据每个元素的第二个维度k，贪心算法，进行插入
        # people已经排序过了：同一高度时k值小的排前面。
        for p in people:
            que.insert(p[1], p)
        return que
