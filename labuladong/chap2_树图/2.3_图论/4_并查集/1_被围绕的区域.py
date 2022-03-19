"""
    题目描述:
        给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，
        找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

    链接: https://leetcode-cn.com/problems/surrounded-regions/
"""

from typing import List

class UF:
    """
        算法的关键点有 3 个：
        1. 用parent数组记录每个节点的父节点，相当于指向父节点的指针，
           所以parent数组内实际存储着一个森林（若干棵多叉树）。

        2. 用size数组记录着每棵树的重量，
           目的是让union后树依然拥有平衡性，而不会退化成链表，影响操作效率。

        3. 在find函数中进行路径压缩，保证任意树的高度保持在常数，
           使得 union 和 connected API 时间复杂度为 O(1)
    """
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]  # 初始化 n 棵树
        self.size = [1] * n  # 每棵树拥有的节点个数
        self.count = n  # 联通分量个数
    
    def find(self, x: int):
        """查找 x 的父亲节点"""
        while self.parent[x] != x:
            # 查找父节点的同时进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def union(self, p: int, q: int):
        """连通 p, q"""
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            # 已经是同一棵树
            return 
        
        # 将较小的树接到较大的树下，保持相对平衡
        if self.size[rootP] < self.size[rootQ]:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
    
    def isConnect(self, p: int, q: int) -> bool:
        """判断 p, q 是否联通"""
        rootP = self.find(p)
        rootQ = self.find(q)

        return rootP == rootQ
    

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead.

            DFS 解决思路:
                for 循环遍历棋盘四边，用 DFS 算法将与边界相连的 O 换位 #
                遍历整个棋盘，将 O 换成 X；将 # 换成 O，即可。
        """
        def dfs(x: int, y: int):
            nonlocal board

            if board[x][y] == 'X' or board[x][y] == '#':
                return
            
            # board[x][y] == 'O'
            board[x][y] = '#'

            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    dfs(nx, ny)
        
        for x in [0, len(board)-1]:
            for y in range(len(board[0])):
                dfs(x, y)
        
        for y in [0, len(board[0])-1]:
            for x in range(len(board)):
                dfs(x, y)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == '#':
                    board[x][y] = 'O'    
        
        return

    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead.

            并查集 解决思路:
                将不需要被替换的 O 连接上一个共同的父节点，这个父节点不被替换。
        """
        if len(board) == 0:
            return
        
        m, n = len(board), len(board[0])

        uf = UF(m * n + 1)  # dummy 节点占据一个位置
        dummy = m * n

        # 将棋盘四边的 'O' 连接上 dummy 节点
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i*n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i*n + n-1, dummy)

        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m-1][j] == 'O':
                uf.union((m-1)*n + j, dummy)
        
        # 搜索内部数组
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    # 将此 'O' 和上下左右的 'O' 联通
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if board[x][y] == 'O':
                            uf.union(x*n + y, i*n + j)
        
        # 所有不和 dummy 联通的 'O' 都要被替换
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not uf.isConnect(dummy, i*n + j):
                    board[i][j] = 'X'

        return 
