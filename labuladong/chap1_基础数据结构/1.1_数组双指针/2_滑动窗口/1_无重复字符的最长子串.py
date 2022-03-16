"""
    题目描述:
        给定⼀个字符串 s ，请你找出其中不含有重复字符的最⻓⼦串的⻓度。

    链接: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """经典的滑动窗口题目
        """

        left, windows = 0, defaultdict(int)
        maxLength = 0

        for right in range(len(s)):
            windows[s[right]] += 1
            
            while windows[s[right]] > 1:
                # 收缩左侧边界
                windows[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            
        return maxLength