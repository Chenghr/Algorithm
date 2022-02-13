"""
    题目描述:
        字符串 S 由小写字母组成。
        我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
        返回一个表示每个字符串片段的长度的列表。
    
    链接: https://leetcode-cn.com/problems/partition-labels/
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            贪心:
                1. 遍历一轮，确定出现的每个字母的起始下标；
                2. 按照起始下标排序；
                3. 得到最大不重叠子区间，个数即为片段长度；
        """
        location = []
        begin, end = [-1] * 26, [-1] * 26

        for i, char in enumerate(s):
            index = ord(char)-ord('a')
            if begin[index] == -1:
                begin[index] = i
                end[index] = i  # 防止字母只出现过一次
            else:
                end[index] = i
        
        for b, e in zip(begin, end):
            if b != -1:
                location.append((b, e))
        
        location.sort()

        result, begin_idx, max_length = [], 0, location[0][1]

        for point in location:
            if point[0] <= max_length:
                # 防止只出现一个字母的片段
                max_length = max(max_length, point[1])
            else:
                result.append(point[0] - begin_idx)
                begin_idx = point[0]
                max_length = point[1]

        result.append(len(s) - begin_idx)

        return result

example = Solution()
result = example.partitionLabels("ababcbacadefegdehijhklij")
print(result)