"""
    题目描述:
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    链接: https://leetcode-cn.com/problems/trapping-rain-water/
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
            暴力求解:
                对于位置 i ，可装下的水量为 左边最高的柱子和右边最高的柱子中的最小值 减去 本身的高度，即：
                    water[i] = min(left_max, right_max) - height[i]
                
                复杂度:O(n^2), O(1)
        """
        waterSum = 0

        for i in range(len(height)):
            left_max, right_max = height[i], height[i]

            # 从左选择最大值
            for left_idx in range(i):
                left_max = max(left_max, height[left_idx])
            
            # 向右选择最大值
            for right_idx in range(i, len(height)):
                right_max = max(right_max, height[right_idx])
            
            waterSum += min(left_max, right_max) - height[i]
            
        return waterSum
    
    def trap(self, height: List[int]) -> int:
        """
            暴力求解 + 备忘录:
                暴力求解中对于每个 i 都要遍历一次寻找最大值，可以使用记忆数组存储最大值，避免重复查询。

                leftMax[i]: 0 ~ i 中的最大值
                rightMax[i]: i ~ len(height)-1 中的最大值

                这里也可以说是动态规划解法，因为在求解最大值得时候可以视为使用了递推公式。
            
            O(n) + O(n)
        """
        leftMax, rightMax = [0]*len(height), [0]*len(height)

        # 前 i 个数中的最大值
        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        # 第 i 个数右边的最大值（包括自身）
        rightMax[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        waterSum = 0
        for i in range(len(height)):
            waterSum += min(leftMax[i], rightMax[i]) - height[i]
        
        return waterSum

    def trap(self, height: List[int]) -> int:
        """
            双指针法:
                可以考虑进一步优化空间开销。

                核心思想: 
                    我们只关心左右边界中较短的那个边界；
                    将左右边界先固定在两边，然后移动较短的边界，向中间推进；

                left, right: 左右边界
                l_max: 0 ~ left 中的最大值;
                r_max: right ~ len(height)-1 中的最大值;

            O(n) + O(1)
        """
        left, right = 0, len(height)-1
        l_max, r_max = 0, 0

        waterSum = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])

            if l_max < r_max:
                # 移动左边界
                waterSum += l_max - height[left]
                left += 1
            else:
                # 移动右边界
                waterSum += r_max - height[right]
                right -= 1
        
        return waterSum
    
    def trap(self, height: List[int]) -> int:
        """
            单调栈解法:
                从行方向出发解决问题；

                1. 单调栈内元素顺序:
                    从栈头（元素从栈头弹出）到栈底的顺序应该是从小到大的顺序。
                    因为一旦发现添加的柱子高度大于栈头元素了，此时就出现凹槽了，需要计算雨水量了。

                2. 对相同高度的柱子的处理:
                    遇到相同的元素，更新栈内下标，就是将栈里元素（旧下标）弹出，将新元素（新下标）加入栈中。
                    因为我们要求宽度的时候 如果遇到相同高度的柱子，需要使用最右边的柱子来计算宽度。
                
                3. 栈内保存的数值:
                    雨水量用长*宽计算，长可用 height 数组获取，宽用下标获取，因此存下标即可。
                
                4. 单调栈处理逻辑:
                    先将下标0的柱子加入到栈中，然后开始从下标1开始遍历所有的柱子；

                    if 当前遍历的元素（柱子）高度小于栈顶元素的高度:
                        元素入栈; (栈里本来就要保持从小到大的顺序)
                    elif 当前遍历的元素（柱子）高度等于栈顶元素的高度:
                        更新栈顶元素;
                    elif 当前遍历的元素（柱子）高度大于栈顶元素的高度:
                        出现凹槽，需要计算；持续更新栈顶元素；

                        取栈顶元素，将栈顶元素弹出，这个就是凹槽的底部，也就是中间位置，下标记为mid，对应的高度为height[mid]；
                        此时的栈顶元素st.top()，就是凹槽的左边位置，下标为st.top()，对应的高度为height[st.top()]；
                        当前遍历的元素i，就是凹槽右边的位置，下标为i，对应的高度为height[i]；

                        雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
                        雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度，注意此处有连续高度相同的情况，因此宽度不一定为 1）；

            O(n) + O(n)
        """
        # stack储存index，用于计算对应的柱子高度
        stack = [0]

        waterSum = 0
        for i in range(1, len(height)):

            if height[i] < height[stack[-1]]:
                # 情况一
                stack.append(i)
            
            elif height[i] == height[stack[-1]]:
                # 情况二
                stack[-1] = i
                # 等价写法
                # stack.pop()
                # stack.append(i)

            elif height[i] > height[stack[-1]]:
                # 情况三，抛弃所有较低的柱子

                while stack and height[i] > height[stack[-1]]:
                    mid_height = height[stack[-1]]
                    stack.pop()

                    if stack:
                        right_height = height[i]
                        left_height = height[stack[-1]]

                        # 高
                        h = min(left_height, right_height)
                        # 宽，注意只求中间宽度
                        w = i - stack[-1] -1

                        waterSum += h*w
                
                stack.append(i)
        
        return waterSum
