"""
    题目描述:
        在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。

        现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足:
            nums1[i] == nums2[j]
            且绘制的直线不与任何其他连线（非水平线）相交。
        
        请注意，连线即使在端点也不能相交: 每个数字只能属于一条连线。

        以这种方法绘制线条，并返回可以绘制的最大连线数。

    链接: https://leetcode-cn.com/problems/uncrossed-lines
"""

from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
            题目分析:
                直线不能相交，这就是说明在字符串A中 找到一个与字符串B相同的子序列，
                且这个子序列不能改变相对顺序，只要相对顺序不改变，链接相同数字的直线就不会相交。

                因此本题即为求两个字符串的最长公共子序列的长度。
                
            1. dp[i][j]: 
                长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
            2. 递推:
                if (text1[i - 1] == text2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        """
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

