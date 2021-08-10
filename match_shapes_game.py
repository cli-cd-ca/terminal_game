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

def start_game_setup():
  print("_____________ Match the Shapes ____________")
  print_board(start_game_board)
  print("Enter row and column number to flip pieces")

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
      print(flipped_pieces)
      player_board = shapes_dict[shape_num] + player_piece
      print("\n" * 986)
      print_board(game_boards_dict[player_board])
      if flipped_pieces in matching_shapes:
        matched_shapes_(flipped_pieces)
      if len(flipped_pieces) == 3:
        flipped_pieces.pop(0)
      if flipped_pieces in matching_shapes:
        matched_shapes_(flipped_pieces)
      print(flipped_pieces)
      if len(matching_shapes) == 8:
        win_game()
        quit()

def matched_shapes_(flipped_pieces):
  print("You matched the shapes!")
  matched_shapes.extend(flipped_pieces)
  game_board_pieces.extend(flipped_pieces)
  matching_shapes.remove(flipped_pieces)
  print(matching_shapes)
  print(matched_shapes)

def win_game():
  print("Game won! You matched all the shapes!")
  matched_shapes.sort()
  matched_shapes_paired = [[x, x + 8] for x in matched_shapes[:8]]
  matched_shapes_paired.extend([[x, x - 8] for x in matched_shapes[8:]])
  matching_shapes.extend([pair for pair in matched_shapes_paired if pair not in matching_shapes])
  matching_shapes.sort()
  print(matching_shapes)
  matched_shapes.clear()
  play_again = input("Would you like to play again? (y/n) ")
  if play_again == "y":
    game_board_solution()
    print(game_board_solution_dict.values())
    print(game_board_solution_dict)
    start_game_setup()
    play_game()

game_board_solution()
print(game_board_solution_dict.values())
print(game_board_solution_dict)
start_game_setup()
play_game()
