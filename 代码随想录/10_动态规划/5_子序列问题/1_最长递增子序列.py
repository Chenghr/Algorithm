"""
    题目描述:
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

        子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
    
    进阶: 你能将算法的时间复杂度降低到 O(n log(n)) 吗?

    链接: https://leetcode-cn.com/problems/longest-increasing-subsequence
"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            1. d[i]: 以第 i 个元素结尾的最长递增子序列长度；
            2. for j in range(0, i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j]+1)
            3. dp[i] = 1; # 每个元素最少可以包含自己，初始化为1
            4. 从前向后;

            复杂度: O(n^2), O(n)
        """
        dp = [ 1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            纸牌游戏方法；
                只能把点数小的牌压到点数比它大的牌上。
                如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去。
                如果当前牌有多个堆可供选择，则选择最左边的堆放置。

                牌的堆数就是我们想求的最长递增子序列的长度，证明略。

            链接: https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484498&idx=1&sn=df58ef249c457dd50ea632f7c2e6e761&source=41#wechat_redirect
        """
        # 模拟牌堆 
        top = [0] * len(nums)
        heapNum = 0

        for poker in nums:
            # 只能把点数小的牌放到比它大的牌上，如果有多个堆可以选择，则选择最左边的堆放置
            
            # 搜索左侧边界的二分查找
            # 这里用到的含义是: target 应该插⼊在 nums 中的索引位置
            left, right = 0, heapNum

            while left < right:
                mid = int((left + right) / 2)

                if top[mid] == poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                elif top[mid] > poker:
                    right = mid
            
            if left == heapNum:
                # 没找到合适的牌堆，新建一堆
                heapNum += 1

            # 把这张牌放到牌堆顶
            top[left] = poker

        # 牌堆数就是 LIS 长度
        return heapNum