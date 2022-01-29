"""
    题目描述:
        假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
        对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
        并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，
        我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
        你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

    提示:
        1 <= g.length <= 3 * 104
        0 <= s.length <= 3 * 104
        1 <= g[i], s[j] <= 231 - 1

    链接: https://leetcode-cn.com/problems/assign-cookies
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
            采用贪心的思想，每个孩子只给恰大于他的饼干，如果没有则不给；

            对胃口值和饼干尺寸分别排序，再加一个标记数组
        """
        g.sort()
        s.sort()

        count = 0
        used = [False] * len(s)

        for val_g in g:
            for i, val_s in enumerate(s):
                if used[i] == False and val_g <= val_s:
                    used[i] = True
                    count += 1
                    break
        
        return count
    
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
            简化上个版本的代码；
            从后向前遍历胃口数组；
            为了避免 used 数组，用一个 index 记录饼干数组的位置即可 

            O(nlgn)、O(1)
        """
        g.sort()
        s.sort()

        s_index, count = len(s)-1, 0

        for g_index in range(len(g)-1, -1, -1):
            if s_index >= 0 and s[s_index] >= g[g_index]:
                count += 1
                s_index -= 1
        
        return count