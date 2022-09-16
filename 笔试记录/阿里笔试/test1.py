if __name__ == "__main__":
    n, m = map(int, input('').split())

    board = []
    for i in range(n):
        row = list(input("").strip())

        if '*' in row:
            x, y = i, row.index('*')

        board.append(row)
    
    ops = list(input('').strip())

    score = 0
    for op in ops:
        if op == 'W' and x > 0:
            x -= 1
        elif op == 'S' and x < n-1:
            x += 1
        elif op == 'A' and y > 0:
            y -= 1
        elif op == 'D' and y < m-1:
            y += 1
        
        if board[x][y] == '$':
            board[x][y] = '.'
            score += 1
    
    print(score)