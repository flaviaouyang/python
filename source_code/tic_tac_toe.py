import sys

# create a board as a dictionary 
board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}

turn = "X"


def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])

def win(board, sym):
    if board['top-l'] == sym and board['top-m'] == sym and board['top-r'] == sym:
        return 1
    if board['mid-l'] == sym and board['mid-m'] == sym and board['mid-r'] == sym:
        return 1
    if board['bot-l'] == sym and board['bot-m'] == sym and board['bot-r'] == sym:
        return 1
    if board['top-l'] == sym and board['bot-l'] == sym and board['mid-l'] == sym:
        return 1
    if board['top-m'] == sym and board['bot-m'] == sym and board['mid-m'] == sym:
        return 1
    if board['top-r'] == sym and board['bot-r'] == sym and board['mid-r'] == sym:
        return 1
    if board['top-l'] == sym and board['mid-m'] == sym and board['bot-r'] == sym:
        return 1
    if board['top-r'] == sym and board['bot-l'] == sym and board['mid-m'] == sym:
        return 1

count = 0
printBoard(board)
while count < 9:
    move = input("Enter your move: ")
    if turn == "O":
        turn = "X"
    else:
        turn = "O"
    board[move] = turn
    printBoard(board)
    count += 1
    if win(board, turn) == 1:
        print(turn, " won!")
        sys.exit()
    continue