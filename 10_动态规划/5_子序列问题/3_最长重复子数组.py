"""
    题目描述:
        给两个整数数组 nums1 和 nums2 ，
        返回 两个数组中 公共的 、长度最长的子数组的长度 。

    链接: https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
"""

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            1. dp[i][j]: nums1 中 i 结尾， nums2 中 j 结尾的最长子数组长度；
            2. 递推:
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
            3. 初始化:
                dp[0][j] = 1 if nums1[0] == nums2[j] else 0
                dp[i][0] = 1 if nums1[i] == nums2[0] else 0
            4. 从前到后
        """
        dp = [[0]*len(nums2) for _ in range(len(nums1))]

        for i in range(len(nums1)):
            dp[i][0] = 1 if nums1[i] == nums2[0] else 0
        
        for j in range(len(nums2)):
            dp[0][j] = 1 if nums1[0] == nums2[j] else 0

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        max_length = max(max(row) for row in dp)

        return max_length
    
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
            本题还可以利用滚动数组，优化空间开销；
            但是要注意使用滚动数组后的遍历顺序。

            不同于二维数组，滚动数组第一列的初始化不再为0，因此长要增加1
            即二维数组大小为 len(nums1)+1 * len(nums2)+1
        """
        dp = [0] * (len(nums2) + 1)

        for i in range(1, len(nums1)+1):
            for j in range(len(nums2), 0 , -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    # 注意此处赋 0 的操作不可省略
                    dp[j] = 0
        
        return max(dp)