"""
    题目描述:
        给定一个由表示变量之间关系的字符串方程组成的数组，
        每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一:
            "a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

        只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

    链接: https://leetcode-cn.com/problems/satisfiability-of-equality-equations
"""

from typing import List

class UF:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int):
        while self.parents[x] != x:
            # 查找父节点的同时进行路径压缩
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        
        return x
    
    def union(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return
        
        if self.size[rootP] < self.size[rootQ]:
            self.parents[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        else:
            self.parents[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
    
    def isConect(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ
 
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
            一共只有 26 个小写字母，因此我们可以构建一个26个节点的并查集；
            然后先处理等号的，将相等的两个节点联通；
            再处理不相等的，如果两个节点在一个子树上，则返回 false，否则返回 True
        """

        uf = UF(26)

        for equation in equations:
            if equation[1] == '=':
                uf.union(ord(equation[0])-ord('a'), ord(equation[3])-ord('a'))
        
        for equation in equations:
            if equation[1] == '!':
                if uf.isConect(ord(equation[0])-ord('a'), ord(equation[3])-ord('a')):
                    return False
        
        return True