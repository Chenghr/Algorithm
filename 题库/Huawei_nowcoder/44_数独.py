"""
    填满一个 9 * 9 的棋盘
    链接: https://www.nowcoder.com/practice/78a1a4ebe8a34c93aac006c44f6bf8a1?tpId=37&tqId=21267&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D5%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=5&judgeStatus=undefined&tags=&title=
"""

def check(board, row, col, num):
    """判断在位置 i, j 上放置 num 是否合法
    """
    for j in range(9):
        if board[row][j] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False
    
    for i in range((row//3)*3, (row//3 + 1)*3):
        for j in range((col//3)*3, (col//3 + 1)*3):
            if board[i][j] == num:
                return False

    return True

def backTracking(board):
    for row in range(9):
        for col in range(9):

            if board[row][col] != 0:
                continue

            for num in range(1, 10):
                if check(board, row, col, num):

                    board[row][col] = num

                    if backTracking(board):
                        return True
                    
                    board[row][col] = 0
            
            return False
    
    return True

if __name__ == "__main__":
    board = []

    for _ in range(9):
        row = list(map(int, input("").split()))
        board.append(row)
    
    if backTracking(board):
        for row in board:
            s = str(row[0])

            for i in range(1, 9):
                s += ' ' + str(row[i])
            
            print(s)
