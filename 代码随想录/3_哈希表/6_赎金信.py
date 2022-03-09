"""
    题目描述:
        给你两个字符串: ransomNote 和 magazine ，
        判断 ransomNote 能不能由 magazine 里面的字符构成。

        如果可以，返回 true ；否则返回 false 。
        magazine 中的每个字符只能在 ransomNote 中使用一次。

    链接: https://leetcode-cn.com/problems/ransom-note/
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26

        for ch in ransomNote:
            record[ord(ch) - ord('a')] += 1
        
        for ch in magazine:
            record[ord(ch) - ord('a')] -= 1

            if record[ord(ch) - ord('a')] < 0:
                return False

        return True

solution = Solution()
print(solution.canConstruct("aa","aab"))