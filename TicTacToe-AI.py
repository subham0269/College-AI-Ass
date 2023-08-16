#Tictactoe AI
import random

board = [' ' for i in range (9)]
boardPosList=[1,2,3,4,5,6,7,8,9]

def boardPrint(board):
  z=0
  print()
  for i in range(3):
    for j in range(3):
      if(j==2):
        print(board[z],end="")
        z+=1
      else:
        print(board[z],end="|")
        z+=1
    print()
    if(i!=2):
      print("-----")
  print()


def compInput(board, posList):
  if posList:
    randPosition = random.choice(posList)
    insertInBoard(board, randPosition, 'O')
    return checkIfWin(board, 'O')
  else:
    return 0  

def userInput(posL):
  uInp=int(input("Enter a position: "))
  if uInp not in posL:
    print("Enter position that is empty")
    userInput(posL)
  else:
    insertInBoard(board, uInp, 'X')
    return checkIfWin(board, 'X')
    
def insertInBoard(board,inpPosition, char):
  board[inpPosition-1] = char
  boardPosList.remove(inpPosition)
  return 1

def checkIfWin(board, char):
  #row checking
  if (board[0]==char and board[1]==char and board[2]==char):
    return True
  elif (board[3]==char and board[4]==char and board[5]==char):
    return True
  elif (board[6]==char and board[7]==char and board[8]==char):
    return True
    
  #column
  elif (board[0]==char and board[3]==char and board[6]==char):
    return True
  elif (board[1]==char and board[4]==char and board[7]==char):
    return True
  elif (board[2]==char and board[5]==char and board[8]==char):
    return True

  #diagonal
  elif (board[2]==char and board[4]==char and board[6]==char):
    return True
  elif (board[0]==char and board[4]==char and board[8]==char):
    return True
  else:
    return False

print("TicTacToe")
print()
print("X for User")
print("O for Computer")
boardPrint(board)
while(1):
  if not boardPosList:
    break
  if userInput(boardPosList):
    print("User Won")
    boardPrint(board)
    print("---------------------")
    break
  else:
    print("after user input")
    boardPrint(board)
    if compInput(board, boardPosList):
      print("Computer Won")
      boardPrint(board)
      print("-------------------")
      break
    print("after computer input")
    boardPrint(board)
