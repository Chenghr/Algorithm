"""
    题目描述:
        给定一个含有 n 个正整数的数组和一个正整数 target 。
        找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
        并返回其长度。如果不存在符合条件的子数组，返回 0 。

    链接: https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            因为是连续子数组，因此可以考虑滑动窗口；
            记录窗口内当前和为 sum
                如果 sum < target: 右指针向右移动直到大于或者等于 target；
                如果 sum > target: 左指针右移直到小于或者等于 target；
                如果 sum == target: 记录当前子数组长度，比较是否为最小值
        """
        min_length = float('inf')

        left, curSum = 0, 0  # 左闭右闭

        for right in range(len(nums)):

            curSum += nums[right]

            while curSum >= target and left <= right:
                # 在收缩左边界的时候也要找最小的长度
                min_length = min(min_length, right - left + 1)
                curSum -= nums[left]
                left += 1
        
        if min_length == float('inf'):
            return 0
        
        return min_length