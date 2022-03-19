"""
    题目描述:
        给你一个有 n 个节点的 有向无环图（DAG），
        请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

        graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

    链接: https://leetcode-cn.com/problems/all-paths-from-source-to-target
"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
            基于深度优先搜索实现；

            具体地，我们从 0 号点出发，使用栈记录路径上的点。
            每次我们遍历到点 n-1，就将栈中记录的路径加入到答案中。
        """
        ans, stack = [], []

        def dfs(node: int):
            if node == len(graph) - 1:
                # 遍历到第 n-1 个节点
                ans.append(stack[:])
                return 
            
            for neighbor in graph[node]:
                
                stack.append(neighbor)  # 深搜，找到一个邻居节点就一直搜索下去

                dfs(neighbor)

                stack.pop()  # 回溯
        
        stack.append(0)
        dfs(0)

        return ans
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
            基于广度优先搜索实现；

            具体地，我们从 0 号点出发，使用栈记录路径上的点。
            每次我们遍历到点 n-1，就将栈中记录的路径加入到答案中。
        """
