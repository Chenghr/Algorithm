"""
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

    数值（按顺序）可以分成以下几个部分：
        若干空格
        一个 小数 或者 整数
        （可选）一个 'e' 或 'E' ，后面跟着一个 整数
        若干空格

    小数（按顺序）可以分成以下几个部分：
        （可选）一个符号字符（'+' 或 '-'）
        下述格式之一：
            至少一位数字，后面跟着一个点 '.'
            至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
            一个点 '.' ，后面跟着至少一位数字

    整数（按顺序）可以分成以下几个部分：
        （可选）一个符号字符（'+' 或 '-'）
        至少一位数字

    部分数值列举如下：
        ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]

    部分非数值列举如下：
        ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        """有限状态自动机解法
            https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
        """

class Solution:
    def isFloat(self, s: str) -> bool:
        """判断是否为小数(或者整数)
        """
        if len(s) == 0 or '.' not in s:  # 这里可能出现非小数的情况
            return False

        start = 1 if s[0] in ['+', '-'] else 0
        mid = s.index('.')

        for i in range(start, mid):
            if not s[i].isdigit():
                return False
        
        for i in range(mid+1, len(s)):
            if not s[i].isdigit():
                return False
        
        if mid == start and mid == len(s)-1:
            return False  # 说明小数中没有数字
        
        return True


    def isInt(self, s: str) -> bool:
        """判断是否为整数
        """
        if len(s) == 0:
            return False

        start = 1 if s[0] in ['+', '-'] else 0

        i = start
        while i < len(s):
            if not s[i].isdigit():
                return False

            i += 1
        
        return True if i > start else False  # 至少有一个数字  

    def isNumber(self, s: str) -> bool:
        """
            从外到内逐步拆分；
            数值判断 -> 小数判断；整数判断
        """
        s = s.strip()  # 去除首尾空格

        if 'e' in s or 'E' in s:  # 数值拆分的情况
            if s.count('e') + s.count('E') > 1:
                return False
            
            index = s.index('e') if 'e' in s else s.index('E')

            if self.isInt(s[index+1:]):
                return self.isFloat(s[:index]) or self.isInt(s[:index])
            
            return False
        
        # 数值不拆分的情况
        return self.isFloat(s) if '.' in s else self.isInt(s)
        

a = Solution()

ans = a.isNumber("te1")
print(ans)