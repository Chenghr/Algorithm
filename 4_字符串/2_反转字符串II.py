"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，
    每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
    如果剩余字符少于 k 个，则将剩余字符全部反转。
    如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

提示：
    1 <= s.length <= 104
    s 仅由小写英文组成
    1 <= k <= 104

https://leetcode-cn.com/problems/reverse-string-ii/
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index, s = 0, list(s)

        while (index < len(s)):
            # 反转前 k 个字符
            if index + k <= len(s):
                left, right = index, index+k-1

                while (left < right):
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                
                index += 2*k
            else:
                # 反转剩下的所有字符
                left, right = index, len(s)-1

                while (left < right):
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                
                break
    
        return "".join(s)

solution = Solution()
print(solution.reverseStr("abcdefg", 8))

# 额外知识
"""
python 中 str 属于不可修改的数据类型；
对字符串进行修改，可以先将其转换为 list，再使用字符串的 join 函数转回字符串
"""