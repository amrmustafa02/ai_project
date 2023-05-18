import math
from copy import deepcopy

stateSpace1 = \
    ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "B", "R", "-", "-", "-"], \
        ["-", "-", "B", "R", "R", "-", "-"], \
        ["-", "-", "R", "B", "B", "R", "-"]

stateSpace2 = \
    ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["R", "R", "R", "-", "-", "-", "-"]

stateSpace3 = \
    ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "-", "-", "-", "-", "-"], \
        ["-", "-", "R", "R", "-", "-", "-"], \
        ["-", "R", "B", "B", "-", "-", "-"], \
        ["R", "B", "R", "B", "-", "-", "-"]


def printBoard(board):
    for x in range(6):
        print("[", end=' ')
        for y in range(7):
            print(board[x][y], end=' ')
        print("]")


def checkHorizontal(board, color):
    h = 0
    for x in range(6):
        for y in range(7):
            if y < 6:
                if board[x][y] == color and board[x][y + 1] == color:
                    h += 10
            if y < 5:
                if board[x][y] == color and board[x][y + 1] == color and board[x][y + 2] == color:
                    h += 100
            if y < 4:
                if board[x][y] == color and board[x][y + 1] == color and board[x][y + 2] == color \
                        and board[x][y + 3] == color:
                    h += 10000
    return h


def checkVertical(board, color):
    h = 0
    for x in range(6):
        for y in range(7):
            if x < 5:
                if board[x][y] == color and board[x + 1][y] == color:
                    h += 10
            if x < 4:
                if board[x][y] == color and board[x + 1][y] == color and board[x + 2][y] == color:
                    h += 100
            if x < 3:
                if board[x][y] == color and board[x + 1][y] == color and board[x + 2][y] == color \
                        and board[x + 3][y] == color:
                    h += 10000
    return h


def checkDiagonalX(board, color):
    h = 0
    for x in range(6):
        for y in range(7):
            if x < 5 and y < 6:
                if board[x][y] == color and board[x + 1][y + 1] == color:
                    h += 10
            if x < 4 and y < 5:
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color:
                    h += 100
            if x < 3 and y < 4:
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color and \
                        board[x + 3][y + 3] == color:
                    h += 10000
    return h


def checkDiagonalY(board, color):
    h = 0
    for x in range(6):
        for y in range(6, 0, -1):
            if x < 5 and y > 0:
                if board[x][y] == color and board[x + 1][y - 1] == color:
                    h += 10
            if x < 4 and y > 1:
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color:
                    h += 100

            if x < 3 and y > 2:
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color and \
                        board[x + 3][y - 3] == color:
                    h += 10000
    return h


# Unused function
def checkFull(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == "-":
                return 0
    return 1


def heuristicHelper(board, color):
    h = 0
    h += checkHorizontal(board, color)
    h += checkVertical(board, color)
    h += checkDiagonalX(board, color)
    h += checkDiagonalY(board, color)
    return h


def heuristic(board, color1, color2):
    a = heuristicHelper(board, color1)
    b = heuristicHelper(board, color2)
    totalHeuristic = a - b
    return totalHeuristic


def replace(currentScore, bestScore, playerX):
    if playerX:
        color = "R"
    else:
        color = "B"

    if color == "R":
        if currentScore > bestScore:
            return True
        else:
            return False
    else:
        if currentScore < bestScore:
            return True
        else:
            return False


def miniMax(board, depthLimit, playerY):
    heuristicScore, move = miniMaxHelper(board, depthLimit, playerY)
    return move


def miniMaxHelper(board, depthLimit, playerZ):
    if depthLimit == 0:
        return heuristic(board, "R", "B"), -1

    if playerZ:
        bestScore = -math.inf

    else:
        bestScore = math.inf

    bestMove = -1
    children = getChildren(board, playerZ)
    for child in children:
        move, childBoard = child
        current, trash = miniMaxHelper(childBoard, depthLimit - 1, not playerZ)
        if replace(current, bestScore, playerZ):
            bestScore = current
            bestMove = move
    return bestScore, bestMove


def makeMove(num, boardMove, color):
    for x in range(6):
        if (boardMove[x][num] == "R" or boardMove[x][num] == "B") and x != 0 and boardMove[x - 1][num] == "-":
            boardMove[x - 1][num] = color
            return boardMove
        if x == 5 and x != 0 and boardMove[x - 1][num] == "-":
            boardMove[x][num] = color
            return boardMove
    return boardMove


def isFullColumn(boardColumn, num):
    for x in range(6):
        if boardColumn[x][num] == "-":
            return False
    return True


def getChildren(boardChildren, playerJ):
    children = []
    if playerJ:
        color = "R"
    else:
        color = "B"
    for i in range(7):
        if not isFullColumn(deepcopy(boardChildren), i):
            childK = makeMove(i, deepcopy(boardChildren), color)
            children.append((i, childK))
    return children


def printChildren(children):
    for i in range(7):
        j, k = children[i]
        printBoard(k)
        print()


# To test miniMax Algorithm
print(miniMax(stateSpace3, 5, True))
