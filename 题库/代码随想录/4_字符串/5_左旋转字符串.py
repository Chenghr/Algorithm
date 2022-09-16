"""
    题目描述:
        字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
        请定义一个函数实现字符串左旋转操作的功能。
        
        比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

        限制:
            1 <= k < s.length <= 10000
    
    链接: https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
""" 

"""
    思路分析:
    1. 可以申请额外空间:
        分别截取前 k 个字符和后 n-k 个字符，然后再拼接即可；

    2. 不申请额外空间，O(1) 的空间复杂度:
        先对整个字符串反转: abcdefg -> gfedcba 
        再对前 n-k 和后 k 个字符分别反转: gfedc ba -> cdefg ab

        或者先对前 k 个字符与后 n-k 个字符分别反转，再整体反转
        ab cdefg -> ba gfedc -> cdefg ab
"""

class Solution:

    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)

        def reverse(s, left, right):
            
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        reverse(s, 0, n-1)
        reverse(s, n, len(s)-1)
        reverse(s, 0, len(s)-1)

        return "".join(s)