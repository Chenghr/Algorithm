"""
    题目描述:
        传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。

        传送带上的第 i 个包裹的重量为 weights[i]。
        每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。
        我们装载的重量不会超过船的最大运载重量。

        返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。
    
    提示：
        1 <= days <= weights.length <= 5 * 104
        1 <= weights[i] <= 500

    链接: https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
"""

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
            货物必须按照指定顺序装载。单个包裹不可拆

            x: 船的运载量；f(x): 运输所需天数；target: days
            f(x): 单调递减

            最低运载能力 -> 左边界
            要注意二分查找的左右边界
        """
        def countDays(x: int):
            capacity, countDays = x, 1

            for weight in weights:
                if capacity >= weight:
                    capacity -= weight
                else:
                    # 新的一天，注意还是要把物品送出去
                    capacity = x - weight
                    countDays += 1
            
            return countDays
        
        left, right = max(weights), 10**8

        while left < right:

            mid = (left + right) // 2
            needDays = countDays(mid)

            if needDays == days:
                right = mid
            elif needDays < days:
                right = mid
            elif needDays > days:
                left = mid + 1
        
        # 本题必有解
        return left

solution = Solution()
result = solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
print(result)