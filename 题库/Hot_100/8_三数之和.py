"""
    题目描述:
        给你一个包含 n 个整数的数组 nums，
        判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
        请你找出所有和为 0 且不重复的三元组。

        注意: 答案中不可以包含重复的三元组。

    链接: https://leetcode-cn.com/problems/3sum
"""

from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            主要有两个问题:
                1. 降低时间开销；（暴力为 O(n*3）)
                2. 去除重复三元组

            时间换空间的思路，使用哈希数组来降低查找的时间开销；
            由于返回具体的元素，因此可以考虑通过排序来去重；

            出现问题:  采用哈希数组做判定，没办法消除前面搜索过的元素的影响；
            应该采用双指针法来降低时间开销。

            「不重复」的本质是什么？我们保持三重循环的大框架不变，只需要保证:
                第二重循环枚举到的元素不小于当前第一重循环枚举到的元素；
                第三重循环枚举到的元素不小于当前第二重循环枚举到的元素。
            
            当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，
            第二个元素是递减的，那么就可以使用双指针的方法.
        """
        
        if len(nums) < 3:
            return []

        nums.sort()

        result = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                # 去重
                continue

            j, k = i+1, len(nums)-1

            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                if k < len(nums)-2 and nums[k] == nums[k+1]:
                    k -= 1
                    continue

                if nums[j] + nums[k] == -nums[i]:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1

        return result