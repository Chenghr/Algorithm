"""
    写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

    当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
    假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

    该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，
         则你的函数不需要进行转换。

    在任何情况下，若函数不能进行有效的转换时，请返回 0。

    说明：
        假设我们的环境只能存储 32 位大小的有符号整数，如果数值超过这个范围，请返回  INT_MAX 或 INT_MIN。
"""

class Solution:
    def strToInt(self, str: str) -> int:
        """
            重点在于数字边界的越界处理；

            由于题目指出 环境只能存储 32 位大小的有符号整数 ，因此判断数字越界时，要始终保持 res 在 int 类型的取值范围内。
            
            在每轮数字拼接前，判断 res 在此轮拼接后是否超过 2147483647（1<<31 - 1） ，若超过则加上符号位直接返回。
            
            设数字拼接边界 bndry = 2147483647 // 10 = 214748364，则以下两种情况越界: 
                情况一: res > bndry, 执行拼接 10×res ≥ 2147483650 越界
                情况二: res = bndry, x > 7, 执行拼接 10×res + x =  2147483648 或者 2147483649 越界

            本题也可以不使用 strip 方法，将空间复杂度降低到 O(1).
        """
        s = str.strip()  # 去除前后空格

        if not s:
            return 0

        INT_MAX, INT_MIN, bndry = (1<<31) - 1, -(1<<31), (1<<31) // 10

        start = 1 if s[0] in '+-' else 0

        num = 0
        for i in range(start, len(s)):
            x = ord(s[i]) - ord('0')

            if not 0 <= x <= 9:
                break  # 非数字字符
                
            if num > bndry or (num == bndry and x > 7):  # 数字越界
                return INT_MIN if s[0] == '-' else INT_MAX

            num = num * 10 + x
        
        return -num if s[0] == '-' else num

    def strToInt(self, str: str) -> int:
        """个人解法
        """
        s = str.strip()  # 去除前后空格

        if len(s) == 0:
            return 0
        
        start = 1 if s[0] in '+-' else 0

        num = 0
        for i in range(start, len(s)):
            if 0 <= ord(s[i]) - ord('0') <= 9:
                num = num * 10 + ord(s[i]) - ord('0') 
            else:
                break
        
        INT_MAX, INT_MIN = (1 << 31) - 1, -(1 << 31)
        if s[0] == '-':
            num = max(INT_MIN, -num)
        else:
            num = min(INT_MAX, num)
        
        return num
        
