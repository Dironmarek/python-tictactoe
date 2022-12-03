#gets what cell is clicked depending on coordinate
def get_cellpos(event):
  if 0 < event.x < 100 and 0 < event.y < 100:
    return (0, 0)
  if 100 < event.x < 200 and 0 < event.y < 100:
    return (0, 1)
  if 200 < event.x < 300 and 0 < event.y < 100:
    return (0, 2)
  if 0 < event.x < 100 and 100 < event.y < 200:
    return (1, 0)
  if 100 < event.x < 200 and 100 < event.y < 200:
    return (1, 1)
  if 200 < event.x < 300 and 100 < event.y < 200:
    return (1, 2)
  if 0 < event.x < 100 and 200 < event.y < 300:
    return (2, 0)
  if 100 < event.x < 200 and 200 < event.y < 300:
    return (2, 1)
  if 200 < event.x < 300 and 200 < event.y < 300:
    return (2, 2)

#
def detect_win(board):
  if board[0] == [1, 1, 1] or board[1] == [1, 1, 1] or board[2] == [1, 1, 1]:
    return 1
  if board[0] == [2, 2, 2] or board[1] == [2, 2, 2] or board[2] == [2, 2, 2]:
    return 2
  if [board[i][0] for i in range(3)] == [1, 1, 1] or [board[i][1] for i in range(3)] == [1, 1, 1] or [board[i][2] for i in range(3)] == [1, 1, 1]:
    return 1
  if [board[i][0] for i in range(3)] == [2, 2, 2] or [board[i][1] for i in range(3)] == [2, 2, 2] or [board[i][2] for i in range(3)] == [2, 2, 2]:
    return 2
  if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
    return 1
  if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
    return 1
  if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
    return 1
  if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
    return 1



