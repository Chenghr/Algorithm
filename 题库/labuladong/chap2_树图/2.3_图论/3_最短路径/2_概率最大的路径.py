"""
    题目描述:
        给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，
        该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，
        且该边遍历成功的概率为 succProb[i] 。

        指定两个节点分别作为起点 start 和终点 end ，
        请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

        如果不存在从 start 到 end 的路径，请 返回 0 。
        只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

    链接: https://leetcode-cn.com/problems/path-with-maximum-probability

"""

from typing import List
from queue import PriorityQueue

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
            图中指定两点的最长路径
            Dijstra 算法改一下即可。
            
            每次选择「未确定节点」时，起点到它的最短路径的长度可以被确定。

            可以这样理解，因为我们已经用了每一个「已确定节点」更新过了当前节点，
            无需再次更新（因为一个点不能多次到达）。而当前节点已经是所有「未确定节点」中与起点距离最短的点，
            不可能被其它「未确定节点」更新。所以当前节点可以被归类为「已确定节点」。
            给定的图必须是正边权图，否则「未确定节点」有可能更新当前节点，这也是 Dijkstra 不能处理负权图的原因。

            为什么当前图能使用 Dijkstra 算法呢？因为该图的边权都是位于区间 [0,1] 的小数（概率），
            即沿着一条边移动无法让边权积增大，只会减小或不变。而我们要求的是最大边权积，
            这符合了 Dijkstra 算法的思想和要求
        """
        graph = [[] for _ in range(n)]

        # 本题中下标为 0-based，无需变动
        for i, (x, y) in enumerate(edges):
            graph[x].append((y, succProb[i]))
            graph[y].append((x, succProb[i]))
        
        probs = [0.0] * n
        probs[start] = 1.0

        # 这里要分开写，不能初始化同时写入元素
        que = PriorityQueue()
        que.put((-1.0, start))

        while que.qsize() != 0:
            item = que.get()
            prob, node = -item[0], item[1]

            if prob < probs[node]:
                continue
                
            for nodeNext, probNext in graph[node]:
                if probs[node] * probNext > probs[nodeNext]:
                    probs[nodeNext] = probs[node] * probNext 
                    que.put((-probs[nodeNext], nodeNext))
        
        return probs[end]