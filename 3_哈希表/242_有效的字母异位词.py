"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

提示:
    1 <= s.length, t.length <= 5 * 104
    s 和 t 仅包含小写字母

https://leetcode-cn.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_ch = [0] * 26

        for ch in s:
            dic_ch[ord(ch)-ord('a')] += 1
        
        for ch in t:
            dic_ch[ord(ch)-ord('a')] -= 1
        
        for num in dic_ch:
            if num != 0:
                return False
        
        return True

# 相关知识：
"""python 中遍历字符串的方式

1）直接进行遍历
2) 利用下标 / enumerate 遍历
3) 利用 range 进行遍历
4) 利用迭代器

https://blog.csdn.net/zy345293721/article/details/89893279
"""

"""python 字符串和 ASCII 码的相互转换

单个字符：
    char -> ASCII: ord(ch)
    ASCII -> char: chr(num)
"""