"""
    输入整数数组 arr ，找出其中最小的 k 个数。
    例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
"""

from typing import List
from queue import PriorityQueue

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """最小堆
        """
        minQueue = PriorityQueue()

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """快排的思想
            O(N)、O(logN)
        """
        def partition(arr, left, right):
            i, j = left, right

            while i < j:
                while i < j and arr[j] >= arr[left]:
                    j -= 1
                
                while i < j and arr[i] <= arr[left]:
                    i += 1
                
                arr[i], arr[j] = arr[j], arr[i]
            
            arr[left], arr[i] = arr[i], arr[left]

            return i
        
        if k < 0:
            return []
        if k > len(arr):
            return arr

        left, right = 0, len(arr)-1

        while left <= right:
            mid = partition(arr, left, right)

            if mid == k-1:
                return arr[: mid+1]
            elif mid > k-1:
                right = mid - 1
            else:
                left = mid + 1
        return []

a = Solution()
ans = a.getLeastNumbers([3,2,1], 2)
print(ans)