"""
    输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，
    打印能拼接出的所有数字中最小的一个。

    说明:
        输出结果可能非常大，所以你需要返回一个字符串而不是整数
        拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""

from typing import List
import functools

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """将数字字符串化；对字符串排序；
            规定 排序判断规则 为：

            若拼接字符串 x + y > y + x，则 x “大于” y ；
            反之，若 x + y < y + x，则 x “小于” y ；
        
            保证了上序性质后，直接将字符串拼接起来即可。
        """
        def compare(x, y):
            a, b = x+y, y+x
            if a > b:
                return 1  # x 大于 y
            elif a < b:
                return -1  # x 小于 y
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(compare))

        return ''.join(nums)
    
    def minNumber(self, nums: List[int]) -> str:
        """
            手动实现排序，快排
        """
        def partition(nums, left, right):
            pivot = left

            while left < right:
                # 下面的边界判断都要取等于
                while left < right and nums[right]+nums[pivot] >= nums[pivot]+nums[right]:
                    right -= 1  # 从右向左找第一个小
                
                while left < right and nums[left] + nums[pivot] <= nums[pivot]+nums[left]:
                    left += 1  # 从左向右找第一个大
                
                nums[left], nums[right] = nums[right], nums[left]

            nums[pivot], nums[left] = nums[left], nums[pivot]

            return left


        def quickSort(arr, left=None, right=None):
            left = 0 if not isinstance(left, int) else left
            right = len(arr)-1 if not isinstance(right, int) else right
    
            if left < right:
                partitionIndex = partition(arr, left, right)
                quickSort(arr, left, partitionIndex-1)
                quickSort(arr, partitionIndex+1, right)
            return arr
        
        nums = [str(num) for num in nums]
        nums = quickSort(nums)
        return "".join(nums)

            

