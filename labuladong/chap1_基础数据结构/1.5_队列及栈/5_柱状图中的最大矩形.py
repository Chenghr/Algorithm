"""
    题目描述:
        给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
        求在该柱状图中，能够勾勒出来的矩形的最大面积。
    
    链接: https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            指定区间内的矩形面积构成: 最小值 * 区间长度
            因此问题可以转化为指定区间内求解最小值
            换句话说，对于值 heights[i] ，求解其最小值区间，即：
                分别向左向右求解其下一个更小值的下标，这样值 heights[i] 构成的矩形即求出；

            求解下一个最值 -> 单调栈；

            本题的单调栈:
                栈内元素: 数组下标
                栈内顺序: 从栈顶到栈底递减
            
            注意 leftIdx 初始化为 -1，rightIdx 初始化为 len(heights) 有利于后续计算面积形式的统一
        """
        leftIdx = [-1] * len(heights)  # 存储左边最近小于当前元素的下标
        rightIdx = [len(heights)] * len(heights)  # 存储右边最近小于元素的下标

        stack = [0]
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                rightIdx[idx] = i
            
            stack.append(i)
        
        stack = [len(heights)-1]
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                leftIdx[idx] = i
            
            stack.append(i)      

        maxArea = 0 
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i]*(rightIdx[i]-leftIdx[i]-1))
            
        return maxArea

    def largestRectangleArea_violent(self, heights: List[int]) -> int:
        """双指针法（暴力解法）:
            对每个 i 向两边搜索第一个最小值下标；

            超时； O(n^2)
        """
        maxArea = 0

        for i in range(len(heights)):
            left, right = i, i

            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            
            while right <= len(heights)-1 and heights[right] >= heights[i]:
                right += 1
            
            maxArea = max(maxArea, heights[i] * (right-left-1))

        return maxArea

    def largestRectangleArea_dp(self, heights: List[int]) -> int:
        """动态规划；预先求解出边界
        """
        minleftIdx = [-1] * len(heights)  # 存储左边最近小于当前元素的下标
        minrightIdx = [len(heights)] * len(heights)  # 存储右边最近小于元素的下标

        for i in range(1, len(heights)):
            pre = i-1

            while pre >= 0 and heights[pre] >= heights[i]:
                # 递归的向前搜索，找到第一个小于当前值的下标
                pre = minleftIdx[pre]
            
            minleftIdx[i] = pre
        
        for i in range(len(heights)-2, -1, -1):
            post = i + 1

            while post <= len(heights)-1 and heights[post] >= heights[i]:
                # 递归的向后搜索，找到第一个大于当前值的下标
                post = minrightIdx[post]
            
            minrightIdx[i] = post
        
        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (minrightIdx[i]-minleftIdx[i]-1))

        return maxArea

    def largestRectangleArea_stack(self, heights: List[int]) -> int:
        """
            单调栈解法: （真）
                本题是要找每个柱子左右两边第一个小于该柱子的柱子，
                所以从栈头（元素从栈头弹出）到栈底的顺序应该是从大到小的顺序；

                栈顶和栈顶的下一个元素以及要入栈的三个元素组成了我们要求最大面积的高度和宽度；
                注意元素相等时的操作，依然会入栈，但是不影响计算，因为会持续推出栈顶元素，直到满足大小限制为止。
        """
        # 前后加入两个哨兵位置，避免额外构造 left，right 数组，利于后续计算; 高度非负，因此插入最小值
        heights.append(0)
        heights.insert(0,0)

        maxArea = 0

        stack = [0]

        for i in range(1, len(heights)):

            while stack and heights[i] < heights[stack[-1]]:
                # 需要出栈；每次出栈都需要计算一次面积
                top = stack.pop()
                # 出栈后的栈顶元素即为左边最近的较小值下标
                maxArea = max(maxArea, heights[top] * (i-stack[-1]-1))

            stack.append(i)

        return maxArea

example = Solution()
result = example.largestRectangleArea_stack([2,1,5,6,2,3])
print(result)