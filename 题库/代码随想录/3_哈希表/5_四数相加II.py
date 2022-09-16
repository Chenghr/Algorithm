"""
    题目描述:
        给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ;
        请你计算有多少个元组 (i, j, k, l) 能满足:
            0 <= i, j, k, l < n
            nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

    链接: https://leetcode-cn.com/problems/4sum-ii/
"""

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        record = dict()

        # 记录，O(n^2)
        for val1 in nums3:
            for val2 in nums4:
                if val1+val2 not in record:
                    record[val1+val2] = 1
                else:
                    record[val1+val2] += 1
        
        count = 0
        for val1 in nums1:
            for val2 in nums2:
                if -(val1+val2) in record:
                    count += record[-(val1+val2)]

        return count