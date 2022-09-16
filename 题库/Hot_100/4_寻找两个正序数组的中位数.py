"""
    题目描述:
        给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
        请你找出并返回这两个正序数组的 中位数 。

        算法的时间复杂度应该为 O(log (m+n)) 。

    链接: https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            中位数:
                n 个数中，第 n+1 / 2 个数或者 n / 2 个数；
            因此本题本质上为两个有序数组中寻找第 k 大的数；

            要达到 O(log (m+n)) 的时间复杂度，只能考虑使用二分查找。

            假设两个有序数组分别是 A 和 B。要找到第 k 个元素，我们可以比较 A[k/2 - 1] 和 B[k/2 - 1]
                - A[k/2 - 1] < B[k/2 - 1]:
                    此时比 A[k/2-1] 小的数最多只有 A 的前 k/2-1 个数和 B 的前 k/2-1 个数，
                    即比 A[k/2-1] 小的数最多只有 k-2 个，因此 A[k/2-1] 不可能是第 k 个数，
                    A[0] 到 A[k/2-1] 也都不可能是第 k 个数，可以全部排除。

                - A[k/2 - 1] > B[k/2 - 1]:
                    同理排除 B[0] 到 B[k/2-1]。
                
                - A[k/2 - 1] == B[k/2 - 1]:
                    可以归入情况一处理（舍去A的元素，B中仍在，不影响）。
            
            特殊情况处理:
                1. k=1:
                    返回两个数组首元素的最小值即可;
                2. 一个数组为空:
                    直接返回另一个数组中第 k 小的元素;
                3. A[k/2-1] 或者 B[k/2-1] 中有一个越界:
                    我们可以选取对应数组中的最后一个元素。
                    在这种情况下，我们必须根据排除数的个数减少 k 的值，而不能直接将 k 减去 k/2。

        """
        
        def getKthElement(k: int):
            """查找第 k 小的元素
            """
            nonlocal nums1, nums2

            index1, index2 = 0, 0

            while True:
                if index1 == len(nums1):
                    return nums2[index2 + k - 1]
                
                if index2 == len(nums2):
                    return nums1[index1 + k - 1]

                if k == 1:
                    # 正常出口
                    return min(nums1[index1], nums2[index2])
                
                # 防止越界
                newIndex1 = min((index1 + k) // 2 - 1, len(nums1)-1)
                newIndex2 = min((index2 + k) // 2 - 1, len(nums2)-1)

                if nums1[newIndex1] <= nums2[newIndex2]:
                    # 情况 1
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    # 情况 2
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 1:
            return getKthElement((total_length+1)/2)
        else:
            return getKthElement(total_length//2) + getKthElement(total_length//2 + 1)