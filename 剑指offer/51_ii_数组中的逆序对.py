"""
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组，求出这个数组中的逆序对的总数。
"""

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
            暴力求解:
                O(n^2)，确定每个数右边比它小的数的个数；

            归并排序的思想:
                归并排序体现了 “分而治之” 的算法思想，合并阶段 本质上是 合并两个排序数组 的过程，
                而每当遇到 左子数组当前元素 > 右子数组当前元素 时，
                意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。
        """
        tmp = [0] * len(nums)  # 存储排序后的数组

        def mergeSort(left, right) -> int:
            """归并排序，返回逆序对个数
            """
            if left >= right:
                return 0  # 递归终点, 返回逆序对数目
            
            # 递归划分
            mid = (left + right) // 2
            res = mergeSort(left, mid) + mergeSort(mid+1, right)

            # 合并
            i, j = left, mid+1
            tmp[left: right+1] = nums[left: right+1]

            for k in range(left, right+1):
                if i == mid+1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == right+1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] > tmp[j]:  # 出现逆序对
                    nums[k] = tmp[j]
                    j += 1
                    res += mid- i + 1  # j 比 i ~ mid 之间的元素都小，均为逆序对

            return res
        
        return mergeSort(0, len(nums)-1)
