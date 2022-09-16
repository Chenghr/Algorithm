"""
    题目描述:
        n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

        你需要按照以下要求，给这些孩子分发糖果:
            每个孩子至少分配到 1 个糖果。
            相邻两个孩子评分更高的孩子会获得更多的糖果。
            请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

    链接: https://leetcode-cn.com/problems/candy
"""

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
            这道题目一定是要确定一边之后，再确定另一边，如果两边一起考虑一定会顾此失彼。
            分两趟处理；
            1. 从左到右遍历，保证右边的孩子比左边的孩子多一个糖果；
            2. 从右到左遍历，保证左边的孩子比右边的孩子多一个糖果；
        """
        candy = [1] * len(ratings)

        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                candy[i+1] = candy[i] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                # 这里注意要选择较大的那个，否则不满足条件
                candy[i-1] = max(candy[i-1], candy[i] + 1)
        
        return sum(candy)