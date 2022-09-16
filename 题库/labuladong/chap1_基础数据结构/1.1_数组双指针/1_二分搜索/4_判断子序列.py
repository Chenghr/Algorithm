"""
    给定字符串s和t，判断s是否为t的⼦序列。 

    进阶：
        如果有⼤量输⼊的 S，称作 S1,S2, ..., Sk, 其中 k > 10亿；依次检查是否为 t 的子序列。

    链接: https://leetcode-cn.com/problems/is-subsequence/
"""

from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
            二分搜索来判断子序列。
                对 t 进行预处理，用一个字典 index 将每个字符出现的索引位置按顺序存储下来
                （对于 ASCII 字符，可以用大小为 256 的数组充当字典）；

                借助index中记录的信息，可以二分搜索index[c]中比 j 大的那个索引;
            
            链接: https://mp.weixin.qq.com/s/hWi2hTrQewL_YKioGkXQJg
        """
        dic = defaultdict(list)

        # 预处理
        for i, char in enumerate(t):
            dic[char].append(i)
        
        s_index, t_index = 0, 0

        while s_index < len(s):
            if len(dic[s[s_index]]) == 0:
                # t 中不含有 s[s_index] 这个字符
                return False
            
            # 在 dic[s[s_index]] 寻找大于等于 t_index 的下标；
            # 采用二分查找，利用查找最左侧元素返回值的性质；当val不存在时，得到的索引恰好是比val大的最小元素索引。
            left, right = 0, len(dic[s[s_index]])

            while left < right:
                mid = int((left + right) / 2)

                if dic[s[s_index]][mid] == t_index:
                    right = mid
                elif dic[s[s_index]][mid] < t_index:
                    left = mid + 1
                elif dic[s[s_index]][mid] == t_index:
                    right = mid
            
            if left == len(dic[s[s_index]]):
                # 没有找到可用的下标
                return False
            
            # 这里是个小细节，要指向可用下标
            t_index = dic[s][s_index][left] + 1
        
        return True

            

