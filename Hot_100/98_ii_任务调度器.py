"""
    题目描述:
        给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。
        其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
        在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

        然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，
        因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

        你需要计算完成所有任务所需要的 最短时间 。

    链接: https://leetcode-cn.com/problems/task-scheduler
"""

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
            贪心思想考虑；
            影响最短时间的是数量最多的任务；
            整体的解题步骤如下：

            计算每个任务出现的次数
            找出出现次数最多的任务，假设出现次数为 x
            计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
            计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count

            存在特殊情况，当冷却时间短，任务种类很多时，执行任务所需的时间，就是任务的数量。
        """
        dic = [0] * 26
        for ch in tasks:
            dic[ord(ch) - ord('A')] += 1
        
        maxNum = max(dic)
        maxCount = dic.count(maxNum)

        minTime = (maxNum-1)*(n+1) + maxCount
        return max(minTime, len(tasks))