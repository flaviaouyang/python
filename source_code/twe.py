# thisdict = {'language':'python',
#            'difficulty':'easy',
#            'is_fun':True}
# print(thisdict)

board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}

print(board['top-l'])

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])
print("Our board will look like this:")
printBoard(board)
print()
print()
print()
move = 'top-l'; input("Enter your move: ")
print()
print()
print()
print()
print()
print()
print("Now it will look something like this")
print("Enter your move: top-l")
print()

turn = "X"
board[move] = turn
printBoard(board)
print()
print()
print()
print()
