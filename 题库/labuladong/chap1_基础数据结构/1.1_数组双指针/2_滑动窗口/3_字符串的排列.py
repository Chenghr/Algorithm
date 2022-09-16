"""
    题目描述:
        给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。
        如果是，返回 true ；否则，返回 false 。

        换句话说，s1 的排列之一是 s2 的 子串 。

    链接: https://leetcode-cn.com/problems/permutation-in-string
"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            本题等价于: 
                ⼀个 S 和⼀个 T，请问你 S 中是否存在⼀个⼦串，包含 T 中所有字符且不包含其他字符？
            
            考虑使用滑动窗口解题；
            注意本题的左指针移动条件和之前不一样；窗口中的元素必须不能包含 s1 之外的字符。
        """
        s1_dic = defaultdict(int)

        for char in s1:
            s1_dic[char] += 1
        
        left, windows, valid = -1, defaultdict(int), 0

        for right in range(len(s2)):
            if s2[right] in s1_dic:

                # 判断是否有起点
                if left == -1:
                    left = right
                
                windows[s2[right]] += 1

                if windows[s2[right]] == s1_dic[s2[right]]:
                    valid += 1

                    if valid == len(s1_dic):
                        return True

                elif windows[s2[right]] > s1_dic[s2[right]]:
                    # 移动左指针直到二者相等

                    while windows[s2[right]] > s1_dic[s2[right]]:

                        if windows[s2[left]] == s1_dic[s2[left]]:
                            # 只有原来相等的，才会因为右移使得不满足条件，需要 valid 减1
                            valid -= 1

                        windows[s2[left]] -= 1
                        left += 1

                    #  注意此时 valid 不用再加1，因为之前相等时已经加1过了
            else:
                # 重新寻找
                left = -1
                windows.clear()
                valid = 0
        
        return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """题解中的写法
        """
        s1_dic = defaultdict(int)
        windows = defaultdict(int)

        for char in s1:
            s1_dic[char] += 1
        
        left, valid = 0, 0

        for right in range(len(s2)):
            if s2[right] in s1_dic:
                char = s2[right]

                windows[char] += 1

                if windows[char] == s1_dic[char]:
                    valid += 1

                # 窗口收缩的条件为左右指针间距大于目标匹配字符串长度
                # 这样可以有效避免无关字符的额外处理
                while right - left + 1 >= len(s1):
                    if valid == len(s1_dic):
                        return True
                    
                    if s2[left] in s1_dic:
                        if windows[s2[left]] == s1_dic[s2[left]]:
                            valid -= 1
                        
                        windows[s2[left]] -= 1
        
        return False

example = Solution()
result = example.checkInclusion("adc", "dcda")
print(result)

