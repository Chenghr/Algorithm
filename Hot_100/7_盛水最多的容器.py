"""
    题目描述:
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

        返回容器可以储存的最大水量。

        说明: 你不能倾斜容器。

    链接: https://leetcode-cn.com/problems/container-with-most-water
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
            暴力算法；
            两层 for 循环.
        """
        maxArea = 0

        for i in range(len(height)-1):
            for j in range(i, len(height)):
                maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        
        return maxArea

    def maxArea(self, height: List[int]) -> int:
        """
            对暴力算法进行优化；
            可以发现是从左向右找左边界，从右向左找右边界；双指针
        """
        left, right = 0, len(height)-1
        maxArea = min(height[left], height[right]) * (right - left)

        while left <= right:
            bound = min(height[left], height[right])

            # 移动短板
            if height[left] < height[right]:
                while left <= right and height[left] <= bound:
                    left += 1
            else:
                while left <= right and height[right] <= bound:
                    right -= 1
            
            newArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, newArea)
        
        return maxArea