"""
    题目描述:
        你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

        在选修某些课程之前需要一些先修课程。 
        先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
        表示如果要学习课程 ai 则 必须 先学习课程  bi 。

        例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。

        请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

    链接: https://leetcode-cn.com/problems/course-schedule
"""

from typing import List
import collections
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            将课程关系抽象成一个有向图，然后即为判断有向图中是否有环的问题。

            采用 DFS 遍历求解，辅助 path 数组，判断 path 数组中是否有重复元素即可。

            对于图中的任意一个节点，它在搜索的过程中有三种状态，即：
                「未搜索」：我们还没有搜索到这个节点；
                「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成；
                「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求。

            使用 DFS 得到拓扑排序的算法流程:
                在每一轮的搜索搜索开始时，我们任取一个「未搜索」的节点开始进行深度优先搜索。

                我们将当前搜索的节点 u 标记为「搜索中」，遍历该节点的每一个相邻节点 v:
                    - 如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；
                    - 如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
                    - 如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，
                        因此 u 无论何时入栈都不会影响到 (u, v) 之前的拓扑关系，以及不用进行任何操作。

                当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。

                在整个深度优先搜索的过程结束后，如果我们没有找到图中的环，
                那么栈中存储这所有的 n 个节点，从栈顶到栈底的顺序即为一种拓扑排序。
            
            优化:
                由于我们只需要判断是否存在一种拓扑排序，而栈的作用仅仅是存放最终的拓扑排序结果，
                因此我们可以只记录每个节点的状态，而省去对应的栈。
        """
        graph = [[] for _ in range(numCourses)]

        # 构建有向图，edge 是 0-based
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        visit = [False] * numCourses  # 标记是否访问过
        onPath = [False] * numCourses  # 标记在路径中是否出现过
        hasCycle = False  # 默认无环

        def dfs(node: int):
            nonlocal graph, visit, onPath, hasCycle

            if onPath[node]:
                hasCycle = True

            if visit[node] or hasCycle:
                # 访问过或者已经有环，则不必继续
                return

            # 当前节点处理
            visit[node] = True
            onPath[node] = True

            for neighbor in graph[node]:
                dfs(neighbor)
            
            # 回溯
            onPath[node] = False
        
        for node in range(numCourses):
            if not visit[node]:
                dfs(node)
        
        return not hasCycle
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """题解写法；优化存储空间结构，将 onPath 数组叠放在 visited 上，值得学习
        """
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid

            visited[u] = 1

            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)

                    if not valid:
                        return

                elif visited[v] == 1:
                    valid = False
                    return
                    
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            基于 BFS 实现。

            注意图的初始化，有向图表示依赖关系是 b -> a.

            借助 indegree 数组记录每个节点的入度。

            思路:
                1. 对 BFS 队列进行初始化，将入度为 0 的节点首先装入队列。
                2. 开始执行 BFS 循环，不断弹出队列中的节点，减少相邻节点的入度，并将入度变为 0 的节点加入队列。
                3. 如果最终所有节点都被遍历过（count 等于节点数），则说明不存在环，反之则说明存在环。
        """
        graph = [[] for _ in range(numCourses)]
        inDegrees = [0] * numCourses  # 记录每个节点的入度

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])  # 初始化图的依赖顺序
            inDegrees[edge[0]] += 1
        
        que = deque([u for u in range(numCourses) if inDegrees[u] == 0])
        
        nodeCount = 0
        while que:
            node = que.popleft()
            nodeCount += 1

            for neighbor in graph[node]:
                inDegrees[neighbor] -= 1

                if inDegrees[neighbor] == 0:
                    que.append(neighbor)
        
        return nodeCount == numCourses



