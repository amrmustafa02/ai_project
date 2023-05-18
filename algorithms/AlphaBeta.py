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


def alphaBeta(board, depthLimit, playerY):
    alph = -math.inf
    beta = math.inf
    heuristicScore, move = alphaBetaHelper(board, depthLimit, playerY, alph, beta)
    return move


def alphaBetaHelper(board, depthLimit, playerZ, alpha, beta):
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
        current, trash = alphaBetaHelper(childBoard, depthLimit - 1, not playerZ,alpha, beta)
        if MiniMax.replace(current, bestScore, playerZ):
            bestScore = current
            bestMove = move
        if playerZ:
            alpha = max(alpha, bestScore)
        else:
            beta = min(beta, bestScore)
        if alpha >= beta:
            break
    return bestScore, bestMove