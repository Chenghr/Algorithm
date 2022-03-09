"""
    题目描述:
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    
    注意:
        0 <= digits.length <= 4
        digits[i] 是范围 ['2', '9'] 的一个数字。

    链接: https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            注意返回空列表和列表中包含空字符串代表的区别。
        """
        dic = [
            [], [],
            ['a','b','c'], ['d','e','f'],
            ['g','h','i'], ['j','k','l'],['m','n','o'],
            ['p','q','r','s'],['t','u','v'],['w','x','y','z']
        ]

        result, path = [], []

        def _backtracking(begin_idx):
            nonlocal digits, result, path, dic

            if len(path) == len(digits):
                result.append(''.join(path))
                return
            
            idx = int(digits[begin_idx])

            for char in dic[idx]:

                path.append(char)
                _backtracking(begin_idx+1)
                path.pop()
        
        if len(digits) == 0:
            return []

        _backtracking(0)

        return result
