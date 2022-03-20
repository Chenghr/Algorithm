"""
    题目描述:
        给定从 0 到 n-1 标号的 n 个结点，和⼀个⽆向边列表（每条边以结点对来表示），
        请编写⼀个函数⽤来判断 这些边是否能够形成⼀个合法有效的树结构。

    链接: https://leetcode-cn.com/problems/graph-valid-tree/
"""

from typing import List

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            思路: 
                构建 n 个节点的并查集，逐边联通节点，
                    如果两个节点在联通前已在同一个连通分量中，则有环，无法构成有效的树结构。

                最终并查集中只有一个联通分量，则构建树成功。
        """
        uf = UF(n)

        for edge in edges:
            if uf.isConected(edge[0], edge[1]):
                return False
            
            uf.union(edge[0], edge[1])
        
        return uf.count == 1