def getMinChange_base(n, numsA, numsB):
    dp = [[0, 0] for _ in range(n)]

    for i in range(1, n):
        if numsA[i] > numsA[i-1] and numsA[i] > numsB[i-1]:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
        elif numsA[i] <= numsA[i-1] and numsA[i] > numsB[i-1]:
            dp[i][0] = dp[i-1][1]
        elif numsA[i] > numsA[i-1] and numsA[i] <= numsB[i-1]:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = float('inf')
        
        if numsB[i] > numsA[i-1] and numsB[i] > numsB[i-1]:
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
        elif numsB[i] <= numsA[i-1] and numsB[i] > numsB[i-1]:
            dp[i][1] = dp[i-1][1] + 1
        elif numsB[i] > numsA[i-1] and numsB[i] <= numsB[i-1]:
            dp[i][1] = dp[i-1][0] + 1
        else:
            dp[i][1] = float('inf')
        
        if dp[i][0] == float('inf') and dp[i][1] == float('inf'):
            return -1
    
    return min(dp[-1][0], dp[-1][1])

def getMinChange_v1(n, numsA, numsB):
    dp = [[0, 0] for _ in range(n)]

    for i in range(1, n):
        if numsA[i] >= numsA[i-1] and numsA[i] >= numsB[i-1]:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
        elif numsA[i] < numsA[i-1] and numsA[i] >= numsB[i-1]:
            dp[i][0] = dp[i-1][1]
        elif numsA[i] >= numsA[i-1] and numsA[i] < numsB[i-1]:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = float('inf')
        
        if numsB[i] >= numsA[i-1] and numsB[i] >= numsB[i-1]:
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
        elif numsB[i] < numsA[i-1] and numsB[i] >= numsB[i-1]:
            dp[i][1] = dp[i-1][1] + 1
        elif numsB[i] >= numsA[i-1] and numsB[i] < numsB[i-1]:
            dp[i][1] = dp[i-1][0] + 1
        else:
            dp[i][1] = float('inf')
        
        if dp[i][0] == float('inf') and dp[i][1] == float('inf'):
            return -1
    
    return min(dp[-1][0], dp[-1][1])

def getMinChange(n, numsA, numsB):
    if n <= 1:
        return 0

    dp = [[0, 0], [0, 0]]

    for i in range(1, n):
        if numsA[i] > numsA[i-1] and numsA[i] > numsB[i-1]:
            dp[1][0] = min(dp[0][0], dp[0][1])
        elif numsA[i] <= numsA[i-1] and numsA[i] > numsB[i-1]:
            dp[1][0] = dp[0][1]
        elif numsA[i] > numsA[i-1] and numsA[i] <= numsB[i-1]:
            dp[1][0] = dp[0][0]
        else:
            dp[1][0] = float('inf')
        
        if numsB[i] > numsA[i-1] and numsB[i] > numsB[i-1]:
            dp[1][1] = min(dp[0][0], dp[0][1]) + 1
        elif numsB[i] <= numsA[i-1] and numsB[i] > numsB[i-1]:
            dp[1][1] = dp[0][1] + 1
        elif numsB[i] > numsA[i-1] and numsB[i] <= numsB[i-1]:
            dp[1][1] = dp[0][0] + 1
        else:
            dp[1][1] = float('inf')
        
        if dp[1][0] == float('inf') and dp[1][1] == float('inf'):
            return -1
        
        dp[0] = dp[1].copy()
    
    if dp[1][0] == float('inf') and dp[1][1] == float('inf'):
        return -1
    return min(dp[1][0], dp[1][1])

if __name__ == '__main__':
    n = int(input(""))
    numsA = list(map(int, input("").split()))
    numsB = list(map(int, input("").split()))

    # ans = getMinChange_base(n, numsA, numsB)
    # ans = getMinChange_v1(n, numsA, numsB)
    ans = getMinChange(n, numsA, numsB)
    print(ans)