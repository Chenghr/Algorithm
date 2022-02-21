"""
    题目描述:
        给定一个未经排序的整数数组，找到最长且 连续递增的子序列，
        并返回该序列的长度。

        连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，
        如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
        那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。

    链接: https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
"""

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
            1. dp[i]: 以 i 结尾的最长连续递增子序列
            2. if nums[i] > nums[i-1]:
                    dp[i] = max(dp[i], dp[i-1]+1)
            3. dp[i] = 1
            4. 从前到后

            O(n), O(n)
        """
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1]+1)
        
        return max(dp)
    
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
            本题也可以用贪心做；
            遇到nums[i + 1] > nums[i]的情况，count就++，
            否则count为1，记录count的最大值就可以了。
        """