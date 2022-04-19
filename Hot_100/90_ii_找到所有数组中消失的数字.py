"""
    题目描述:
        给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
        请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
    
    进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 
         你可以假定返回的数组不算在额外空间内。

    链接: https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """暴力: 开辟一个大小为 n 的标记数组；
            遍历数组得到输出
        """
        tag = [True] * (len(nums)+1)

        for num in nums:
            tag[num] = False
        
        ans = []
        for i in range(1, len(tag)):
            if tag[i]:
                ans.append(i)
        
        return ans

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            注意到标记数组的有效长度为 n；nums 的有效长度也为 n。
            那么考虑让 nums 作为标记数组。

            遍历 nums，每遇到一个数 x，就让 nums[x-1] 增加 n。
            由于 nums 中所有数均在 [1,n] 中，增加以后，这些数必然大于 n。

            最后我们遍历 nums，若 nums[i] 未大于 n，就说明没有遇到过数 i+1。
            这样我们就找到了缺失的数字。

            注意，当我们遍历到某个位置时，其中的数可能已经被增加过，
            因此需要对 n 取模来还原出它本来的值
        """

        for num in nums:
            num %= len(nums)  # 可能被别的数加过，保证数组不越界
            nums[num-1] += len(nums)  # nums[-1] 刚好对应 num 为 n

        ans = []
        for i, num in enumerate(nums):
            if num <= len(nums):  # 这里可以取等
                ans.append(i+1)
        
        return ans
