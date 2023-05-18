
import time
import random

from lab_code.board import Board

from algorithms import MiniMax

from lab_code import board
import time

from lab_code.board import Board


# GAME LINK
# http://kevinshannon.com/connect4/


def convertBoard(grid):
    board = [['-' for i in range(7)] for j in range(6)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                board[i][j] = '-'
            elif grid[i][j] == 1:
                board[i][j] = 'R'
            elif grid[i][j] == 2:
                board[i][j] = 'B'
    return board


def main(algo, level):
    board = Board()

    time.sleep(4)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        print("------------------------------")
        board.print_grid(game_board)
        print("------------------------------")
        # YOUR CODE GOES HERE
        boardd = convertBoard(game_board)
        MiniMax.printBoard(boardd)
        if algo == 1:
            move = MiniMax.miniMax(boardd, level, True)
        # here alpha beta
        else:
            move = MiniMax.miniMax(boardd, level, True)

        print("move = ", move)

        board.select_column(move)

        time.sleep(2)


if _name_ == '_main_':
    main(1, 3)


