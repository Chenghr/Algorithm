"""
    题目描述:
        存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。
        给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。
        形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。
        该无向图同时具有以下属性：
            不存在自环（graph[u] 不包含 u）。
            不存在平行边（graph[u] 不包含重复值）。
            如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
            这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。

        二分图 定义：
            如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，
            并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。

        如果图是二分图，返回 true ；否则，返回 false 。

    链接: https://leetcode-cn.com/problems/is-graph-bipartite
"""

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
            进行 dfs 搜索是遇到没标记过的顶点，就按照二分图定义标记；
            遇到已经标记过的顶点，就检查相邻顶点是否不同色；
        """
        visit = [False] * len(graph)  # 标记是否访问过节点
        color = [0] * len(graph)  # 着色，false 和 true 表示不同颜色
        isTag = True  # 标记能否二分图

        def dfs(node: int):
            nonlocal graph, visit, isTag

            if not isTag:
                # 出现不满足的边
                return

            visit[node] = True

            for neighbor in graph[node]:
                if visit[neighbor] == False:
                    # 邻居节点没有被访问过
                    color[neighbor] = 1 - color[node]
                    dfs(neighbor)  # 递归遍历
                else:
                    # 邻居节点已经判断过
                    if color[neighbor] == color[node]:
                        isTag = False
        
        for node in range(len(graph)):
            if not visit[node]:
                dfs(node)
        
        return isTag

example = Solution()
result = example.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
print(result)