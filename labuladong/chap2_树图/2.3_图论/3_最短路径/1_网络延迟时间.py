"""
    题目描述:
        有 n 个网络节点，标记为 1 到 n。

        给你一个列表 times，表示信号经过 有向 边的传递时间。 
        times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

        现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？
        如果不能使所有节点收到信号，返回 -1 。

    链接: https://leetcode-cn.com/problems/network-delay-time
"""

from typing import List
from queue import PriorityQueue

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            求解最短路径: Dijkstra 算法（BFS思想）

            算法思想:
                a. 初始时，S只包含源点，即S = {v}，v的距离为0;
                   U包含除v外的其他顶点，即:U={其余顶点};
                   若v与U中顶点u有边，则<u,v>正常有权值，若u不是v的出边邻接点，则<u,v>权值为∞。

                b. 从U中选取一个距离v最小的顶点k，把k，加入S中（该选定的距离就是v到k的最短路径长度）。

                c. 以k为新考虑的中间点，修改U中各顶点的距离；若从源点v到顶点u的距离（经过顶点k）比原来距离（不经过顶点k）短，则修改顶点u的距离值，修改后的距离值的顶点k的距离加上边上的权。

                d. 重复步骤b和c直到所有顶点都包含在S中。
        """
        graph = [[float('inf')] * n for _ in range(n)]

        # 注意 info 中节点下标是 1-based
        for info in times:
            graph[info[0]-1][info[1]-1] = info[2]
        
        dist = [float('inf')] * n
        dist[k-1] = 0  # 起点距离置为 0
        used = [False] * n

        for _ in range(n):
            # 逐个加入节点到已访问节点中

            u = -1
            for v, tag in enumerate(used):
                # 确定起始节点，优先选择距离最短的节点
                if not tag and (u == -1 or dist[v] < dist[u]):
                    u = v
            
            used[u] = True
            
            # 更新选中节点的相邻接点距离
            for v, time in enumerate(graph[u]):
                dist[v] = min(dist[v], dist[u]+time)
        
        ans = max(dist)

        return ans if ans < float('inf') else -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            优化:
                在寻找与起点节点距离最近的点时可以用小根堆（优先队列）来优化。
        """
        graph = [[] for _ in range(n)]

        for edge_from, edge_to, time in times:
            # 只需保留含边节点
            graph[edge_from-1].append((edge_to-1, time))
        
        dist = [float('inf')] * n
        dist[k-1] = 0

        que = PriorityQueue()
        que.put((0, k-1))

        while que.qsize() != 0:
            time, u = que.get()
            if dist[u] < time:
                # time 是入队时源点到node的时间开销，dist[node]是当前的时间开销
                # 说明已出现了更短路径将其替换了
                continue
                
            for v, time1 in graph[u]:
                if dist[u] + time1 < dist[v]:
                    # 更新路径后入栈
                    dist[v] = dist[u] + time1
                    que.put((dist[v], v))
        
        ans = max(dist)
        return ans if ans < float('inf') else -1

a = Solution()
result = a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
print(result)