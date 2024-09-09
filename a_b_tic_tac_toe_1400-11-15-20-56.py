def Print(board):
    for i in range(1,10):
        print(board[i], end='')
        if i%3 == 0:
            print()
            print('------')
            #print()
        else :
            print(end='|')



def Insert(letter, position):
    if board[position] == ' ':
        board[position] = letter
        Print(board)
        if (Draw()):
            print("Draw!")
            quit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                quit()
            else:
                print("Player wins!")
                quit()

        return


    else:
        print("Can't insert there!")
        position = int(input("enter new position:  "))
        Insert(letter, position)
        return


def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def whoWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def Draw():
    for key in keys:
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    print()
    position = int(input(f"Enter the position for '{player}':  "))
    Insert(player, position)
    return


def compMove():
    bestScore = -2
    bestMove = 0
    for key in keys:
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, alpha , beta , False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    Insert(bot, bestMove)
    return


def minimax(board, depth, alpha , beta ,  Max):
    if (whoWon(bot)):
        return 1
    elif (whoWon(player)):
        return -1
    elif (Draw()):
        return 0

    if (Max):
        bestScore = -2
        for key in keys:
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, alpha , beta , False)
                board[key] = ' '
                bestScore = max(score , bestScore)
                alpha = max(alpha , score)
                if alpha >= beta :
                    break
        return bestScore

    else:
        bestScore = 2
        for key in keys:
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, alpha , beta, True)
                board[key] = ' '
                bestScore = min(score , bestScore)
                beta = min(beta, score)
                if alpha >= beta:
                    break
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

keys = board.keys()

alpha = -2
beta = 2

print("Can't win LOL :)")
global firstMove


firstMove = int(input("who play first? '0 bot first --- 1 you first' :  "))
if (firstMove == 0 or firstMove == 1) :
    pass
else:
    firstMove = int(input("invalid number ! ' 0 bot first --- 1 you first ' :  "))

player = 'O'
bot = 'X'




while not checkWin():
    if firstMove:
        playerMove()
        compMove()
    else:
        compMove()
        playerMove()
