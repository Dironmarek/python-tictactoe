import library.functions as functions

#Calculate what move the computer should make
def compMove(board):
  exampleBoard=board
  #First priority is to find if there is a winning place 
  for i in range(3):
    for j in range(3):
      exampleBoard[j][i]=2
      if functions.detect_win(exampleBoard)==2:
        return [j,i]

  #Second priority is to block winning place of opposition
  blockWin=humanTwoInARow(board)
  if blockWin!=-1:
    return blockWin
    #Third priority is to take control of the center
  elif board[1][1]==0:
    return [1,1]
    #Fourth priority is to take control of the corners
  elif board[0][0]==0:
    return [0,0]
  elif board[0][2]==0:
    return [0,2]
  elif board[2][0]==0:
    return [2,0]
  else:
    return [2,2]

#Find if the human opponent has a two in a row
def humanTwoInARow(board):
  #Check rows
  for i in range(3):
    if board[i]==[1,1,0]:
      return [i,2]
    elif board[i]==[0,1,1]:
      return [i,0]
    elif board[i]==[1,0,1]:
      return [i,1]

  #Check diagonal (left-right)
  if board[0][0]==1 and board[1][1]==1:
    return [2,2]
  elif board[0][0]==1 and board[2][2]==1:
    return [1,1]
  elif board[1][1]==1 and board[2][2]==1:
    return [0,0]

  #Check diagonal (right-left)
  if board[0][2]==1 and board[1][1]==1:
    return [2,0]
  elif board[0][2]==1 and board[2][0]==1:
    return [1,1]
  elif board[1][1]==1 and board[2][0]==1:
    return [0,2]

  #Check columns
  for i in range(3):
    if board[0][i]==1 and board[1][i]==1:
      return [2,i]
    elif board[0][i]==1 and board[2][i]==1:
      return [1,i]
    elif board[1][i]==1 and board[2][i]==1:
      return [0,i]
      
  return -1
