board = ["_","_","_",
         "_","_","_",   
         "_","_","_" ]


gameplay = True
current_player = "X"
winner = None

def gaming_board ():
  print(board[0]+" | ", board[1]+" | ",board[2]+" | ")
  print(board[3]+" | ", board[4]+" | ",board[5]+" | ")
  print(board[6]+" | ", board[7]+" | ",board[8]+" | ")

def Tic_Tac_Toe():
     while gameplay :
        
        on_board(current_player)

        flip_player()

        check_for_winners()

        winners()

def on_board(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "_":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  gaming_board()

def flip_player():
  global current_player

  if current_player == "X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"


def check_for_winners ():


  global winner

  row_winners()

  column_winners()

  diagonal_winners()

  row_winner = row_winners()

  column_winner = column_winners()

  diagonal_winner = diagonal_winners()

  if row_winner:
    winner= row_winner
  elif column_winner:
    winner= column_winners()

  elif diagonal_winner:
    winner = diagonal_winners()



def winners():
  global winner
  global gameplay

  if winner == "X" or winner == "O":
    print(winner , " won.")

  elif "_" not in board :
    print("Tied.")   
    gameplay = False


def row_winners():
  
    global gameplay

    row1 = board[0] == board[1] == board[2] !="_"
    row2 = board[3] == board[4] == board[5] !="_"
    row3 = board[6] == board[7] == board[8] !="_"

    if row1 or row2 or row3:
      gameplay = False

    if row1:
      return board[0]
    elif row2:
      return board[3] 
    elif row3:
      return board[6]
  # Or return None if there was no winner
    else:
      return None

def column_winners():
    
    global gameplay

    col1 = board[0] == board[3] == board[6] !="_"
    col2 = board[1] == board[4] == board[7] !="_"
    col3 = board[2] == board[5] == board[8] !="_"

    if col1 or col2 or col3:
      gameplay = False
    if col1:
      return board[0]

    elif col2:
      return board[1]

    elif col3:
      return board[2]

    else:
      return None

    return

def diagonal_winners():
    global gameplay

    diagonal1 = board[0] == board[4] == board[8] !="_"
    diagonal2 = board[2] == board[4] == board[6] !="_"

    if diagonal1 or diagonal2 :
      gameplay = False
    if diagonal1:
      return board[0]

    elif diagonal2:
      return board[2]

    else:
      return None

    return

Tic_Tac_Toe()  
