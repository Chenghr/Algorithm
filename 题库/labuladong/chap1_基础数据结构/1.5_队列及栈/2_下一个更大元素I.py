"""
    题目描述:
        nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置右侧的第一个比 x 大的元素。

        给你两个没有重复元素的数组 nums1 和 nums2 ，下标从 0 开始计数，
        其中nums1 是 nums2 的子集。

        对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
        并且在 nums2 确定 nums2[j] 的 下一个更大元素 。
        如果不存在下一个更大元素，那么本次查询的答案是 -1 。

        返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的下一个更大元素 。

    提示:
        1 <= nums1.length <= nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 104
        nums1和nums2中所有整数 互不相同
        nums1 中的所有整数同样出现在 nums2 中
    
    进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

    链接: https://leetcode-cn.com/problems/next-greater-element-i
"""

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            暴力思路: 两层 for 循环； O(n^2)

            单调栈:
                栈内元素: 数组 nums2 中的值；本题只用到nums2中元素的顺序而无需下标；
                栈内顺序: 从栈顶到栈底递增；这样较大的元素就会出栈
        """
        dic = {}
        for i, num in enumerate(nums1):
            dic[num] = i

        result = [-1] * len(nums1)
        stack = [nums2[0]]  # 栈顶到栈底递增
        
        for i in range(1, len(nums2)):
            # 栈顶元素需要出栈
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                if num in dic:
                    result[dic[num]] = nums2[i]

            stack.append(nums2[i])
        
        return result
