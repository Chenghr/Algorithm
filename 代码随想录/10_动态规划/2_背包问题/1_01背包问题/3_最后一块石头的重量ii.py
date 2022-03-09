"""
    题目描述:
        有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

        每一回合，从中选出任意两块石头，然后将它们一起粉碎。
        假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下:
            如果 x == y，那么两块石头都会被完全粉碎；
            如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
            最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

    链接: https://leetcode-cn.com/problems/last-stone-weight-ii
"""

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
            分析:
                本质为将石头分成两堆，两堆石头之间总和差距尽可能小，返回差值。

            每块石头只能使用一次，01背包模型，目标是两堆石头大小相同；因此有:
                bagsize: sum/2;
                物品价值: 石头重量；物品重量: 石头重量；
            
            1. dp[j]: 背包容量为 j 的情况下，能获得的最大价值;
            2. dp[j] = max(dp[j], dp[j-stons[i]] + stones[i])
            3. stones 非负，均初始化为 0 即可；
            4. 遍历: 从后向前遍历背包容量；

            返回: sum - dp[-1]*2
        """
        bag_size = int(sum(stones) / 2)
        dp = [0] * (bag_size + 1)

        for i in range(len(stones)):
            for j in range(bag_size, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        
        return sum(stones) - dp[-1]*2