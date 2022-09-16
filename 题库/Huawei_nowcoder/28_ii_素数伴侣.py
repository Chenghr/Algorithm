"""
    题目描述:
        若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
        从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”
        能组成“素数伴侣”最多的方案称为“最佳方案”，求出最佳方案的个数。
"""
"""
    1. 素数一定是一个奇数和一个偶数的和；（素数不可能为偶数）
    2. 素数判定的优化: 取开方，素数表的筛选
    3. 最优匹配: 匈牙利算法（二分图）
"""

# 匈牙利算法
def match(i):
    for j in range(M):
        # 有边且未访问
        if matrix[i][j] == 1 and not visit[j]:
            visit[j] = True
            # 如果暂无匹配，或者原来匹配的元素可以找到新的匹配
            if matched[j] == -1 or match(matched[j]):
                matched[j] = i
                return True
    return False

while True:
    try:
        # 输入
        n = int(input())
        lst = list(map(int,input().split()))
    except:
        break
    else:
        # 分为奇偶元素
        evens,odds = [],[]
        for i in lst:
            if i % 2 == 0: evens.append(i)
            else: odds.append(i)
        N,M = len(evens),len(odds)
        # 创建空邻接矩阵
        matrix = []
        for i in range(N):
            temp = []
            for j in range(M):
                temp.append(0)
            matrix.append(temp)
        # 填充矩阵
        for i in range(N):
            for j in range(M):
                val = evens[i] +odds[j]
                if val <= 3:
                    matrix[i][j] = 1
                else:
                    flag = True
                    for k in range(2,int(val**0.5)+1):
                        if val%k == 0:  flag = False
                    if flag : matrix[i][j] = 1
        # 记录已匹配矩阵和已访问矩阵
        matched = [-1 for i in range(M)]
        # 开始匈牙利算法，进行匹配
        count = 0
        for i in range(N):
            visit = [False for j in range(M)]
            if match(i):
                count += 1
        print(count)
