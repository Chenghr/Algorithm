"""
    链接https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484751&idx=1&sn=a873c1f51d601bac17f5078c408cc3f6&chksm=9bd7fb47aca07251dd9146e745b4cc5cfdbc527abe93767691732dfba166dfc02fbb7237ddbf&cur_album_id=1318892385270808576&scene=189#wechat_redirect
"""
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
    