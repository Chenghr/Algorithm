"""
    题目描述:
        给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），
        返回 nums 中每个元素的 下一个更大元素 。

        数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，
        这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

    链接: https://leetcode-cn.com/problems/next-greater-element-ii
"""

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
            处理循环数组的思路:
                1. 将两个 nums 数组拼接在一起，使用单调栈计算；然后将结果集 resize 为原数组即可；
                2. 遍历两次 nums 数组，中间使用取余操作避免越界；同时避免额外的空间开销。
            
            单调栈:
                存储数组下标；
                从栈顶到栈底递增；
        """
        result = [-1] * len(nums)

        stack = [0]

        for i in range(1, len(nums)*2):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i % len(nums)]
            
            stack.append(i % len(nums))
        
        return result

example = Solution()
result = example.nextGreaterElements([5,4,3,2,1])
print(result)
                
