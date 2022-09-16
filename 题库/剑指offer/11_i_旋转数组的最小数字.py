"""
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

    给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，
    并按上述情形进行了一次旋转。请返回旋转数组的最小元素。
    
    例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  

    注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为
    数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
"""

from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
            进行部分有序区间的筛选，采用二分加速查找

            mid 可以和 left 比较或者 right 比较；由于 将部分有序区间搬到数组的末尾，
            因此可以通过和 right 比较来进行区间的取舍；
        """
        left, right = 0, len(numbers)-1

        while left < right:
            mid = (left + right) // 2

            if numbers[mid] > numbers[right]:
                left = mid + 1  # min 在右半区间
            elif numbers[mid] < numbers[right]:
                right = mid  # mid 在左半区间，且 mid 可能为最终的最小值
            elif numbers[mid] == numbers[right]:
                right -= 1  # 删除一个
        
        return numbers[left]