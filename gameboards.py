start_game_board = []

for i in range(4):
  start_game_board.append([" ________  " * 4, "\n| /\   _ | | /\   _ | | /\   _ | | /\   _ |", "\n|/__\/_ /| |/__\/_ /| |/__\/_ /| |/__\/_ /|",
  "\n|  _  /\ | |  _  /\ | |  _  /\ | |  _  /\ |", "\n|_|_|_\/_| |_|_|_\/_| |_|_|_\/_| |_|_|_\/_|\n"]) 

def print_board(game_board):
  for row in game_board:
    print("".join(row))

print_board(start_game_board)