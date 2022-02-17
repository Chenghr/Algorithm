"""
    题目描述:
        给你一个 只包含正整数 的 非空 数组 nums 。
        请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    
    链接: https://leetcode-cn.com/problems/partition-equal-subset-sum/
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            n 个物品从中选择，目标总和为 sum(nums)/2;

            物品不可重复，对标01背包问题:
                背包容量: sum(nums)/2;
                商品重量: 元素值；商品价值: 元素值；
                背包正好装满则满足题意；
                背包中每个元素不可重复选取
            
            1. dp[j]: 背包容量为 j，最大价值总和:
            2. dp[j] = max(d[j], dp[j - nums[i]] + nums[i])
            3. 初始化: 
                要求的是背包恰装满时的最大价值:
                因此 dp[0] = 0, dp[j] = -float('inf')， j != 0
            4. 从后向前遍历;
        """
        """
            题解思路:
                主要要理解，题目中物品是nums[i]，重量是nums[i]，价值也是nums[i]，背包体积是sum/2。
                由此可以推导出: 
                    dp[i]的数值一定是小于等于i的。
                    如果dp[i] == i 说明，集合中的子集总和正好可以凑成总和i。
                最后判断 dp[-1] 是否等于 sum/2 即可。
        """ 
        if sum(nums) % 2 != 0:
            return False
        
        bag_size = int(sum(nums) / 2)
        dp = [-float('inf')] * (bag_size + 1)

        dp[0] = 0

        for i in range(len(nums)):
            for j in range(bag_size, nums[i]-1, -1):
                if nums[i] <= j:
                    dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        
        if dp[-1] >= 0:
            return True
        
        return False
        

example = Solution()
result = example.canPartition([2,2,1,1])
print(result)