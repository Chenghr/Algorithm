"""
    题目描述:
        给你⼀个 points 数组，表示 2D 平⾯上的⼀些点，其中 points[i] = [xi, yi] 。
        连接点 [xi, yi] 和点 [xj, yj] 的费⽤为它们之间的曼哈顿距离： |xi - xj| + |yi - yj| ，
        其中 |val| 表示 val 的绝对值。 
        
        请你返回将所有点连接的最⼩总费⽤。
        只有任意两点之间有且仅有⼀条简单路径时，才认为所有点都已连接。
    
    链接: https://leetcode-cn.com/problems/min-cost-to-connect-all-points/
"""

from typing import List
from queue import PriorityQueue

class UF:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.count = n  # 记录联通分量个数

    def find(self, x: int) -> int:
        """查找根节点，同时做路径压缩"""
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        
        return x
    
    def union(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return 

        if self.sizes[rootP] < self.sizes[rootQ]:
            self.parents[rootP] = rootQ
            self.sizes[rootQ] += self.sizes[rootP]
        else:
            self.parents[rootQ] = rootP
            self.sizes[rootP] += self.sizes[rootQ]
        
        self.count -= 1
    
    def isConected(self, p: int, q: int) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)

        return rootP == rootQ


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
            最小生成树算法的应用。
            小技巧: 这里使用每个点在 points 数组中的下标作为标记。
        """
        uf = UF(len(points))

        que = PriorityQueue()

        for i in range(0, len(points)):
            for j in range(i, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                que.put((dist, i , j))
        
        mst = 0
        while que.qsize() != 0:
            weight, u, v = que.get()
            
            if uf.isConected(u, v):
                continue

            uf.union(u, v)
            mst += weight
        
        return int(mst)

