"""
    题目描述:
        给你一个字符串 s 、一个字符串 t 。
        返回 s 中涵盖 t 所有字符的最小子串。
        如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

    注意:
        对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
        如果 s 中存在这样的子串，我们保证它是唯一的答案。

    链接: https://leetcode-cn.com/problems/minimum-window-substring/
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            在 s 中寻找连续子串，考虑使用滑动窗口；
            难点在于:
                1. 窗口的移动规则；
                2. 窗口符合条件的判断（涵盖 t 中所有字符的判断）
        """
        t_dic = defaultdict(int)

        for char in t:
            t_dic[char] += 1

        def check(t_dic: defaultdict) -> bool:
            """字典中每一项的值均为非正
            """
            for value in t_dic.values():
                if value > 0:
                    return False
            
            return True
        
        left, subStr = 0, ""

        for right in range(len(s)):

            if s[right] in t_dic:
                t_dic[s[right]] -= 1
            
            while check(t_dic) and left <= right:
                # 单纯的求和会出现抵消的情况，实际要求的是每一项都非正
                if subStr == "" or len(subStr) > (right - left + 1):
                    subStr = s[left: right+1]
                
                if s[left] in t_dic:
                    t_dic[s[left]] += 1
                
                left += 1
        
        return subStr

    def minWindow(self, s: str, t: str) -> str:
        """
            上个解法中判断是否合法的时间开销过大，迭代一下解法。
            在收缩双指针的同时，完成窗口内字符串是否有效的判断，时间复杂度降到O(n)
        """
        t_dic = defaultdict(int)  # 记录窗口内需要的字符数

        for char in t:
            t_dic[char] += 1

        left, subStr = 0, ""
        valid = 0  # 记录 t 中满足条件的字符数
        for right in range(len(s)):

            if s[right] in t_dic:
                t_dic[s[right]] -= 1

                if t_dic[s[right]] == 0:
                    # 出现一个满足条件的字符
                    valid += 1
            
            while valid == len(t_dic):
                # 收缩左侧窗口
                if subStr == "" or len(subStr) > (right - left + 1):
                    subStr = s[left: right+1]
                
                if s[left] in t_dic:
                    t_dic[s[left]] += 1

                    if t_dic[s[left]] > 0:
                        valid -= 1

            left += 1

        return subStr

example = Solution()
result = example.minWindow("bba", "ab")
print(result)
                