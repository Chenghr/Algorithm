"""
    题目描述:
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

        注意: 若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

    提示:
        1 <= s.length, t.length <= 5 * 104
        s 和 t 仅包含小写字母

    链接: https://leetcode-cn.com/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            由于仅包含小写字母，因此可以使用 26 维的数组当做字典；

            注意 python 中字符和 ASCII 码之间的相互转换。

            char -> ASCII: ord(ch)
            ASCII -> char: chr(num)
        """
        dic_ch = [0] * 26

        for ch in s:
            dic_ch[ord(ch)-ord('a')] += 1
        
        for ch in t:
            dic_ch[ord(ch)-ord('a')] -= 1
        
        for num in dic_ch:
            if num != 0:
                return False
        
        return True
