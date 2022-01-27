"""
    题目描述:
        给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

        回文串 是正着读和反着读都一样的字符串。
    
    提示:
        1 <= s.length <= 16
        s 仅由小写英文字母组成

    链接: https://leetcode-cn.com/problems/palindrome-partitioning/
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
            分成两个部分:
                1. 判断回文字符串
                2. 遍历所有可能的情况
                    回溯 + 剪枝
        """
        def isOK(s: str) -> bool:
            """判断字符串是否为回文字符串"""
            left, right = 0, len(s)-1

            while (left <= right):
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

        result, path = [], []
        def _backtracing(s: str, begin_idx: int):
            nonlocal result, path

            if begin_idx >= len(s):
                result.append(path.copy())
                return
            
            for end_idx in range(begin_idx+1, len(s)+1):
                # 剪枝
                if isOK(s[begin_idx: end_idx]):  
                    # 只有满足回文字符串的要求才行  
                    path.append(s[begin_idx: end_idx])
                    _backtracing(s, end_idx)
                    path.pop()

        _backtracing(s, 0)
        return result

example = Solution()

result = example.partition('a')

for a in result:
    print(a)