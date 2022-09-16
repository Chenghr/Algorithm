"""
    题目描述:
        给你一个整数数组 nums ，你需要找出一个 连续子数组 ，
        如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

        请你找出符合题意的 最短 子数组，并输出它的长度。
    
    时间复杂度为 O(n) 的解决方案

    链接: https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
"""
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            将子数组分成三段 nums1, nums2, nums3;
            只对 nums2 排序说明 nums1，以及 nums3 内部顺序和最终顺序相同；
            那么将 nums 排序，找出排序前后的最长相同前后缀即可。
        """
        nums_post = nums.copy()
        nums_post.sort()

        preLen, index = 0, 0
        while index < len(nums) and nums[index] == nums_post[index]:
            preLen += 1
            index += 1
        
        postLen, index = 0, len(nums)-1
        while index > -1 and nums[index] == nums_post[index]:
            postLen += 1
            index -= 1
        
        return len(nums) - min(len(nums), preLen+postLen)

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
            一趟遍历
            把这个数组分成三段，左段和右段是标准的升序数组，中段数组是无序的

            考虑中段数组，设其左边界为L，右边界为R，最大值max,最小值min
                从左到右遍历，如果进入右段，就没有比max小的数，所以最后一个比max小的数为中段的右边界R
                从右到左遍历，如果进入左段，就没有比min大的数，所以最后一个比min大的数为中段的左边界L

            https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
        """
        left, right = -1, -1

        maxVal, minVal = -float('inf'), float('inf')

        for i in range(len(nums)):
            # 从左向右遍历，记录最后一个比max小的下标
            if nums[i] >= maxVal:
                maxVal = nums[i]
            else:
                right = i
            
            # 从右向左遍历，记录最后一个比min大的下标
            j = len(nums)-1 - i
            if nums[j] <= minVal:
                minVal = nums[j]
            else:
                left = j

        # 对于链表有序的情况需要特殊处理，此时right = -1
        return 0 if right == -1 else right - left + 1
