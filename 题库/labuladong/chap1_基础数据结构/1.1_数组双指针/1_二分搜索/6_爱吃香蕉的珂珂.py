"""
    题目描述:
        珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。
        警卫已经离开了，将在 H 小时后回来。

        珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。
        每个小时，她将会选择一堆香蕉，从中吃掉 K 根。
        如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

        珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

        返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。
    
    提示:
        1 <= piles.length <= 10^4
        piles.length <= H <= 10^9
        1 <= piles[i] <= 10^9

    链接: https://leetcode-cn.com/problems/koko-eating-bananas
"""

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            由题意分析得: 
                吃完所有香蕉用时: sum(piles[i] // k + 1) for i in N

            根据二分搜索的泛化：
                x: 吃香蕉的速度；f(x): 吃香蕉总用时；H: target.
                f(x) 单调递减
            
            题目要求最小速度 k，即求左边界。
        """
        def costTime(x: int) -> int:
            nonlocal piles
            sumTime = 0

            for pile in piles:
                # sumTime += math.ceil(pile / x)
                sumTime += (pile-1) // x + 1  # 等价写法
            
            return sumTime
        
        # 根据题目限制给出上下界
        left, right = 1, 10**9+1

        while left < right:
            mid = (left + right) // 2

            sumTime = costTime(mid)

            if sumTime == h:
                right = mid
            elif sumTime < h:
                # 注意 costTime 是单调递减函数
                right = mid
            elif sumTime > h:
                left = mid + 1
        
        # 本题一定有解
        return left

solution = Solution()
result = solution.minEatingSpeed([312884470], 968709470)
print(result)