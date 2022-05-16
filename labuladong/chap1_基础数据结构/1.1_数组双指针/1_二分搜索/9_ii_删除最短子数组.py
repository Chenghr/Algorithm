"""
    给你一个整数数组 arr ，请你删除一个子数组（可以为空），
    使得 arr 中剩下的元素是 非递减 的。

    一个子数组指的是原数组中连续的一个子序列。
    请你返回满足题目要求的最短子数组的长度。
"""

from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """贪心 + 双指针法求解；

            第二部分的求解还可以使用二分查找；
            即使用二分查找在右区间寻找大于等于 arr[i] 的值的下标。
        """
        left, right = 0, len(arr)-1

        while left < len(arr)-1 and arr[left] <= arr[left+1]:
            left += 1
        
        if left == len(arr)-1:
            return 0

        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1

        ans = min(len(arr)-left-1, right)

        i, j = 0, right
        while i <= left and j < len(arr):
            if arr[i] <= arr[j]:
                ans = min(ans, j-i-1)
                i += 1
            else:
                j += 1
        
        return ans

a = Solution()
ans = a.findLengthOfShortestSubarray([1,2,3,3,10,1,3,3,5])
print(ans)