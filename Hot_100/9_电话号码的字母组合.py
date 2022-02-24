"""
    题目描述:
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    链接: https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
            回溯 + map :
            将 2~9 map 到对应的字母；
            由于要返回组合，每个数字有多重选择，考虑使用回溯，记录 path.
        """
        dic = [
            [], [],
            ['a','b','c'], ['d','e','f'],
            ['g','h','i'], ['j','k','l'],['m','n','o'],
            ['p','q','r','s'],['t','u','v'],['w','x','y','z']
        ]

        result, path = [], []

        def backtracking(idx: int):
            nonlocal result, path

            if idx == len(digits):
                result.append("".join(path))
                return  # 否则还会继续往下执行
            
            for char in dic[int(digits[idx])]:
                path.append(char)

                backtracking(idx + 1)

                path.pop()  # 回溯

        if len(digits) == 0:
            # 注意特殊情况的处理
            return []

        backtracking(0)

        return result