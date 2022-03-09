"""
    题目描述:
        给你一个整数数组 nums 和一个整数 target 。
        向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式:

        例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，
        然后串联起来得到表达式 "+2-1" 。
        
        返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

    链接: https://leetcode-cn.com/problems/target-sum
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            回溯法求解:
                每个元素有两种状态，取正或者取负；
                递归 + 回溯 可以求解
        """
        result = 0

        def backtracking(idx: int, curSum: int):
            nonlocal nums, target, result

            if idx == len(nums):
                # idx 从 0 开始
                if curSum == target:
                    result += 1

                return
            
            for i in range(idx, len(nums)):
                curSum += nums[i]

                backtracking(i+1, curSum)

                # 回溯
                curSum -= nums[i]*2
            
            # 最后一个元素取负的判断
            if curSum == target:
                result += 1

            return
        
        backtracking(0, 0)

        return result
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            回溯法显然会超时，因此考虑动态规划解法。

            动态规划:
                每个元素有正负两种状态，可以对应选中或者不选中，假设选中的为正，未选中的为负；
                可以应用01背包
                问题转换为装满指定容量的背包有几种方法。

            bag_size = (sum + target) / 2
            物品重量: nums[i], 物品价值: nums[i]

            具体的:
            1. dp[j]: 装满容量 j 的背包最大方法数；
            2. 递推公式: 
                dp[j] += dp[j-nums[i]]
            3. 初始化:
                dp[0] = 1,(一切的起点，为 0 则恒为 0)
            4. 遍历顺序:
                外层遍历数组，内层逆序遍历背包容量
            
            -1000 <= target <= 1000
        """
        if (sum(nums) + target) % 2 != 0:
            return 0

        # 保证 bag_size 为正
        # -1000 <= target <= 1000
        if target > 0 :
            bag_size = int((sum(nums) + target) / 2)
        else:
            bag_size = int((sum(nums) - target) / 2)

        dp = [0] * (bag_size + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(bag_size, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        
        return dp[bag_size]

example = Solution()
result = example.findTargetSumWays([1,1,1], 1)
print(result)