stateSpace1 = ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
             ["-", "-", "-", "-", "-", "-", "-"], \
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


def checkHorizontal(board,color):
    h = 0
    for x in range(6):
        for y in range(7):
            if y < 6:
                if board[x][y] == color and board[x][y + 1] == color:
                    h += 1
            if y < 5:
                if board[x][y] == color and board[x][y + 1] == color and board[x][y + 2] == color:
                    h += 100
            if y < 4:
                if board[x][y] == color and board[x][y + 1] == color and board[x][y + 2] == color and board[x][y + 3] == color:
                    h += 1000
    return h


def checkVertical(board, color):
    h = 0
    for x in range(6):
        for y in range(7):
            if x < 5:
                if board[x][y] == color and board[x+1][y] == color:
                    h += 1
            if x < 4:
                if board[x][y] == color and board[x+1][y] == color and board[x+2][y] == color:
                    h += 100
            if x < 3:
                if board[x][y] == color and board[x][y + 1] == color and board[x][y + 2] == color and board[x+3][y] == color:
                    h += 1000
    return h


def checkDiagonalX(board, color):
    h = 0
    for x in range(6):
        for y in range(7):
            if x<5 and y<6:
                if board[x][y] == color and board[x + 1][y + 1] == color:
                    h += 1
            if x < 4 and y < 5:
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color:
                    h += 100
            if x < 3 and y < 4:
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color and board[x + 3][y + 3] == color:
                    h += 1000
    return h


def checkDiagonalY(board, color):
    h = 0
    for x in range(6):
        for y in range(7, 0, -1):
            if x < 5 and y < 0:
                if board[x][y] == color and board[x + 1][y - 1] == color:
                    h += 1
            if x < 4 and y < 1:
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color:
                    h += 100

            if x < 3 and y < 2:
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color and board[x + 3][ y - 3] == color:
                    h += 1000
    return h


def checkFull(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == "-":
                return 0
    return 1


def checkWinner(board, color):
    h = 0
    h += checkHorizontal(board, color)
    h += checkVertical(board, color)
    h += checkDiagonalX(board, color)
    h += checkDiagonalY(board, color)
    return h


def checkState(board, color1, color2):
    a = checkWinner(board, color1)
    b = checkWinner(board, color2)
    heuristic = a - b
    return b


print(checkState(stateSpace2, "R", "B"))
