"""
    题目进阶:
        所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
        这种情况下，求偷窃到的最大金额。
    
    链接: https://leetcode-cn.com/problems/house-robber-ii/
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            将环切割成两个线性房屋，即 0 ~ len(nums)-2; 1 ~ len(nums)-1;
            然后在两个线性房屋中使用 打家劫舍1 中的 dp 思路；
            在结果中选择较大的那个作为最终值即可。
        """
        if len(nums) == 1:
            return nums[0]

        return max(self.robRange(nums, 0, len(nums)-1), self.robRange(nums, 1, len(nums)))
        
    def robRange(slef, nums, begin, end):
        """begin, end 左闭右开
        """
        if end - begin == 1:
            return nums[begin]

        dp = [0] * end

        dp[begin] = nums[begin]
        dp[begin+1] = max(nums[begin], nums[begin+1])

        for j in range(begin+2, end):
            dp[j] = max(dp[j-1], dp[j-2]+nums[j])
        
        return dp[end-1]
        