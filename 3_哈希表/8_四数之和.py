"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
    0 <= a, b, c, d < n
    a、b、c 和 d 互不相同
    nums[a] + nums[b] + nums[c] + nums[d] == target

你可以按 任意顺序 返回答案 。

提示：
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109

https://leetcode-cn.com/problems/4sum/
"""

"""
思路分析:

1. 暴力求解
    四层 for 循环求解，时间复杂度 O(n^4)

2. 双指针法
    先排序（便于去重），再使用双指针法，可以减少一次遍历，时间复杂度 O(n^3)

# 注意:
    - 早停的条件不满足，break要删除
    - 要对 idx1 和 idx2 均去重
"""
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        if len(nums) < 4:
            return []

        nums.sort()

        result = []

        for idx1 in range(len(nums)-3):
                
            # 去重
            if idx1 >= 1 and nums[idx1] == nums[idx1-1]:
                continue

            for idx2 in range(idx1+1, len(nums)-2):

                # 去重
                if idx2 >= idx1+2 and nums[idx2] == nums[idx2-1]:
                    continue

                left = idx2+1
                right = len(nums)-1

                while (left < right):

                    if nums[idx1] + nums[idx2] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[idx1] + nums[idx2] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        # 找到一个可行解
                        result.append([nums[idx1], nums[idx2], nums[left], nums[right]])
                        
                        while (left < right and nums[left] == nums[left+1]):
                            left += 1

                        while (left < right and nums[right] == nums[right-1]):
                            right -= 1
                        
                        left += 1
                        right -= 1
            
        return result

solution = Solution()
print(solution.fourSum([2, 2, 2, 2, 2], 8))