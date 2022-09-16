"""
    输入一个字符串，打印出该字符串中字符的所有排列。
"""

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(used):
            nonlocal ans, path, s

            if len(path) == len(s):
                ans.append("".join(path))
                return
            
            for i, ch in enumerate(s):
                if used[i]:
                    continue

                if i > 0 and s[i-1] == ch and used[i-1] == False:
                    continue

                used[i] = True
                path.append(ch)

                dfs(used)

                path.pop()
                used[i] = False

        
        ans, path = [], []
        used = [False] * len(s)

        s = list(s)
        s.sort()

        dfs(used)

        return ans
