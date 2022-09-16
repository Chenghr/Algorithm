"""
    题目:
        
"""

import sys 

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
        
    # 读取环上的数字以及对应的颜色
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    
    color = sys.stdin.readline()
    
    rScores, pScores = [0] * n, [0] * n
    rSum, pSum = 0, 0
    
    for i, score in enumerate(nums):
        if color[i] == 'R':
            rSum += score
        else:
            pSum += score
            
        rScores[i] = rSum
        pScores[i] = pSum
    
    q = int(sys.stdin.readline().strip())
    for i in range(q):
        # 读取每一行
        x = int(sys.stdin.readline().strip())
        
        if x % n == 0:
            rAns = (x // n) * rSum
            pAns = (x // n) * pSum
        else:
            rAns = (x // n) * rSum + rScores[x % n - 1]
            pAns = (x // n) * pSum + pScores[x % n - 1]
        
        print(rAns, pAns)