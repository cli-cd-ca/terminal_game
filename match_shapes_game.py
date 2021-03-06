# Codecademy - CS101: Introduction to Programming - Final Project
# Match the images memory game with shapes on 4x4 board where player flips pieces using row and column number until they match all shapes

# imports print board function, start board, game board rows for each sized shape, and game piece rows from game boards file
from gameboards import *
import random

# Numbers that represent pairs of four shapes (triangle, square, parallelogram, and diamond) 
# in large and small sizes to assign random shapes to every piece in the game board solution dictionary
shape_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# The random shape assigned to every spot on 4x4 board with zero assigned before first game solution
game_board_solution_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 
12: 0, 13: 0, 14: 0, 15: 0, 16: 0}

# A string name for player's row and column number paired with each spot in the game board solution dictionary
game_board_dict = {"1x1": 1, "1x2": 2, "1x3": 3, "1x4": 4, "2x1": 5, "2x2": 6, "2x3": 7, "2x4": 8,
"3x1": 9, "3x2": 10, "3x3": 11, "3x4": 12, "4x1": 13, "4x2": 14, "4x3": 15, "4x4": 16}

# Number that represents matching shapes in the game board solution paired with the game board rows for each shape 
shapes_dict = {1: larg_tri_row, 2: small_tri_row, 3: larg_squ_row, 4: small_squ_row, 5: larg_paral_row, 6: small_paral_row, 
7: larg_diamd_row, 8: small_diamd_row, 9: larg_tri_row, 10: small_tri_row, 11: larg_squ_row, 12: small_squ_row, 13: larg_paral_row,
14: small_paral_row, 15: larg_diamd_row, 16: small_diamd_row}

# List of matching shapes from shapes dictionary to identify when player matches shapes
# (the pairs are reversed so the player can match shapes in any order)
matching_shapes = [[1, 9], [9, 1], [2, 10], [10, 2], [3, 11], [11, 3], [4, 12], [12, 4], [5, 13], [13, 5], 
[6, 14], [14, 6], [7, 15], [15, 7], [8, 16], [16, 8]]

# Empty list that holds shapes matched from matching shapes above when player matches shapes
matched_shapes = []

# Assigns random shapes from shape numbers list to solution dictionary
def game_board_solution():
  for i in range(1, 17):
    shape = random.choice(shape_nums)
    game_board_solution_dict[i] = shape
    shape_nums.pop(shape_nums.index(shape))

# Prints title, start board and game instructions
def start_game_setup():
  print("_____________ Match the Shapes ____________")
  for row in start_game_board:
    print_board(row)
  print("Enter row and column number to flip pieces")

# Player can match shapes for 100 tries and exit game with empty inputs
def play_game():
  flipped_pieces = []
  for i in range(100):
    row_num = input("Row: ")
    column_num = input("Column: ")
    if row_num == "" and column_num == "":
      exit_game = input("Do you want to exit the game? (y/n) ")
      if exit_game == "n":
        continue
      quit()
    elif row_num not in ['1', '2', '3', '4'] or column_num not in ['1', '2', '3', '4']:
      print("Enter 1, 2, 3, or 4")
      continue
    else:
      player_piece = row_num + "x" + column_num
      shape_num = game_board_solution_dict[game_board_dict[player_piece]]
      if shape_num in matched_shapes:
        print("You already matched that shape")
        continue
      flipped_pieces.append(shape_num)
      print("\n" * 1010)
      print_player_board(int(row_num), int(column_num), shape_num)
      print("")
      if len(flipped_pieces) == 3:
        flipped_pieces.pop(0)
      if flipped_pieces in matching_shapes:
        matched_shapes_(flipped_pieces)
      if len(matching_shapes) == 8:
        win_game()
        quit()

# Prints game board with shape at player's row and column number
def print_player_board(row, column, shape):
  shape_row = shapes_dict[shape]
  shape_col = column - 1
  if row == 1:
    print_board(shape_row[shape_col])
    print_board(game_piece_row[2])
  if row == 2:
    print_board(game_piece_row[0])
    print_board(shape_row[shape_col])
    print_board(game_piece_row[1])
  if row == 3:
    print_board(game_piece_row[1])
    print_board(shape_row[shape_col])
    print_board(game_piece_row[0])
  if row == 4:
    print_board(game_piece_row[2])
    print_board(shape_row[shape_col])

# Called when player matches two shapes in flipped pieces list
def matched_shapes_(flipped_pieces):
  print("You matched the shapes!")
  matched_shapes.extend(flipped_pieces)
  shape_nums.extend(flipped_pieces)
  matching_shapes.remove(flipped_pieces)

# Called when player matches 8 pairs from matching shapes list and allows player to play again or exit game 
def win_game():
  print("Game won! You matched all the shapes!")
  matched_shapes.sort()
  matched_shapes_paired = [[x, x + 8] for x in matched_shapes[:8]]
  matched_shapes_paired.extend([[x, x - 8] for x in matched_shapes[8:]])
  matching_shapes.extend([pair for pair in matched_shapes_paired if pair not in matching_shapes])
  matching_shapes.sort()
  matched_shapes.clear()
  play_again = input("Would you like to play again? (y/n) ")
  if play_again == "y":
    print("\n" * 1010)
    game_board_solution()
    start_game_setup()
    play_game()

# Calls the first game with solution, start game setup, and play game functions
game_board_solution()
start_game_setup()
play_game()
