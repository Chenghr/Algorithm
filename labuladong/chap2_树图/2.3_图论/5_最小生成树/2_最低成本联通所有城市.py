"""
    题目描述:
        想象⼀下你是个城市基建规划者，地图上有 N 座城市，它们按以 1 到 N 的次序编号。 
        给你⼀些可连接的选项 ，其中每个选项 conections[i] = [city1, city2, cost] 
        表示 将城市 city1 和城市city2 city2 conections 连接所要的成本为 cost
        （连接是双向的，也就是说城市 city1 和城市 city2 相连也同样意味着城市 和城市 city1 相连）。 
        
        计算使得每对城市都连通的最⼩成本。如果根据已知条件⽆法完成该项任务，则请你返回 -1。
    
    链接: https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost/
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

class Solution():
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
            最小生成树算法:
                贪心思想；
                将所有边按照权重从小到大排序，从权重最小的边开始遍历，
                如果这条边和mst中的其它边不会形成环，则这条边是最小生成树的一部分，将它加入mst集合；
                否则，这条边不是最小生成树的一部分，不要把它加入mst集合。

                最后mst集合中的边就形成了最小生成树
        """
        
        uf = UF(n)
        que = PriorityQueue()
        
        mst = 0
        for edge in connections:
            que.put((edge[-1], edge[0], edge[1]))
        
        while que.qsize() != 0:
            # 注意本题城市编号是 1-based
            weight, u, v = que.get()

            if uf.isConected(u-1, v-1):
                continue
                
            uf.union(u-1, v-1)
            mst += weight

        return mst if uf.count == 1 else -1

ans = Solution()
res = ans.minimumCost(3, [[1,2,5], [1,3,6], [2,3,1]])
print(res)
connections = [[1,2,5], [1,3,6], [2,3,1]]