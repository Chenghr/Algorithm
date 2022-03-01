"""
    题目描述:
        你正在探访一家农场，农场从左到右种植了一排果树。
        这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

        你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果:

            你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
            你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。
            采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
            一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
        
        给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。

    链接: https://leetcode-cn.com/problems/fruit-into-baskets
"""

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
            双指针；滑动窗口
            在连续区间内，只能选择两种树，求最大连续区间长度；

            两个问题:
                1. 双指针的移动策略；
                2. 选中水果种类的更新；
                    抓住连续区间的特性，出现第三种水果时，选中的水果只能为第三种水果前的水果以及第三种水果两种；
                    向前找到 left 最远的可达距离即可。
        """
        choose = []
        left, max_length = 0, 0

        for right in range(len(fruits)):

            if fruits[right] not in choose:

                if len(choose) < 2:
                    choose.append(fruits[right])
                else:
                    # 更新最大区间长度
                    max_length = max(max_length, right - left)

                    # 从 right 开始向左遍历， 更新 left 下标
                    left = right -1

                    while left > 0 and fruits[left] == fruits[left-1]:
                        left -= 1
                    
                    choose = [fruits[left], fruits[right]]
            
            # 避免水果种类小于3类，直接遍历到列表末尾的情况出现
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    def totalFruit(self, fruits: List[int]) -> int:
        """
            更新水果的另一种思路:
                采用字典记录；
                水果类型作为键，值为对应树的数目
                移动右边界，则+1，移动左边界，则-1；某种水果数目为0时，则删除键。
        """
        dic = defaultdict(int)

        left, max_length = 0, 0

        for right in range(len(fruits)):
            dic[fruits[right]] += 1

            while len(dic) > 2:
                # 水果种类大于 2，需要移动左边界
                dic[fruits[left]] -= 1

                if dic[fruits[left]] == 0:
                    # 彻底移除一种树
                    del(dic[fruits[left]])

                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
