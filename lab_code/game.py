from algorithms import MiniMax
from algorithms import AlphaBeta

import time

from lab_code.board import Board


# GAME LINK
# http://kevinshannon.com/connect4/


def convertBoard(grid):
    board2 = [['-' for i in range(7)] for j in range(6)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                board2[i][j] = '-'
            elif grid[i][j] == 1:
                board2[i][j] = 'R'
            elif grid[i][j] == 2:
                board2[i][j] = 'B'
    return board2


def main(algo, level):
    board1 = Board()
    print("test1")
    time.sleep(4)
    game_end = False
    while not game_end:
        print("test2")

        (game_board, game_end) = board1.get_game_grid()
        print("test3")

        # FOR DEBUG PURPOSES
        print("------------------------------")
        board1.print_grid(game_board)
        print("------------------------------")
        # YOUR CODE GOES HERE
        boardd = convertBoard(game_board)
        MiniMax.printBoard(boardd)
        if algo == 1:
            move = MiniMax.miniMax(boardd, level, True)
        # here alpha beta
        else:
            move = AlphaBeta.alphaBeta(boardd, level, True)

        print("move = ", move)

        board1.select_column(move)

        time.sleep(2)


# main(1, 4)
