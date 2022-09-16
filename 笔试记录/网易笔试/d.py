import sys

class UF:
    def __init__(self, n):
        self.father = [i for i in range(n)]  
        self.father.append(-1)# 红色的为-1

        self.size = [1] * (n+1)
        self.count = n+1
    
    def find(self, x):
        while self.father[x] != x:
            self.father[x] = self.father[self.father[x]]
            x = self.father[x]
        
        return x
    
    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if pRoot == qRoot:
            return 
        
        if self.size[pRoot] < self.size[qRoot]:
            self.father[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            self.father[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
    
    def isConnected(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        return pRoot == qRoot

def dfs(matrix, uf):
    # 深搜图，将
    
if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    n, m = map(int, line.split())
    
    uf = UF(n*m)  # 构建连通图

    matrix = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        matrix.append(list(map(int, line.split())))

    q = int(sys.stdin.readline())

    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    
