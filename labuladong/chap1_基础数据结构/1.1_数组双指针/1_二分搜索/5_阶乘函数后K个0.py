"""
    题目描述:
        f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。

        例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；
        而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
        
        给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。
    
    提示: 0 <= k <= 109

    链接: https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
"""

import sys

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """n! 后 0 的数量可以转化为 n! 最多可以分解出多少个因子 5。
        """
        result = 0

        while n > 0:
            n = n // 5
            result += n
        
        return result

    def searchLeftBound(self, k: int) -> int:
        # 获取 int 最大值，和计算机的位数相关
        left, right = 0, sys.maxsize

        while left < right:
            mid = (left + right) // 2

            if self.trailingZeroes(mid) == k:
                right = mid
            elif self.trailingZeroes(mid) < k:
                left = mid + 1
            elif self.trailingZeroes(mid) > k:
                right = mid
        
        if left == sys.maxsize or self.trailingZeroes(left) != k:
            return -1
        
        return left
    
    def searchRightBound(self, k: int) -> int:
        # 获取 int 最大值，和计算机的位数相关
        left, right = 0, sys.maxsize

        while left < right:
            mid = (left + right) // 2

            if self.trailingZeroes(mid) == k:
                left = mid + 1
            elif self.trailingZeroes(mid) < k:
                left = mid + 1
            elif self.trailingZeroes(mid) > k:
                right = mid
        
        if left == 0 or self.trailingZeroes(left - 1) != k:
            return -1
        
        return left - 1

    def preimageSizeFZF(self, k: int) -> int:
        """
            搜索满足条件的 n 最小值，即求，满足条件的 n 最小值和最大值，相减即可。

            n 的取值范围为正整数，且递增，因此考虑使用二分搜索，最小值和最大值即二分搜索左右边界。
        """
        if self.searchLeftBound(k) == -1 and self.searchRightBound(k) == -1:
            return 0
        
        return self.searchRightBound(k) - self.searchLeftBound(k) + 1
        

