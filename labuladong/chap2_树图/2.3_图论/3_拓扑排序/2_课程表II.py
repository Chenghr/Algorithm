"""
    题目描述:
        现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
        给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，
        表示在选修课程 ai 前 必须 先选修 bi 。

        例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
        
        返回你为了学完所有课程所安排的学习顺序。
        可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

    链接: https://leetcode-cn.com/problems/course-schedule-ii
"""

from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            如果把课程抽象成节点，课程之间的依赖关系抽象成有向边，那么这幅图的拓扑排序结果就是上课顺序。

            基于 DFS 实现。
                成环的图无法进行拓扑排序，后序遍历逆序的结果，即为拓扑排序的结果；
                类比二叉树的后序遍历: 左右节点遍历完才会遍历根节点；
                拓扑排序中一个任务必须等到它依赖的所有任务都完成之后才能开始开始执行，类似于后序遍历的性质。
        """
        graph = [[] for _ in range(numCourses)]

        # 构建有向图，edge 是 0-based
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        visit = [False] * numCourses
        onPath = [False] * numCourses
        hasCycle = False
        postPath = []

        def dfs(node: int):
            nonlocal graph, visit, onPath, hasCycle, postPath

            if onPath[node]:
                hasCycle = True
            
            if visit[node] or hasCycle:
                return
            
            # 处理当前节点
            visit[node] = True
            onPath[node] = True

            for neighbor in graph[node]:
                dfs(neighbor)
            
            # 后序遍历，记录节点
            postPath.append(node)

            onPath[node] = False  # 回溯
        
        for node in range(numCourses):
            if not visit[node]:
                dfs(node)
        
        if hasCycle:
            return []
        else:
            postPath = postPath.reverse()
            return postPath

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            对图进行一遍深度优先搜索。
            当每个节点进行回溯的时候，我们把该节点放入栈中。
            最终从栈顶到栈底的序列就是一种拓扑排序
        """
        graph = [[] for _ in range(numCourses)]
        
        for info in prerequisites:
            graph[info[1]].append(info[0])
        
        # 标记节点状态，0为未搜索，1为搜索中，2为已搜索
        visited = [0] * len(numCourses)
        result= []
        valid = True  # 默认无环

        def dfs(node: int):
            nonlocal valid

            visited[node] = 1  # 开始搜索，等于是添加到路径中

            for next in graph[node]:
                if visited[next] == 0:
                    # 遇到一个未搜索过的邻接点，继续深搜
                    dfs(next)

                    if not valid:
                        return
                
                elif visited[next] == 1:
                    # 找到环
                    valid = False
                    return
            
            visited[node] = 2  # 节点搜索完成
            result.append(node)

        for node in range(numCourses):
            if valid and not visited[node]:
                dfs(node)
        
        if not valid:
            return []
        
        return result[:: -1]  # 逆序输出



    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
            基于 BFS 实现。
            
            思路:
                1. 对 BFS 队列进行初始化，将入度为 0 的节点首先装入队列。
                2. 开始执行 BFS 循环，不断弹出队列中的节点，减少相邻节点的入度，并将入度变为 0 的节点加入队列。
                3. 如果最终所有节点都被遍历过（count 等于节点数），则说明不存在环，反之则说明存在环。
            
            弹出节点的顺序即为拓扑排序的结果
        """
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        # 将所有入度为 0 的节点放入队列中
        que = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while que:
            # 从队首取出一个节点
            u = que.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    que.append(v)

        if len(result) != numCourses:
            result = list()

        return result