"""题目描述:
    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
    给定的字符串只含有小写英文字母，并且长度不超过10000。

    https://leetcode-cn.com/problems/repeated-substring-pattern/
"""

"""解题思路:
    如果一个字符串可以由子串重复多次构成，则必定有相同前后缀；
    那么反过来，给出一个字符串，我们可以计算出它的前缀表( KMP 中的 next 数组)；
    数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        def getNext(pattern: str) -> list:
            next = [0] * len(pattern)
            next[0] = 0

            j = 0  # j 前缀的末尾指针

            # i 后缀的末尾指针
            for i in range(1, len(pattern)):
                # 当前不匹配
                while j > 0 and pattern[i] != pattern[j]:
                    j = next[j-1]  # 向前回退
                
                # 当前字符匹配
                if pattern[i] == pattern[j]:
                    j += 1
                
                # 填充next数组
                next[i] = j
            
            return next
        
        if len(s) == 0:
            return False
        
        next = getNext(s)

        if next[-1] != 0 and len(s) % next[-1] == 0:
            return True
        else:
            return False