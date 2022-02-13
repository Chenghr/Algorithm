"""
    题目描述:
        如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。
        第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

            例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

            相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，
            第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

        子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

        给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

    进阶: 你能否用 O(n) 时间复杂度完成此题?

    链接: https://leetcode-cn.com/problems/wiggle-subsequence
"""

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            贪心思想:
                让峰值尽可能的保持峰值，然后删除单一坡度上的节点。
            
            注意峰顶和峰底的判断条件，eg: 12332
            注意差值的更新时间，只有找到一个峰值的时候才需要更新
        """
        # 避免只含有一个元素或者两个相等元素的情况
        count = 1  
        prediff = 0  

        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]

            if prediff * curdiff <= 0 and curdiff != 0:
                count += 1
                prediff = curdiff  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        
        return count
    
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
            动态规划思想:
                对于我们当前考虑的这个数，要么是作为山峰（即nums[i] > nums[i-1]），
                要么是作为山谷（即nums[i] < nums[i - 1]）。
            
            设 dp状态 dp[i][0]，表示考虑前i个数，第i个数作为山峰的摆动子序列的最长长度
            设 dp状态 dp[i][1]，表示考虑前i个数，第i个数作为山谷的摆动子序列的最长长度
            
            则转移方程为:
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)，其中0 < j < i且nums[j] < nums[i]，表示将nums[i]接到前面某个山谷后面，作为山峰。
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)，其中0 < j < i且nums[j] > nums[i]，表示将nums[i]接到前面某个山峰后面，作为山谷。

            初始状态:
                由于一个数可以接到前面的某个数后面，也可以以自身为子序列的起点，所以初始状态为:
                dp[0][0] = dp[0][1] = 1。
            
            进阶:
                可以用两棵线段树来维护区间的最大值
        """