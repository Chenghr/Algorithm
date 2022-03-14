"""
    题目描述:
        假设你有⼀个⻓度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k 个更新的操作。

        其中，每个操作会被表示为⼀个三元组：[startIndex, endIndex, inc] ，
        你需要将⼦数组 A[startIndex, ..., endIndex]（包括 startIndex 和 endIndex）增加 inc。 

        请你返回 k 次操作后的数组。
    
    链接: https://mp.weixin.qq.com/s/123QujqVn3--gyeZRhxR-A
"""

class Solution:
    def getDiffArray(self, nums: list[int]) -> list[int]:
        """获取差分数组
        """
        diff = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i-1]
        
        return diff
    
    def getPreArray(self, diff: list[int]) -> list[int]:
        """从差分数组中恢复原始数组
        """
        nums = [diff[0]] * len(diff)

        for i in range(1, len(diff)):
            nums[i] = nums[i-1] + diff[i]
        
        return nums

    def getModifigedArray(self, nums: list[int], updates: list[list[int]]):
        """使用差分数组的思想
        """
        diff = self.getDiffArray(nums)

        for update in updates:
            # increment 操作
            diff[update[0]] += update[2]

            if update[1]+1 < len(diff):
                diff[update[1]+1] -= update[2]
        
        nums = self.getPreArray(diff)

        return nums