import pprint
import sys

# cat = {'size': 'big', 'color': 'gray', 'temperament': 'gentle'}
# print(cat)
# print(cat['size'])

# print(cat['gray'])
# you can access value through keys, but not the other way around


# for i in cat.values():
#     print (i)
# # output:
# # big
# # gray
# # gentle

# for i in cat.keys():
#     print(i)
# # output:
# # size
# # color
# # temperament

# for i in cat.items():
#     print(i)
# # output
# # ('size', 'big')
# # ('color', 'gray')
# # ('temperament', 'gentle')

# for i, j in cat.items():
#     print("key: ", i, " value: ", j)
# # output:
# # key:  size  value:  big
# # key:  color  value:  gray
# # key:  temperament  value:  gentle

# print(cat.keys())
# # output:
# # dict_keys(['size', 'color', 'temperament'])
# print(list(cat.keys()))
# # output:
# # ['size', 'color', 'temperament']

# print('big' in cat)
# # output:
# # False

# print('size' in cat)
# # output:
# # True

# print('big' in cat.values())
# # output:
# # True

# print("The cat is ", cat.get('size', 'undetermined in terms of size'), ".")
# # output:
# # The cat is  big .

# print("The cat is ", cat.get('breed', 'undetermined in terms of breed'), ".")
# # output:
# # The cat is  undetermined in terms of breed .

# cat.setdefault('breed', 'english short hair')
# print(cat.get('breed', 'failed'))
# # output:
# # english short hair
# print(cat.setdefault('breed', 'english short hair'))
# # output:
# # english short hair

# cat.setdefault('color', 'red')
# print(cat.get('color','color DNE'))
# # output:
# # gray
# print(cat.setdefault('color', 'red'))
# # output:
# # gray

# message = 'Someone will remember us, I say. Even in another time.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)

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
        # print(sym, " won!")
        return 1
    if board['mid-l'] == sym and board['mid-m'] == sym and board['mid-r'] == sym:
        # print(sym, " won!")
        return 1
    if board['bot-l'] == sym and board['bot-m'] == sym and board['bot-r'] == sym:
        # print(sym, " won!")
        return 1
    if board['top-l'] == sym and board['bot-l'] == sym and board['mid-l'] == sym:
        # print(sym, " won!")
        return 1
    if board['top-m'] == sym and board['bot-m'] == sym and board['mid-m'] == sym:
        # print(sym, " won!")
        return 1
    if board['top-r'] == sym and board['bot-r'] == sym and board['mid-r'] == sym:
        # print(sym, " won!")
        return 1
    if board['top-l'] == sym and board['mid-m'] == sym and board['bot-r'] == sym:
        # print(sym, " won!")
        return 1
    if board['top-r'] == sym and board['bot-l'] == sym and board['mid-m'] == sym:
        # print(sym, " won!")
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

         
