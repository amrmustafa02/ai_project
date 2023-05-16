stateSpace1 = ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "B", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "R", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"]
stateSpace2 = ["B", "B", "B", "B", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "B", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "R", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"]
stateSpace3 = ["R", "-", "-", "-", "-", "-", "-"], \
             ["-", "R", "-", "-", "-", "-", "-"], \
             ["-", "-", "R", "-", "B", "-", "-"], \
             ["-", "-", "-", "R", "-", "-", "-"], \
             ["-", "-", "-", "-", "R", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"]


def printBoard(board):
    for x in range(6):
        print("[", end=' ')
        for y in range(7):
            print(board[x][y], end=' ')
        print("]")


def checkHorizontal(board):
    h = 0
    for x in range(6):
        for y in range(4):
            if board[x][y] == "B" and board[x][y+1] == "B" :
                return 3
            if board[x][y] == "R" and board[x][y + 1] == "R" and board[x][y + 2] == "R" and board[x][y + 3] == "R":
                return 4
            if board[x][y] == "R" and board[x][y+1] == "R" and board[x][y+2] == "R" and board[x][y+3] == "R":
                return 4
    return 0


def checkVertical(board):
    for x in range(3):
        for y in range(7):
            if board[x][y] == "B" and board[x+1][y] == "B" and board[x+2][y] == "B" and board[x+3][y] == "B":
                return 3
            if board[x][y] == "B" and board[x][y + 1] == "B" and board[x][y + 2] == "B":
                return 3

            if board[x][y] == "R" and board[x+1][y] == "R" and board[x+2][y] == "R" and board[x+3][y] == "R":
                return 4
    return 0


def checkDiagonalX(board):
    h = 0
    for x in range(3):
        for y in range(4):
            if board[x][y] == "B" and board[x + 1][y + 1] == "B":
                h

            if board[x][y] == "B" and board[x+1][y+1] == "B" and board[x+2][y+2] == "B" and board[x+3][y+3] == "B":
                return 3
            if board[x][y] == "R" and board[x+1][y+1] == "R" and board[x+2][y+2] == "R" and board[x+3][y+3] == "R":
                return 4
    return 0


def checkDiagonalY(board):
    for x in range(3):
        for y in range(6, 2, -1):
            if board[x][y] == "B" and board[x+1][y-1] == "B" and board[x+2][y-2] == "B" and board[x+3][y-3] == "B":
                return 3
            if board[x][y] == "R" and board[x+1][y-1] == "R" and board[x+2][y-2] == "R" and board[x+3][y-3] == "R":
                return 4
    return 0


def checkFull(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == "-":
                return 0
    return 1


def checkWinner(board):
    h = 0
    h += checkHorizontal(board)
    h += checkVertical(board)
    h += checkDiagonalX(board)
    h += checkDiagonalY(board)

    


def checkState(board):
    a = checkWinner(board)
    b = checkFull(board)
    if a == 3:
        return 3
    elif a == 4:
        return 4
    elif b == 1:
        return 1
    elif a == 0 or b == 0:
        return 0


print(checkState(stateSpace2))
