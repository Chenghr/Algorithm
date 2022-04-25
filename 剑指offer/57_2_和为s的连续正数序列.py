"""
    输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
    序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
"""

from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """数学推导
            利用等差数列和的形式，给定 left 和 target ，可以求解出 right；
            然后 right 满足: 
                right 为整数（连续和等于目标）；
                right > left（至少两个数）；即可
        """


    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """滑动窗口的另一种写法
        """
        ans, left, windowSum = [], 1, 1

        for right in range(2, target // 2 + 2):
            windowSum += right

            if windowSum > target:
                while windowSum > target and left < right:
                    windowSum -= left
                    left += 1
            
            if windowSum == target:
                ans.append(list(range(left, right+1)))
        
        return ans

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """连续数字和，因此最大的值为 target // 2 + 1
        """
        nums = [i for i in range(1, target // 2 + 2)]

        ans = []
        left, windowsSum = 0, 1

        for right in range(1, len(nums)):
            windowsSum += nums[right]
            
            if windowsSum > target:
                # 收缩 left
                while windowsSum > target and left < right:
                    windowsSum -= nums[left]
                    left += 1
            
            if windowsSum == target:
                ans.append(nums[left : right+1])
        
        return ans