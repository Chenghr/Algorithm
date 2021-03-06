"""
    给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
    每段绳子的长度记为 k[0],k[1]...k[m-1] 。
    请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
    
    例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        """
            dp:
            1. dp[i]: 长为 i 的绳子，至少分为 m（m > 1）的最大长度；
            2. 递推:
                很自然的想到将绳子一分为二，但是注意，子绳子有两种选择，切分或者不切分，要分开考虑；
                不分开考虑时长度即为 i*(j-i)，继续切分的话为 dp[i]*(j-i)，取其中最大值。
        """
        dp = [i-1 for i in range(n+1)]

        for j in range(3, n+1):
            for i in range(2, j):
                dp[j] = max(dp[j], i*(j-i), dp[i]*(j-i))
        
        return dp[n]
    
    def cuttingRope(self, n: int) -> int:
        """
            数学推导；
             1. 将绳子 以相等的长度等分为多段 ，得到的乘积最大。
             2. 尽可能将绳子以长度 3 等分为多段时，乘积最大。
            
            切分规则：
                最优： 3， 把绳子尽可能切为多个长度为 3 的片段，留下的最后一段绳子的长度可能为 0,1,2 三种情况。
                次优： 2 。若最后一段绳子长度为 2 ；则保留，不再拆为 1+1 。
                最差： 1 。若最后一段绳子长度为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2*2 > 3*1
        """
        if n < 4:
            return n-1
        
        num3 = n // 3

        if n % 3 == 1:
            return 3 ** (num3-1) * 2 * 2
        elif n % 3 == 2:
            return 3 ** (num3) * 2
        else:
            return 3 ** (num3)