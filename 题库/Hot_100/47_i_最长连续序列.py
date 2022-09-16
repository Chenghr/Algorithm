"""
    题目描述:
        给定一个未排序的整数数组 nums ，
        找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

        请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

    链接: https://leetcode-cn.com/problems/longest-consecutive-sequence
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            哈希表
            暴力求解思路:
                对数组内的每个元素，求其作为起点得到的最大长度，然后从中获取最大值；
            
            优化:
                1. 采用哈希表存储元素；这样查找后续元素的时间复杂度为 O(1)；
                2. 并非所有元素都需要作为起点元素去搜索；只需要搜索断点出现的元素即可；即 x-1 未出现的 x；
                3. 数组中的重复元素可以去掉；无需考虑。

            综合以上；可以采用 set 作为字典的构造。 
        """
        nums_set = set(nums)  # 构造字典，且去重

        longest_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                # 找到一个搜索起点
                current_num = num
                current_length = 1

                while current_num+1 in nums_set:
                    current_length += 1
                    current_num += 1
                
                longest_length = max(longest_length, current_length)
            
        return longest_length
        

        