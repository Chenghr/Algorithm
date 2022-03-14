"""
    题目描述:
        给定一个整数数组  nums，处理以下类型的多个查询:

        计算索引 left 和 right（包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
        
        实现 NumArray 类：
            - NumArray(int[] nums) 使用数组 nums 初始化对象
            - int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，
              包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

    链接: https://leetcode-cn.com/problems/range-sum-query-immutable
"""

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self.preSum = []
        curSum = 0

        for num in nums:
            curSum += num
            self.preSum.append(curSum)

    def sumRange(self, left: int, right: int) -> int:
        """会多次调用该函数；可以考虑使用前缀和预处理，避免每次调用都遍历数组。
        """
        if left == 0:
            return self.preSum[right]
        
        return self.preSum[right] - self.preSum[left-1]

        """
            ⽤⼀个新的数组 preSum 记录 nums[0..i-1] 的累加和;
            返回 preSum[right + 1] - preSum[left];
        """


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)