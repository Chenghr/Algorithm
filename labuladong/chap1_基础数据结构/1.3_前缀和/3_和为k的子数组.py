"""
    题目描述:
        给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。
    
    链接: https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            构造 nums 的前缀和数组，然后遍历前缀和数组，寻找符合条件的差值；
            O(n*2)
        """
        # 构造前缀和
        preSum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]
        
        result = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)+1):
                if preSum[j] - preSum[i] == k:
                    result += 1
        
        return result

    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            前缀和 + 哈希数组 + 二分搜索， O(nlogn)
        """
        preSum = [0] * (len(nums)+1)
        dic = defaultdict(list)

        for i in range(len(nums)):
            preSum[i+1] = preSum[i] + nums[i]
            dic[preSum[i+1]].append(i+1)  # 存储相关下标
        
        result = 0
        for i in range(0, len(nums)):
            key = k + preSum[i]

            if key in dic:
                # 寻找 i 的右边界
                left, right = 0, len(dic[key])

                while left < right:
                    mid = (left + right) // 2

                    if dic[key][mid] == i:
                        left = mid + 1
                    elif dic[key][mid] < i:
                        left = mid + 1
                    elif dic[key][mid] > i:
                        right = mid
                
                result += len(dic[key]) - left
        
        return result
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            前缀和 + 哈希数组 : O(n);
            前缀和数组也可以压缩
        """
        dic = defaultdict(int)  # 只记录出现次数
        dic[0] = 1
        result = 0

        preSum = 0
        for num in nums:
            preSum += num

            if preSum - k in dic:
                result += dic[preSum - k]
            
            dic[preSum] += 1
        
        return result

solution = Solution()
result = solution.subarraySum([1,1,1], 2)
print(result)