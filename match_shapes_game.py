# Match the images memory game with shapes in 4x4 board where player flips pieces using row and column number until they match all the shapes

from gameboards import print_board, start_game_board, larg_tri_boards, small_tri_boards, larg_squ_boards, small_squ_boards, larg_paral_boards, small_paral_boards, larg_diamd_boards, small_diamd_boards, game_boards_dict
import random

print_board(small_diamd_boards[15])

game_board_pieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

game_board_solution_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 
12: 0, 13: 0, 14: 0, 15: 0, 16: 0}

game_board_dict = {"1x1": 1, "1x2": 2, "1x3": 3, "1x4": 4, "2x1": 5, "2x2": 6, "2x3": 7, "2x4": 8,
"3x1": 9, "3x2": 10, "3x3": 11, "3x4": 12, "4x1": 13, "4x2": 14, "4x3": 15, "4x4": 16}

shapes_dict = {1: "larg_tri_", 2: "small_tri_", 3: "larg_squ_", 4: "small_squ_", 5: "larg_paral_", 6: "small_paral_", 
7: "larg_diamd_", 8: "small_diamd_", 9: "larg_tri_", 10: "small_tri_", 11: "larg_squ_", 12: "small_squ_", 13: "larg_paral_",
14: "small_paral_", 15: "larg_diamd_", 16: "small_diamd_"}

matching_shapes = [[1, 9], [9, 1], [2, 10], [10, 2], [3, 11], [11, 3], [4, 12], [12, 4], [5, 13], [13, 5], 
[6, 14], [14, 6], [7, 15], [15, 7], [8, 16], [16, 8]]

matched_shapes = []

def game_board_solution():
  for i in range(1, 17):
    piece = random.choice(game_board_pieces)
    game_board_solution_dict[i] = piece
    game_board_pieces.pop(game_board_pieces.index(piece))

game_board_solution()
print(game_board_solution_dict.values())
print(game_board_solution_dict)

