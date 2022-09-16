"""
    题目描述:
        写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，
        然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

    数据范围: 1 ≤ n ≤ 1000 
"""

import sys
from collections import defaultdict

def countChar(s: str, target: str) -> int:

    dic = defaultdict(int)

    for char in s:
        dic[char] += 1

    return dic[target]

if __name__ == "__main__":
    """注意查找的字符可能为空格；大小写字符需要统一一下，本题中统一为小写字符
    """
    s = sys.stdin.readline()
    target = sys.stdin.readline()

    s = s[:-1].lower()    # 所有字符中的大写字母转化为小写字母，去除最后的回车
    target = target[:-1].lower()

    count = countChar(s, target)

    print(count)