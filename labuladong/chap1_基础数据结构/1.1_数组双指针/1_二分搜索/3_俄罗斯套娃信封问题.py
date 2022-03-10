"""
    题目描述:
        给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

        当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

        请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

        注意：不允许旋转信封。

    链接: https://leetcode-cn.com/problems/russian-doll-envelopes
"""

from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
           动态规划:
                先对二维数组按照宽度进行升序排序，然后再高度中寻找最长升序子数组长度即可。
                注意此处升序为严格升序，即宽度和高度均要大于才行，等于不可以。
            
            1. dp[i]:
                以下标 i 信封结尾的最大升序子数组长度。
            2. 递推公式:
                dp[i] = max(dp[i], dp[j]+1), 
                    j in [1, i-1] and envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1] 
            3. 初始化:
                dp[i] = 1
            4. 递推公式:
                从前向后        
            
            O(n*2), 超时了。。。
        """ 
        envelopes.sort()

        dp = [1] * len(envelopes)

        maxLength = 1
        for i in range(1, len(envelopes)):

            for j in range(0, i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            
            maxLength = max(maxLength, dp[i])

        return maxLength
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
           方法一的进一步优化:
            1. 先对 envelopes 排序，对宽度升序排序，高度降序排序；
                这样问题会完全转化为 高度的最长上升子序列问题（排除了宽度相同，高度大于前者的情况）；
            
            2. 由于信封量过大，因此要用 LIS 求解的 贪心+二分思想求解。
                dp[i]: 表示长度为 i 的最长上升子序列的末尾元素的最小值；
                且 dp[i] 内的元素均为 尽可能的小的数。
        """ 
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []

        for i in range(len(envelopes)):
            
            target = envelopes[i][1]

            if len(dp) == 0 or dp[-1] < target:
                dp.append(target)

            else:
                # 二分法寻找 dp 中 target 的左边界
                left, right = 0, len(dp)

                while left < right:
                    mid = int((left + right) / 2)

                    if dp[mid] == target:
                        right = mid
                    elif dp[mid] < target:
                        left = mid + 1
                    elif dp[mid] > target:
                        right = mid

                # 如果 dp 中不含有 target，那么最终 left 指向第一个大于 target 的值
                dp[left] = target
        
        return len(dp)
                


    
solution = Solution()
result = solution.maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
print(result)