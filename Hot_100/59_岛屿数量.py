"""
    题目描述:
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

        此外，你可以假设该网格的四条边均被水包围。

    链接: https://leetcode-cn.com/problems/number-of-islands
"""

from typing import List
from collections import deque

class UF:
    def __init__(self, num):
        self.parents = [i for i in range(num)]
        self.size = [1] * (num)
        self.count = num  # 联通分量个数
    
    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        
        return x
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return
        
        if self.size[rootP] < self.size[rootQ]:
            self.parents[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parents[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]

        self.count -= 1

    def isConected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        return rootP == rootQ

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            采用并查集来做；
            将所有的 0 联通到一个虚拟节点上；将 1 与周围的联通分量相联通；
            最终所有的联通分量个数 - 1即为岛屿数量。
        """
        m, n = len(grid), len(grid[0])
        uf = UF(m*n + 1)  # 所有的 0 联通到最后一个节点上

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '0':
                    uf.union(x*n+y, m*n)
                else:
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                            uf.union(x*n+y, nx*n+ny)
        
        return uf.count - 1
                        
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            深搜；
            如果一个位置为 1，则以其为起始节点开始进行深度优先搜索。
            在深度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。

            最终岛屿的数量就是我们进行深度优先搜索的次数。
        """
        def dfs(grid, x, y):
            grid[x][y] = '0'

            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                    dfs(grid, nx, ny)
                
        count = 0
        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(grid, x, y)
                    count += 1
        
        return count
    
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            广搜；
            思想同上，搜索策略上采用广搜。
        """
        def bfs(grid, x, y):

            grid[x][y] = '0'

            que = deque([(x, y)])
        
            while len(que) != 0:
                x, y = que.popleft()

                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                        que.append((nx, ny))
                        grid[nx][ny] = '0'  # 在这里处理，否则可能出现死循环。
                
        count = 0
        m, n = len(grid), len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    bfs(grid, x, y)
                    count += 1
        
        return count