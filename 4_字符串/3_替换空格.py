"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

限制：
    0 <= s 的长度 <= 10000

https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
"""

"""
思路分析:
    python 中 str 类型不可修改，因此考虑将 str 先转成 list 类型；
    然后对 list 中的空格进行替换；
    再使用 str 的 join() 方法即可。

进阶:
    不使用额外的辅助空间；
    - 首先扩充数组到每个空格替换后的大小；
    - 再从后向前替换空格，即使用双指针法。

    这里从后向前替换是避免时间复杂过高，从前往后替换是 O(n^2) 的算法。
"""

from typing import Counter


class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)

        for index, ch in enumerate(s):
            if ch == ' ':
                s[index] = '%20'
            
        return "".join(s)
    
    def replaceSpace(self, s: str) -> str:
        countNum = s.count(' ')
        
        # 拓展空间
        res = list(s)
        res.extend([' '] * countNum * 2)

        # 左右指针分别指向原始字符串的末尾，拓展后的字符串的末尾
        left, right = len(s)-1, len(res)-1

        while left >= 0:
            if res[left] != ' ':
                # 非空格项，直接向后平移即可
                res[right] = res[left]
                right -= 1
            else:
                # 空格项，替换
                # 切片为左闭右开
                res[right-2: right+1] = '%20'
                right -= 3
                
            left -= 1

        return "".join(res)
