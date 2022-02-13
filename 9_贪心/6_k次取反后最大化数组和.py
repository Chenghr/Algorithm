"""
    题目描述:
        给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组:
            选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
            重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

        以这种方式修改数组后，返回数组 可能的最大和 。

    链接: https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations
"""

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        # 绝对值大小降序排列
        nums.sort(key=lambda x: abs(x), reverse=True)

        for i in range(len(nums)):
            if k == 0:
                break
            
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        if k := k % 2:
            nums[-1] = -nums[-1]
        
        return sum(nums)
