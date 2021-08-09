# Match the images memory game with shapes in 4x4 board where player flips pieces using row and column number until they match all the shapes

from gameboards import print_board, start_game_board, larg_tri_boards, small_tri_boards, larg_squ_boards, small_squ_boards, larg_paral_boards, small_paral_boards, larg_diamd_boards, small_diamd_boards, game_boards_dict
import random

print_board(small_diamd_boards[15])

game_board_pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

game_board_solution_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 
12: 0, 13: 0, 14: 0, 15: 0, 16: 0}

def game_board_solution():
  for i in range(1, 17):
    piece = random.choice(game_board_pieces)
    game_board_solution_dict[i] = piece
    game_board_pieces.pop(game_board_pieces.index(piece))

game_board_solution()
print(game_board_solution_dict.values())
print(game_board_solution_dict)