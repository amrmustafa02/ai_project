
import time
import random

from lab_code.board import Board


# GAME LINK
# http://kevinshannon.com/connect4/


def main(algorithm, level):
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column = random.randint(0, 6)
        board.select_column(random_column)

        time.sleep(2)



