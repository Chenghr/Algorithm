"""
    给你一个字符串 s ，逐个翻转字符串中的所有单词。
    单词是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

    请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

    说明：
        输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
        翻转后单词间应当仅用一个空格分隔。
        翻转后的字符串中不应包含额外的空格。

    提示：
        1 <= s.length <= 104
        s 包含英文大小写字母、数字和空格 ' '
        s 中 至少存在一个 单词

    https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""

"""思路分析

    - 要点:
        1. s 中原来单词间可能间隔有多个空格，反转后只保留一个空格;
        2. 翻转后的 s 中开头和结尾都不应有空格;
        3. 仅翻转单词间的顺序，单词内的顺序不改变;

    - 方法:
    1. 不考虑额外空间开销:
        遍历 s，使用 tag 标记是否处于单词中，遍历完一个单词，就将其存储到 list中；
        逆序遍历 list，得到符合要求的逆序字符串；

        Note:
            注意边界条件，即最后一个单词后面没有空格的情况，具体还要分两种，
            一种是仅有一个字符，另一种是多个字符（采用 tag 标记带来的影响）。
    
    2. 不使用额外空间，O(1)空间开销内完成：
        a. 移除多余空格;
        b. 反转整个字符串;
        c. 反转字符串中的单词;
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        word = []

        # 标记是否找到一个单词的开头，以及单词的起止下标
        tag, left, right = False, 0, 0

        for index, ch in enumerate(s):
            if tag == False:
                # 当前不处于一个单词内
                if ch == ' ':
                    continue
                elif ch != ' ':
                    tag = True
                    left = index

                    if index == len(s) - 1:
                        # 走到了字符串的末尾，且处于单词中
                        word.append(s[left:])
            else:
                # 当前处于一个单词内
                if ch == ' ':
                    tag = False
                    right = index
                    word.append(s[left : right])
                elif index == len(s)-1:
                    # 走到了字符串的末尾，且处于单词中
                    word.append(s[left:])
                else:
                    continue
        
        result = word[len(word)-1]

        for i in range(len(word)-2, -1, -1):
            result = result + ' ' + word[i]
        
        return result
    
    def removeExtraSpaces(self, s: str) -> str:
        """移除字符串中的多余空格，使用快慢指针法
        """
        s = list(s)
        fast, slow = 0, 0

        # 去除开头的空格
        while (s[fast] == ' ' and fast < len(s)):
            fast += 1
        
        # 去除中间部分字符串的冗余空格
        while (fast < len(s)):
            # 如果fast指向空格，且之前也为空格，则跳过赋值
            if s[fast] == ' ' and fast >= 1 and s[fast] == s[fast-1]:
                fast += 1
            else:
                s[slow] = s[fast]
                fast += 1
                slow += 1
        
        # 去除字符串末尾的空格
        if slow >= 1 and s[slow-1] == ' ':
            slow -= 1
        
        # resize
        s = s[ : slow]

        return "".join(s)
