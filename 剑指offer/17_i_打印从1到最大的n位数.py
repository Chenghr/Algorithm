"""
    输入数字 n;
    按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
"""

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        """
            本题的本质是大数的输出处理，采用字符串输出的形式，即全排列。
            注意前导0的处理；这里的思路为:
                辅助函数 dfs(x, len) : 生成长度为len的数字，正在确定第 x 位。
        """
        ans, path = [], []

        def dfs(k, length):
            """搜索第k位数的取值"""
            nonlocal ans, path

            if k == length:
                ans.append(int(''.join(path)))
                return

            start = 0 if k > 0 else 1

            for i in range(start, 10):
                path.append(str(i))
                dfs(k+1, length)
                path.pop()
        
        for i in range(1, n+1):
            dfs(0, i)
        
        return ans

    def printNumbers(self, n: int) -> List[int]:
        ans = []

        for i in range(1, 10 ** n):
            ans.append(i)
        
        return ans