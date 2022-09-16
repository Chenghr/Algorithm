def findMinSteps(board, start, target):
    minStep = float('inf')
    isOK = [[True] * len(board[0]) for _ in range(len(board))]

    def backTracking(x, y, steps):
        nonlocal board, minStep, target, isOK

        if x == target[0] and y == target[1]:
            minStep = min(minStep, steps)
            return True
        
        n, m = len(board), len(board[0])

        if 1 <= x and board[x-1][y] != '0':
            # 上方两个节点
            for nx, ny in [(x-2, y-1), (x-2, y+1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == '1' or board[nx][ny] == 'T':
                        if isOK[nx][ny]:
                            board[nx][ny] = '2'

                            if not backTracking(nx, ny, steps+1):
                                isOK[nx][ny] = False

                            board[nx][ny] = '1'  # 回溯

        if x <= n-2 and board[x+1][y] != '0':
            # 下方两个节点
            for nx, ny in [(x+2, y-1), (x+2, y+1)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == '1' or board[nx][ny] == 'T':
                        if isOK[nx][ny]:
                            board[nx][ny] = '2'

                            if not backTracking(nx, ny, steps+1):
                                isOK[nx][ny] = False

                            board[nx][ny] = '1'  # 回溯

        if 1 <= y and board[x][y-1] != '0':
            # 左边两个节点
            for nx, ny in [(x-1, y-2), (x+1, y-2)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == '1' or board[nx][ny] == 'T':
                        if isOK[nx][ny]:
                            board[nx][ny] = '2'

                            if not backTracking(nx, ny, steps+1):
                                isOK[nx][ny] = False

                            board[nx][ny] = '1'  # 回溯

        if y <= m-2 and board[x][y+1] != '0':
            # 右边两个节点
            for nx, ny in [(x-1, y+2), (x+1, y+2)]:
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == '1' or board[nx][ny] == 'T':
                        if isOK[nx][ny]:
                            board[nx][ny] = '2'

                            if not backTracking(nx, ny, steps+1):
                                isOK[nx][ny] = False

                            board[nx][ny] = '1'  # 回溯
        
        return False

    backTracking(start[0], start[1], 0)

    return -1 if minStep == float('inf') else minStep


while True:
    try:
        T = int(input(""))
        ans = []
        for _ in range(T):
            n, m = map(int, input("").split())

            board = []
            start, target = None, None

            for i in range(n):
                row = list(input(""))
                board.append(row)

                if 'K' in row:
                    start = (i, row.index('K'))
                
                if 'T' in row:
                    target = (i, row.index('T'))
            
            minStep = findMinSteps(board, start, target)

            print(minStep)
            
    except:
        break
