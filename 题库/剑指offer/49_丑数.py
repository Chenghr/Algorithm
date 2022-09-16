from queue import PriorityQueue

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
            使用最小堆，会预先存储较多的丑数，导致空间复杂度较高，维护最小堆的过程也导致时间复杂度较高。
            可以使用动态规划（多指针）的方法进行优化。

            丑数只会由丑数生成，每个丑数生成下一个丑数的方式有三种方式（2 3 5），
            因此可以用三个指针分别记录 *2 *3 *5 指针对应丑数的位置，每次生成新的丑数就选择其中最小的一个；
            这样可以保证丑数的顺序生成；
            另外去重问题，可能有多个路径同时生成最小的丑数，此时我们可以将满足的指针均向后移动一位即可。
        """
        dp = [1] * n
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            num2, num3, num5 = dp[p2]*2, dp[p3]*3, dp[p5]*5

            dp[i] = min(num2, num3, num5)  # 三个候选值中选择最小值
            
            # 更新指针 + 去重
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[-1]

    def nthUglyNumber(self, n: int) -> int:
        """
            一个丑数必然由之前的丑数推出；但是可能会有多个来源，因此需要判断是否出现过；-> 哈希
            要求第 n 个丑数，因此需要排序；-> 优先队列（堆）
        """
        ugly_nums = []
        que = PriorityQueue()
        que.put(1)

        while len(ugly_nums) != n:
            num = que.get()

            if num not in ugly_nums:
                ugly_nums.append(num)
            
                que.put(num*2)
                que.put(num*3)
                que.put(num*5)
        
        return ugly_nums[-1] 
    
