"""
    输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        """
            可以考虑枚举每一个数位，分别统计该数位上数字 1 出现的次数，最后将所有数位统计出的次数进行累加即可得到答案。

            当数位为 10^k 时，最后的 k 个数位每 10^{k+1} 个数会循环一次，并且其中包含 10^k 个 1;
            不在循环中的部分还有 n % (10^(k+1)) 个数，这一部分的 1 的个数为 n % (10^(k+1)) - 10^k + 1 ，如果这个值小于 0，那么调整为出现 0 次；
            如果这个值大于 10^k，那么调整为出现 10^k 次。

            复杂度分析
                时间复杂度: O(log n)。n 包含的数位个数与 n 呈对数关系。
                空间复杂度: O(1)。
        """
        ans = 0
        digit = 1

        while digit <= n:
            # digit 位为 1 的总次数
            ans += (n//(10 * digit)) * digit + min(digit, max(0, (n%(10*digit)) - digit + 1))
            digit *= 10
        
        return ans

    def countDigitOne(self, n: int) -> int:
        """这里考虑思路和上面一致，但是分类更细致，更加精细化了，有点没必要
        """
        ans = 0
        high, cur, low = n // 10, n % 10, 0
        digit = 1

        while high != 0 or cur != 0:
            if cur == 0:
                # 位 1 的出现次数只由高位 high 决定
                ans += high * digit
            elif cur == 1:
                # 位 1 的出现次数只由高位 high 和低位 low 决定
                ans += high * digit + low + 1
            else:
                # 位 1 的出现次数只由高位 high 决定，low 的作用在于帮 high 增加了 1
                ans += (high+1) * digit

            high = high // 10
            cur = high % 10
            low = low + cur * digit
            digit = digit * 10
           
        return ans