"""
    题目描述:
        给你一个字符串数组，请你将 字母异位词 组合在一起。
        可以按任意顺序返回结果列表。

        字母异位词 是由重新排列源单词的字母得到的一个新单词，
        所有源单词中的字母通常恰好只用一次。

    链接: https://leetcode-cn.com/problems/group-anagrams
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            哈希；
            重点在于如何判断字母异位词是否出现过
                1. 利用长为26的数组标记每个字符出现的次数，然后将数组作为哈希表的键值；
                2. 将每个字符串排序，排序后的字符串作为哈希表的键
            
            注意字典的键不能是数组，要转换为元组。
        """
        ans = []
        dic = defaultdict(int)

        for str in strs:
            tagNum = [0] * 26

            for char in str:
                tagNum[ord(char)-ord('a')] += 1
            
            if tuple(tagNum) not in dic:
                ans.append([str])
                dic[tuple(tagNum)] = len(ans)-1
            else:
                ans[dic[tuple(tagNum)]].append(str)
        
        return ans

        