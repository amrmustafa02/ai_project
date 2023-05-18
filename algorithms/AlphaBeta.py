import math
from copy import deepcopy
from algorithms import MiniMax

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

# Unused function
def checkFull(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == "-":
                return 0
    return 1




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


def alphaBeta(board, depthLimit, playerY):
    heuristicScore, move = alphaBetaHelper(board, depthLimit, playerY)
    return move


def alphaBetaHelper(board, depthLimit, playerZ):
    if depthLimit == 0:
        return MiniMax.heuristic(board, "R", "B"), -1

    if playerZ:
        bestScore = -math.inf

    else:
        bestScore = math.inf

    bestMove = -1
    children = getChildren(board, playerZ)
    for child in children:
        move, childBoard = child
        current, trash = alphaBetaHelper(childBoard, depthLimit - 1, not playerZ)
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
