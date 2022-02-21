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
            本题要使用贪心 + 二分查找的方式可以给出 O(nlogn) 的解法；
            具体待研究。
        """