"""
    题目描述:
        给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

    提示:
        0 <= s.length <= 5 * 104
        s 由英文字母、数字、符号和空格组成

    链接: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            朴素思路:
                双指针（动态窗口）+ map 
        """
        if len(s) <= 1:
            return len(s)

        dic = defaultdict(int)  # 存储字符出现的位置，从 1 开始计数

        left, right = 0, 1
        max_length = 0

        dic[s[left]] = left + 1
        
        while right <= len(s):
            # 加等于号是为了防止字符串本身没有重复字符

            if right == len(s):
                max_length = max(max_length, right - left)
                break

            if dic[s[right]] == 0:
                # 记录字符在本轮寻找中出现的第一个位置
                dic[s[right]] = right + 1

            else:
                # 出现重复字符
                max_length = max(max_length, right - left)

                # 移动 left
                while left < dic[s[right]]:
                    dic[s[left]] = 0
                    left += 1

                dic[s[right]] = right + 1
            
            right += 1

        return max_length        
