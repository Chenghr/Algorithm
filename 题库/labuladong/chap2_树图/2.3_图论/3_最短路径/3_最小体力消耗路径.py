"""
    题目描述:
        你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，
        其中 heights[row][col] 表示格子 (row, col) 的高度。
        一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。
        你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

        一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。
        请你返回从左上角走到右下角的最小 体力消耗值 。

    链接: https://leetcode-cn.com/problems/path-with-minimum-effort

    提醒: 本题有三个思路可以解决: 二分查找，并查集，最短路径
"""

from typing import List
from queue import PriorityQueue

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
            将地图中的每个格子转化成图中节点，边为相邻格子的高度差绝对值
            路径长度: 经过所有边权的最大值。
        """
        m, n = len(heights), len(heights[0])
        dists = [float('inf')] * (m*n)
        dists[0] = 0

        que = PriorityQueue()
        que.put((0, 0, 0))

        seenNode = set()

        while que.qsize() != 0:
            dist, x, y = que.get()

            node = x*n + y
            if node in seenNode:
                continue
            if (x, y) == (m-1, n-1):
                break
                
            seenNode.add(node)

            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    if max(dist, abs(heights[x][y] - heights[nx][ny])) <= dist[nx * n + ny]:
                        # 更新最短路径
                        dist[nx*n + ny] = max(dist, abs(heights[x][y] - heights[nx][ny]))
                        que.get((dist[nx*n + ny], nx, ny))
            
        return dist[m*n - 1]
