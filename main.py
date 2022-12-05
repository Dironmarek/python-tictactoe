import library.functions as functions
import library.ai as ai
import tkinter as tk
turn = 0
counter = 0
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
flag_thing = True
root=tk.Tk()
root.geometry("300x300")
canvas=tk.Canvas(root, width=999, height=999)
canvas.pack()

#Runs when two player button is clicked
def twoPlayer(event):
  global turn
  global counter
  global menu_button
  global board
  global flag_thing
  flag = False
  for i in range(3):
    for j in range(3):
      if j == functions.get_cellpos(event)[0] and i == functions.get_cellpos(event)[1] and board[j][i]==0 and flag_thing:
        if turn == 0:
          canvas.create_line(100*i,100*j,100*(i+1),100*(j+1), fill="red", width=3)
          canvas.create_line(100*(i+1),100*j,100*i,100*(j+1), fill="red", width=3)
          board[j][i] = 1 #x
        else:
          canvas.create_oval(100*(i+1),100*j,100*i,100*(j+1), outline="blue",width=3)
          board[j][i] = 2 #o
        flag = True
        break
  if functions.detect_win(board) == 1:
    turn = 0
    counter = 0
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    flag_thing = False
    flag=False
    canvas.delete('all')
    canvas.create_text(150, 125, text="X wins", fill="black", font=('Helvetica 15 bold'))
    menu_button=tk.Button(root, text="Menu", command = menu)
    menu_button.place(x=120, y=150)
  elif functions.detect_win(board) == 2:
    turn = 0
    counter = 0
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    flag_thing = False
    flag=False
    canvas.delete('all')
    canvas.create_text(150, 125, text="O wins", fill="black", font=('Helvetica 15 bold'))
    menu_button=tk.Button(root, text="Menu", command = menu)
    menu_button.place(x=125, y=150)
  if counter == 8:
    turn = 0
    counter = 0
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    flag_thing = False
    flag=False
    canvas.delete('all')
    canvas.create_text(150, 120, text="Draw", fill="black", font=('Helvetica 15 bold'))
    menu_button=tk.Button(root, text="Menu", command = menu)
    menu_button.place(x=122, y=150)
  if flag:
    turn += 1
    turn %= 2
    counter += 1


#Runs when three player button is clicked
def onePlayer(event) :
  pass

#Sets up the tic-tac-toe board
def main():
  global flag_thing
  flag_thing = True
  canvas.delete('all')
  play1.place_forget()
  play2.place_forget()
  canvas.create_line(100,0,100,300, fill="black", width=3)  
  canvas.create_line(200,0,200,300, fill="black", width=3)
  canvas.create_line(0,100,300,100, fill="black", width=3)
  canvas.create_line(0,200,300,200, fill="black", width=3)


#Main menu when game is started
def menu():
  global play2
  global play1
  global menu_button
  canvas.delete('all')
  menu_button.place_forget()
  canvas.create_text(150,70, text="Menu", fill="black",font=('Helvetica 15 bold'))
  play2=tk.Button(root, text="Two Players", command = lambda:{main(),canvas.bind("<Button>", twoPlayer)})
  play2.place(x=103, y=90)
  play1=tk.Button(root, text="One Player", command = lambda:{main(),canvas.bind("<Button>", onePlayer)})
  play1.place(x=107,y=120)

canvas.delete('all')
menu_button=tk.Button(root, text="Menu", command = menu)
menu_button.place(x=120, y=150)
menu()
root.mainloop()

