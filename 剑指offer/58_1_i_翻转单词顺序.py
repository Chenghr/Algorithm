"""
    输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
    为简单起见，标点符号和普通字母一样处理。
    例如输入字符串"I am a student. "，则输出"student. a am I"。

    说明: 
        无空格字符构成一个单词。
        输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
        如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        left = -1

        s += ' '  # 避免额外的判断
        for right in range(len(s)):
            if s[right] != ' ' and left == -1:
                left = right  # 单词起点
            
            if s[right] == ' ' and left != -1:
                # 单词终点
                if len(ans) == 0:
                    ans = s[left: right]
                else:
                    ans = s[left: right] + ' ' + ans

                left = -1
        
        return ans
    
    def reverseWords1(self, s: str) -> str:
        """偷懒方法
        """
        s = s.strip() # 删除首尾空格

        # split() 方法将单词间的 “多个空格看作一个空格” 因此不会出现多余的 “空单词” 
        # split(' ')的时候，多个空格都要分割，每个空格分割出来空。
        strs = s.split() # 分割字符串

        strs.reverse() # 翻转单词列表

        # 语法：  'sep'.join(seq) :  以sep作为分隔符，将seq所有的元素合并成一个新的字符串
        return ' '.join(strs) # 拼接为字符串并返回
