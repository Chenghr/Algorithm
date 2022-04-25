"""
    字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
    请定义一个函数实现字符串左旋转操作的功能。
    比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
"""

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        """进行三次反转，假装避免额外空间开销（python str不可更改因此实际达不到）
            python中可以使用:
                1. 字符串切片;
                2. 列表遍历拼接;
                3. 字符串遍历拼接;
        """
        def reverse(left, right):
            nonlocal s

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        s = list(s)
        reverse(0, n-1)
        reverse(n, len(s)-1)
        reverse(0, len(s)-1)

        return ''.join(s)
