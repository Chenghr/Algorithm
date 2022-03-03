"""
    题目描述:
        编写一个算法来判断一个数 n 是不是快乐数。

        「快乐数」定义为:
            对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
            然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
            如果 可以变为  1，那么这个数就是快乐数。
            如果 n 是快乐数就返回 true ；不是，则返回 false 。

    提示:
        1 <= n <= 231 - 1

    链接: https://leetcode-cn.com/problems/happy-number/
"""

class Solution:

    def isHappy(self, n: int) -> bool:
        """
            用字典存储中间数的出现，出现循环则查找终止。
        """

        from collections import defaultdict

        def calBitSum(n: int) -> int:
            # 将一个数字逐位拆开
            summ = 0
            n_str = str(n)

            for ch in n_str:
                summ += int(ch) ** 2

            return summ

        dic, num = defaultdict(int), n
        
        while True:
            num = calBitSum(num)

            if num == 1:
                return True

            if dic[num] == 1:
                return False
            else:
                dic[num] = 1

# Note:
# 这里主要是判断中间数是否出现过，可以采用set集合来存储，而非字典