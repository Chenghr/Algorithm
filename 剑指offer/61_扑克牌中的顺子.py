"""
    从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。
    2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
"""

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """
            成顺: 
                1. 不包含重复数字；
                2. 去除 0 后的最大值和最小值间隔小于等于 5均可。
            
            去重: 排序，或者使用哈希数组
        """
        dic = [0] * 14  # 这里可以使用 set 去重

        maxNum, minNum = 0, 14
        for num in nums:
            if num > 0 and dic[num] > 0:
                return False
            
            dic[num] += 1
            maxNum = max(maxNum, num)
            minNum = min(minNum, num) if num > 0 else minNum
        
        return maxNum - minNum <= 4

