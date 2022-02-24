"""
    题目描述:
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

        你可以按任意顺序返回答案。

    进阶: 你可以想出一个时间复杂度小于 O(n2) 的算法吗？

    链接: https://leetcode-cn.com/problems/two-sum
"""

from typing import List

from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            由于返回数组下标，因此不可使用排序算法更改数组相对顺序；

            1. 空间换时间:
                先遍历一次数组，记录每个元素出现的次数（map）；
                在遍历一次数组，判断对应元素是否出现即可；

                O(n), O(n)
            
            2. 两层 for 循环;
                O(n*2), O(1)
        """
        dic = defaultdict(list)

        for i, num in enumerate(nums):
            dic[num].append(i)
        
        for i, num in enumerate(nums):
            if target - num != num and len(dic[target - num]) != 0:
                return [i, dic[target - num][0]]
            
            if target - num == num and len(dic[num]) == 2:
                return dic[num]
        
        return [-1, -1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """还可以进一步优化代码 
        """
        record = dict()

        for idx, val in enumerate(nums):

            if target - val not in record:
                record[val] = idx
            else:
                return [record[target-val], idx]
        
        return [-1, -1]