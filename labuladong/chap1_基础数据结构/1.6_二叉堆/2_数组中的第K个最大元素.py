"""
    题目描述:
        给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
        请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
    
    链接: https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""

from typing import List
from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            思路一:
                快速搜索算法，快排算法的变种；
        """
        def partition(nums, left, right):
            """一趟快排，返回基准元素最后的下标"""
            base = left

            while left < right:
                # 从右向左找到第一个大于基准点元素的
                while left < right and nums[right] <= nums[base]:
                    right -= 1

                # 从左向右找到第一个小于基准点元素的
                while left < right and nums[left] >= nums[base] :
                    left += 1
                
                nums[left], nums[right] = nums[right], nums[left]
            
            nums[base], nums[left] = nums[left], nums[base]
        
            return left 

        left, right = 0, len(nums)-1

        while left <= right:
            # 一趟划分后的基准点下标
            mid = partition(nums, left, right)

            if mid == k-1:
                # 下标为 k-1 表示恰为第 k 大的元素
                return nums[mid]
            elif mid < k-1:
                # 目标元素在右边
                left = mid + 1
            elif mid > k-1:
                # 目标元素在左边，注意区间是左闭右闭
                right = mid - 1
        
        return nums[left]  # 只有一个元素

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
            思路二:
                维护一个大小为k的小顶堆；注意进出栈的细节
        """
        pq = PriorityQueue()

        for num in nums:
            pq.put(num)  # 每个元素都进一次二叉堆

            if pq.qsize() > k:
                drop = pq.get()
        
        return pq.get()

example = Solution()
result = example.findKthLargest([3,2,1,5,6,4], 2)
print(result)
