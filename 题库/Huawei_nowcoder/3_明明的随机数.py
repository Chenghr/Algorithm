"""
    题目描述:
        明明生成了 N 个1到500之间的随机整数。
        请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，
        然后再把这些数从小到大排序，按照排好的顺序输出。

    数据范围： 1≤n≤1000  ，输入的数字大小满足 1≤val≤500 
"""

import sys

if __name__ == "__main__":
    """
        两种思想:
            1. set 去重 + 快排；
            2. 本题随机数范围有限，可以使用数组去重+排序输出
    """
    tag = [0] * 501

    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        tag[num] = 1
    
    for i in range(1, 501):
        if tag[i] == 1:
            print(i)