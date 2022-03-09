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
    
solution = Solution()
result = solution.maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])
print(result)