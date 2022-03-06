"""
    题目描述:
        实现 strStr() 函数。
        给你两个字符串 haystack 和 needle ，
        请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
        如果不存在，则返回  -1 。

        说明: 
            当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
            对于本题而言，当 needle 是空字符串时我们应当返回 0 。
            这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

        提示: 
            0 <= haystack.length, needle.length <= 5 * 104
            haystack 和 needle 仅由小写英文字符组成

    链接: https://leetcode-cn.com/problems/implement-strstr/
"""

"""
    思路分析:
        本题本质上是个字符串匹配问题，有两种实现思路:

    1. 暴力匹配，O(M * N) 时间开销；

    2. KMP算法，O(N) 时间开销；
        https://programmercarl.com/0028.实现strStr.html
        https://blog.csdn.net/v_JULY_v/article/details/7041827
"""

from typing_extensions import ParamSpecArgs


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
        
        def getNextV1(pattern: str) -> list:
            """求解 next 数组

            前缀表，代表当前字符之前的字符串中，最长相同前后缀。
            next 数组等于前缀表
            """
            next = [0] * len(pattern)

            # 初始化，j 指向前缀末尾位置
            next[0] = 0  
            j = 0

            # i 指向后缀末尾位置，不回退，注意下标从 1 开始
            for i in range(1, len(pattern)):

                # 处理前后缀不相同的情况
                while (j > 0 and pattern[i] != pattern[j]):
                    # j 保证大于0，避免下标越界
                    j = next[j-1]  # 向前回退，找前一位的对应的回退位置
                
                if pattern[i] == pattern[j]:
                    # 找到相同的前后缀
                    j += 1

                # 将 j（前缀的长度）赋给next[i]
                next[i] = j
            
            return next
        
        def kmpSearchV1(text: str, pattern: str) -> int:
            if len(pattern) == 0:
                return 0
            
            # next数组即为前缀表
            next = getNextV1(pattern)

            j = 0  # 指向模式串的指针

            for i in range(len(text)):

                # 当前字符不匹配，持续回退，要么找到一个匹配的，要么回到起点从头匹配
                while j > 0 and text[i] != pattern[j]:
                    j = next[j-1]

                # 当前字符匹配
                if text[i] == pattern[j]:
                    j += 1
                
                # 匹配成功
                if j == len(pattern):
                    return i-len(pattern)+1

            # 匹配失败
            return -1


        def getNext(pattern: str) -> list:
            """求解 next 数组

            next 数组的求解：求解出前缀表，然后整体右移一位，初始值补0，然后减1
            """
            next = [0] * len(pattern)

            # 初始化，j 指向前缀起始位置
            next[0] = -1  
            j = -1  

            # i 指向后缀起始位置，不回退，注意下标从 1 开始
            for i in range(1, len(pattern)):

                # 处理前后缀不相同的情况
                # 注意 next 数组为前缀表整体右移一位，因此为 pattern
                while (j >= 0 and pattern[i] != pattern[j+1]):
                    j = next[j]  # 向前回退，直到起点
                
                if pattern[i] == pattern[j+1]:
                    # 找到相同的前后缀
                    j += 1

                next[i] = j
            
            return next

        def kmpSearch(text: str, pattern: str) -> int:
            if len(pattern) == 0:
                return 0

            next = getNext(pattern)

            j = -1  # next数组里记录的起始位置为-1

            # 注意这里开始下标为0
            for i in range(len(text)):
                while j >=0 and text[i] != pattern[j+1]:
                    # 不匹配，j 向前回退
                    j = next[j] 
                
                if text[i] == pattern[j+1]:
                    # 当前字符匹配，i 和 j 同时向后移动，i 的移动在 for 循环内
                    j += 1
                
                if j == len(pattern)-1:
                    # 字符串匹配
                    return i-len(pattern)+1
                
            return -1

        index = kmpSearch(haystack, needle)   
        return index