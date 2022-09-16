"""
    题目描述:
        整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
        整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。
        更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
        如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

        例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
        类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
        而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
        
        给你一个整数数组 nums ，找出 nums 的下一个排列。
        必须 原地 修改，只允许使用额外常数空间。

    链接: https://leetcode-cn.com/problems/next-permutation
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
            Do not return anything, modify nums in-place instead.
            
            两遍扫描
            下一个排列总是比当前排列大；除非当前排列已经是最大排列；
            具体的：
                1. 左边找到一个较小值，右边找到一个较大值，交换，使得当前排列字典序变大；
                2. 由于要求紧跟的下一个字典序；
                    因此较小数要尽可能靠右，较大数尽可能靠左且尽可能小；
                    且交换后较大数右侧有重新排序为升序。
            
            算法设计:
                1. 从后向前查找第一个顺序对(i, i+1)，满足 a[i] < a[i+1];
                   则较小数为 a[i]，且 [i+1, n) 必为下降序列；
                2. 如果找到了顺序对，则从 [i+1, n) 中从后向前查找第一个元素 j 满足 a[i] < a[j];
                   较大数即为 a[j];
                3. 交换 a[i], a[j]，此时 [i+1, n) 必为下降序列；可以直接用双指针反转区间，避免排序。
        """
        left = len(nums)-2
        while left >= 0 and nums[left] >= nums[left+1]:
            # 寻找连续顺序对
            left -= 1

        if left >= 0:
            # 找到符合条件的顺序对
            right = len(nums)-1

            while right > left and nums[right] <= nums[left]:
                # 查找第一个大于 nums[left] 的值
                right -= 1

            # 交换
            nums[left], nums[right] = nums[right], nums[left]
        
        # 维持 left + 1 后的元素升序
        left, right = left+1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return