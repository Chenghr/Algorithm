"""
    题目描述:
        计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。
        （注: 字符串末尾不以空格为结尾）
    
    链接: https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&tqId=21224&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
"""
import sys

def lastWordLength(s: str) -> int:
    for i in range(len(s)-1, -1, -1):
        if s[i].isalpha():
            # 找到单词的起点
            for j in range(i-1, -1, -1):
                if not s[j].isalpha():
                    # 单词的重点
                    return i - j

            # 从 0 到 i 为一个单词
            return i + 1
    
    return 0

if __name__ == "__main__":
    """
        判断单词长度: 寻找单词的起始点
        单词的合法性: 每个字符均为字母（大小写均可），不存在空格等其他字符
    """
    s = sys.stdin.readline().strip()

    wordLength = lastWordLength(s)

    print(wordLength)
    

