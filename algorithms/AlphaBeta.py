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
    children = MiniMax.getChildren(board, playerZ)
    for child in children:
        move, childBoard = child
        current, trash = alphaBetaHelper(childBoard, depthLimit - 1, not playerZ)
        if replace(current, bestScore, playerZ):
            bestScore = current
            bestMove = move
    return bestScore, bestMove