"""
    题目描述:
        输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
        长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
    
    链接: https://www.nowcoder.com/practice/d9162298cb5a437aad722fccccaae8a7?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
"""

import sys

def print8char(s: str):
    if len(s) == 0:
        print(s)
        return

    if len(s) % 8 != 0:
        s = s + '0'*(8 - len(s)%8)
    
    idx = 0
    while idx < len(s):
        print(s[idx: idx+8])
        idx += 8
    
    return 

while True:
    try:
        # s = sys.stdin.readline().strip()
        s = input("")  # 使用上面会死循环
        # Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
        print8char(s)
    except:
            break

# if __name__ == "__main__":
#     s = sys.stdin.readline().strip()
#     print8char(s)