"""
    在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
"""

from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        """进阶实现: 有序哈希表

            有序哈希表中的键值对是 按照插入顺序排序 的。
            基于此，可通过遍历有序哈希表，实现搜索首个 “数量为 11 的字符”。

            Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()。
        """
        dic = OrderedDict()

        for c in s:
            dic[c] = not c in dic

        for k, v in dic.items():
            if v: return k
            
        return ' '

    def firstUniqChar(self, s: str) -> str:
        """哈希
        """
        if len(s) == 0:
            return ' '

        dic = [0] * 26

        for ch in s:
            dic[ord(ch) - ord('a')] += 1
        
        for ch in s:
            if dic[ord(ch) - ord('a')] == 1:
                return ch
        
        return ' '
        
