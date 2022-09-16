"""
    给定一个数字，我们按照如下规则把它翻译为字符串:
        0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    
    一个数字可能有多个翻译。
    请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

class Solution:
    def translateNum(self, num: int) -> int:
        """
            可通过 求余 和 求整 运算实现 从右向左 的遍历计算。
            而根据上述动态规划 “对称性” ，可知从右向左的计算是正确的。
            再加上 循环数组的使用，进一步节约空间复杂度。
        """
        a, b = 1, 1
        y = num % 10

        while num != 0:
            num //= 10
            x = num % 10

            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a

            a, b = c, a
            y = x
            
        return a


    def translateNum(self, num: int) -> int:
        num = str(num)

        dp = [1] * len(num)

        for i in range(1, len(num)):
            dp[i] = dp[i-1]

            if 9 < int(num[i-1]+num[i]) < 26:
                if i >= 2:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
        
        return dp[-1]
    