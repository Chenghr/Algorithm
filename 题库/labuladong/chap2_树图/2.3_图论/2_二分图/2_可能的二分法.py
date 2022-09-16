"""
    题目描述:
        给定一组 n 人（编号为 1, 2, ..., n）， 
        我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

        给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，
        表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；
        否则返回 false。

    链接: https://leetcode-cn.com/problems/possible-bipartition
"""

from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
            n 个人视为 n 个节点，dislike 视为边；
            看看能否构成一个二分图。
        """
        graph = [[] for _ in range(n)]

        # 构建邻接表，注意dislikes 中下标是 1-based
        for edge in dislikes:
            graph[edge[0]-1].append(edge[1]-1)
            graph[edge[1]-1].append(edge[0]-1)

        visit = [False] * n
        color = [0] * n
        isTag = True

        def dfs(node: int):
            nonlocal graph, visit, color, isTag

            if not isTag:
                return
            
            visit[node] = True

            for neighbor in graph[node]:
                if not visit[neighbor]:
                    color[neighbor] = 1 - color[node]
                    dfs(neighbor)
                else:
                    if color[neighbor] == color[node]:
                        isTag = False
        
        for node in range(n):
            if not visit[node]:
                dfs(node)
        
        return isTag
