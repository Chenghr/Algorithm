"""题目描述:

    实现 strStr() 函数。
    给你两个字符串 haystack 和 needle ，
    请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
    如果不存在，则返回  -1 。

    说明：
        当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
        对于本题而言，当 needle 是空字符串时我们应当返回 0 。
        这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

    提示：
        0 <= haystack.length, needle.length <= 5 * 104
        haystack 和 needle 仅由小写英文字符组成

    https://leetcode-cn.com/problems/implement-strstr/
"""

"""思路分析:
    本题本质上是个字符串匹配问题，有两种实现思路:

    1. 暴力匹配，O(M * N) 时间开销；

    2. KMP算法，O(N) 时间开销；
        https://blog.csdn.net/v_JULY_v/article/details/7041827
"""

class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     # 暴力求解
    #     if len(needle) == 0:
    #         return 0
    #     if len(haystack) < len(needle):
    #         return -1
        
    #     for i in range(0, len(haystack)-len(needle)+1):
    #         # 找起始下标

    #         j = 0
    #         while j < len(needle):
    #             # 注意这里不能用 for 循环，for循环采用的是迭代器，无法在外围判断
    #             if needle[j] != haystack[i+j]:
    #                 break
    #             j += 1

    #         if j == len(needle):
    #             return i

    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # KMP算法
        
        def getNext(pattern: str) -> list:
            """求解 next 数组

            next: 代表当前字符之前的字符串中，有多大长度的相同前缀后缀。
                  例如如果next [j] = k，代表 j 之前的字符串中有最大长度为 k 的相同前缀后缀

            在某个字符失配时，该字符对应的 next 值会告诉你下一步匹配中，模式串应该跳到哪个位置（跳到 next[j] 的位置）。
            如果 next[j] 等于0或-1，则跳到模式串的开头字符，
            若 next[j] = k 且 k > 0，代表下次匹配跳到j 之前的某个字符，而不是跳到开头，且具体跳过了 k 个字符

            next 数组的求解：就是找最大对称长度的前缀后缀，然后整体右移一位，初值赋为-1
            """
            next = [0] * len(pattern)
            next[0] = -1
            j, k = 0, -1

            while (j < len(pattern)-1):
                if k == -1 or pattern[j] == pattern[k]:
                    k += 1
                    j += 1
                    next[j] = k
                else:
                    # 第j个字符和第k个字符不匹配时，
                    k = next[k]
            
            return next

        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
            
        next = getNext(needle)

        i, j = 0, 0

        while (i < len(haystack) and j < len(needle)):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        
        if j == len(needle):
            return i-j
        
        return -1

            
            
