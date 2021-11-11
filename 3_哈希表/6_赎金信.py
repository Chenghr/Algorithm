"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

提示：
    你可以假设两个字符串均只含有小写字母。

https://leetcode-cn.com/problems/ransom-note/
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26

        for ch in ransomNote:
            record[ord(ch) - ord('a')] += 1
        
        for ch in magazine:
            tag = ord(ch) - ord('a')

            if record[tag] > 0:
                record[tag] -= 1
        
        for num in record:
            if num != 0:
                return False
        return True

solution = Solution()
print(solution.canConstruct("aa","aab"))