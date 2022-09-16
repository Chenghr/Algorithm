"""
    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口 + 哈希
            注意本题是找最长子字符串，所以应该是左指针向右走，右指针每轮向右探索最长边界
        """
        dic = set()
        right, maxLength = -1, 0

        for left in range(len(s)):
            if left != 0:
                dic.remove(s[left-1])
            
            while right + 1 < len(s) and s[right+1] not in dic:
                dic.add(s[right+1])
                right += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口 + 哈希(习惯写法)
        """
        dic = set()
        left, maxLength= 0, 0

        for right in range(len(s)):
            if s[right] not in dic:
                dic.add(s[right])
            else:
                maxLength = max(maxLength, right - left)

                while left < right and s[left] != s[right]:
                    dic.remove(s[left])
                    left += 1

                