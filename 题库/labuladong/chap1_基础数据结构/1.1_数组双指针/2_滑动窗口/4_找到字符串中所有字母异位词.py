"""
    题目描述:
        给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，
        返回这些子串的起始索引。不考虑答案输出的顺序。

        异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

    链接: https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
"""

from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            滑动窗口，记录每次窗口满足条件时的左指针下标即可。
            另外这里注意是子串，不是子序列。
        """
        p_dic = defaultdict(int)

        for char in p:
            p_dic[char] += 1

        left, windows, valid = -1, defaultdict(int), 0
        result = []

        for right in range(len(s)):
            if s[right] in p_dic:

                if left == -1:
                    # 找到一个异位词起点
                    left = right

                windows[s[right]] += 1

                if windows[s[right]] == p_dic[s[right]]:
                    valid += 1
                elif windows[s[right]] > p_dic[s[right]]:
                    # 移动左指针直到满足条件
                    while windows[s[right]] > p_dic[s[right]]:
                        # 先判断
                        if windows[s[left]] == p_dic[s[left]]:
                            valid -= 1

                        windows[s[left]] -= 1
                        left += 1

                if valid == len(p_dic):
                    # 移动左边界
                    result.append(left)

                    windows[s[left]] -= 1
                    valid -= 1  # 此时不用判断，一定是有一个不能满足了

                    left += 1

            else:
                # 出现一个不在目标范围的字母，left 置为-1，表示需要重新寻找起点
                left = -1
                windows.clear()
                valid = 0

        return result

example = Solution()
result = example.findAnagrams("vwwvv","vwv")
print(result)

