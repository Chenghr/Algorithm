"""
    除法求值
    httxs://leetcode-cn.com/xroblems/evaluate-division/
"""

from typing import List
from collections import defaultdict, deque

class UF:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.weight = [1] * n  # 当前节点指向父节点的权重
    
    def union(self, x, y, value):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return
        
        self.father[rootX] = rootY
        # 平行四边形法则
        self.weight[rootX] = value * self.weight[y] / self.weight[x] 
    
    def find(self, x):
        if x != self.father[x]:
            origin = self.father[x]  # 保留原来的父节点
            self.father[x] = self.find(self.father[x])  # 递归的路劲压缩，更新权重
            self.weight[x] = self.weight[x] * self.weight[origin]  # 更新当前节点权重
        
        return self.father[x]

    def isConnected(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            return -1.0
        else:
            return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
            并查集实现；
            在一个联通分量的变量可以计算出比值，不在的则不能；
            在传统联通分量的基础上，增加记录每个节点到根节点的权重
        """
        dic = defaultdict(int)

        for x, y in equations:
            if x not in dic:
                dic[x] = len(dic)
            
            if y not in dic:
                dic[y] = len(dic)
        
        uf = UF(len(dic))
        for (x, y), val in zip(equations, values):
            uf.union(dic[x], dic[y], val)
        
        ans = []
        for x, y in queries:
            if x not in dic or y not in dic:
                ans.append(-1.0)
            else:
                ans.append(uf.isConnected(dic[x], dic[y]))
        
        return ans





class Solution1:
    """dfs实现"""
    def genneateGraphDict(self, equations: List[List[str]], values: List[float]):
        """使用字典构造图，便于查找节点
        """
        graph = {}

        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            
            if y in graph:
                graph[y][x] = 1.0 / v
            else:
                graph[y] = {x: 1/v}
        
        return graph


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """bfs 实现"""
        # 处理图节点
        graph = self.genneateGraphDict(equations, values)

        def dfs(start, end):
            nonlocal graph, visited

            if start == end:
                return 1
            
            for node in graph[start].keys():
                if node == end:
                    return graph[start][node]

                elif node not in visited:
                    visited.append(node)
                    w1 = dfs(node, end)

                    if w1 != -1:
                        return graph[start][node] * w1
            
            return -1
                        
        ans = []
        for (x, y) in queries:
            if x not in graph or y not in graph:
                ans.append(-1.0)
            else:
                visited = []
                ans.append(dfs(x, y))

        return ans


class Solution2:
    def genneateGraphMartix(self, equations: List[List[str]], values: List[float]):
        """邻接矩阵构建图
        """
        dic_node = defaultdict(int)

        for _, e in enumerate(equations):
            # 统计节点数目，编号
            if e[0] not in dic_node:
                dic_node[e[0]] = len(dic_node)
            
            if e[1] not in dic_node:
                dic_node[e[1]] = len(dic_node)

        # 生成图
        graph = [[0] * len(dic_node) for _ in range(dic_node)]

        for i, val in enumerate(values):
            node1, node2 = dic_node[equations[i][0]], dic_node[equations[i][1]]

            graph[node1][node2] = val
            graph[node2][node1] = 1.0 / val
        
        return dic_node, graph

    def bfs(self, graph, start, end):
        """bfs 搜索从 start 到 end 的路径长度"""
        que = deque()
        visited = []

        for to, weight in graph[start]:
            if to == end:
                return weight

            que.append((to, weight))
        
        while len(que) != 0:
            node, w0= que.popleft()
            
            if node == end:
                graph[start].append((end, w0))
                return w0

            visited.append(node)

            for to, w1 in graph[node]:
                if to not in visited:
                    que.append((to, w0 * w1))
        
        return -1.0
    
    def floyd(self, graph):
        """计算出图中任意两点间距离"""

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 处理图节点
        dic_node = defaultdict(int)
        graph = []

        for i, e in enumerate(equations):
            if e[0] not in dic_node:
                dic_node[e[0]] = len(graph)
                graph.append([])
            
            if e[1] not in dic_node:
                dic_node[e[1]] = len(graph)
                graph.append([])
            
            node1, node2 = dic_node[e[0]], dic_node[e[1]]
            graph[node1].append((node2, values[i]))
            graph[node2].append((node1, 1.0 / values[i]))

        ans = []
        for q in queries:
            if q[0] not in dic_node or q[1] not in dic_node:
                ans.append(-1.0)
            else:
                ans.append(self.bfs(graph, dic_node[q[0]], dic_node[q[1]]))

        return ans

a = Solution()
ans = a.calcEquation(equations=[["a","b"],["b","c"]], values=[2.0,3.0], queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print(ans)