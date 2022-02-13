"""
    题目描述:
        给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。
        判断你是否能够到达最后一个下标。
    
    链接: https://leetcode-cn.com/problems/jump-game/
"""

"""
    题目描述:
        给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。
        你的目标是使用最少的跳跃次数到达数组的最后一个位置。
        假设你总是可以到达数组的最后一个位置。
    
    链接: https://leetcode-cn.com/problems/jump-game-ii/

"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            问题转化为 跳跃覆盖范围究竟可不可以覆盖到终点；

            每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。

            贪心算法局部最优解: 每次取最大跳跃步数（取最大覆盖范围）;
            整体最优解: 最后得到整体最大覆盖范围，看是否能到终点。

            局部最优推出全局最优，找不出反例，试试贪心.
        """

        max_length = nums[0]

        for idx, num in enumerate(nums):
            if idx > max_length:
                return False
            
            max_length = max(max_length, idx + num)

            if max_length >= len(nums)-1:
                return True
        
        return True

    def jump(self, nums: List[int]) -> int:
        """
            以最小的步数增加覆盖范围，覆盖范围一旦覆盖了终点，得到的就是最小步数.

            统计两个覆盖范围，当前这一步的最大覆盖和下一步最大覆盖。

            贪心的思路:
                局部最优: 当前可移动距离尽可能多走，如果还没到终点，步数再加一。
                整体最优: 一步尽可能多走，从而达到最小步数。
        """
        cur_cover, next_cover = 0, nums[0]
        count = 0

        for i, num in enumerate(nums):
            if i > cur_cover:
                # 走出当前覆盖的最大范围，则增加一步，更新范围到下一步的最大范围
                cur_cover = next_cover
                count += 1
            
            if cur_cover >= len(nums)-1:
                # 找到终点
                return count
            
            # 在当前覆盖的范围内更新下一步覆盖的最大值
            next_cover = max(next_cover, i+num)
        
        return count