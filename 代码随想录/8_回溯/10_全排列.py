
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            题目描述:
                给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
            
            提示:
                1 <= nums.length <= 6
                -10 <= nums[i] <= 10
                nums 中的所有整数 互不相同

            链接: https://leetcode-cn.com/problems/permutations/

            思路:
                相较于组合问题，排序问题每次都是从头开始选取，需要用一个标记数组，标记元素是否被选取过；
                由于数组中不含重复数字，因此不涉及到排列去重问题，本题较为简单
        """
        result, path = [], []

        def _backtracking(nums, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for idx, num in enumerate(nums):
                if used[idx] == True:
                    continue
                    
                path.append(num)
                used[idx] = True

                _backtracking(nums, used)

                path.pop()
                used[idx] = False
        
        used = [False] * len(nums)
        _backtracking(nums, used)

        return result
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
            题目描述:
                给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
            
            提示:
                1 <= nums.length <= 8
                -10 <= nums[i] <= 10

            链接: https://leetcode-cn.com/problems/permutations-ii/

            思路:
                在上一题的基础上增加了去重的要求；
                分析回溯树可知: 本题去重是同层去重

                有两个思路:
                    1. 排序后去重，不需要额外标记数组
                    2. 不排序，引入 哈希 去重，同层不选用相同的元素
                此处我们采用排序的思想
        """
        result, path = [], []

        def _backtracking(nums, used):
            nonlocal result, path

            if len(path) == len(nums):
                result.append(path[:])
                return

            for idx, num in enumerate(nums):
                if used[idx] == True:
                    continue

                if idx > 0 and num == nums[idx-1] and used[idx-1] == False:
                    continue

                path.append(num)
                used[idx] = True

                _backtracking(nums, used)

                path.pop()
                used[idx] = False
        
        used = [False] * len(nums)
        nums.sort()

        _backtracking(nums, used)

        return result

example = Solution()

result = example.permuteUnique([1,1,2])

print(result)