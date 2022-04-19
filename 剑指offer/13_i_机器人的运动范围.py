from queue import Queue

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
            1. 
            行坐标和列坐标数位之和大于 k 的格子看作障碍物，那么这道题就是一道很传统的搜索题目，
            我们可以使用广度优先搜索或者深度优先搜索来解决它，本文选择使用广度优先搜索的方法来讲解。
            注意本题障碍物的出现只会在当前可达节点的右下方，因为位数和是递增的。
            2. 
            由于只用向右向下查找，可以考虑使用dp，dp[i][j]表示是否可达
            if calBitNum(i) + calBitNum(j) <= k:
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            注意边界处理。
        """
        def calBitNum(n: int):
            ans = 0

            while n > 0:
                ans += n % 10
                n = n // 10

            return ans

        visited = set()

        que = Queue()
        que.put((0, 0))
        
        while not que.empty():
            x, y = que.get()

            if (x, y) not in visited and 0 <= x < m and 0 <= y < n and calBitNum(x) + calBitNum(y) <= k:
                # 访问条件 / 剪枝条件
                # 这里如果写在下面会死循环
                visited.add((x, y))

                for nx, ny in [(x+1, y), (x, y+1)]:
                    # 只用向下向右查找，因为位数和是递增的
                    que.put((nx, ny))
        
        return len(visited)

a = Solution()
ans = a.movingCount(36,11,15)
print(ans)