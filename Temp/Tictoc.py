""" Tic Tac Toe
----------------------------------------
"""
#Import the required libraries
#Import the required libraries
import random
#Import the required libraries
#Import the required libraries
import sys

board = [i for i in range(0, 9)]
player, computer = '', ''

moves = ((1, 7, 3, 9), (5, ), (2, 4, 6, 8))

winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))

tab = range(1, 10)


#Defining a function with name print_board
#Defining a function with name print_board
def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end += '---------\n'
        char = ' '
        if i in ('X', 'O'): char = i
        x += 1
        print(char, end=end)


#Defining a function with name select_char
#Defining a function with name select_char
def select_char():
    chars = ('X', 'O')
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


#Defining a function with name can_move
#Defining a function with name can_move
def can_move(brd, player, move):
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


#Defining a function with name can_win
#Defining a function with name can_win
def can_win(brd, player, move):
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x)
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


#Defining a function with name make_move
#Defining a function with name make_move
def make_move(brd, player, move, undo=False):
    #Trigger Function 'can_move' with parameters
    #Use conditional statement on parameters/check the options
    #Trigger Function 'can_move' with parameters
    #Use conditional statement on parameters/check the options
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        #Use conditional statement on parameters/check the options
        #Use conditional statement on parameters/check the options
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


#Defining a function with name computer_move
#Defining a function with name computer_move
def computer_move():
    move = -1

    #Trigger Function 'range' with parameters
    #Repeat action till iterator completes
    #Trigger Function 'range' with parameters
    #Repeat action till iterator completes
    for i in range(1, 10):
        #Trigger Function 'make_move' with parameters
        #Use conditional statement on parameters/check the options
        #Trigger Function 'make_move' with parameters
        #Use conditional statement on parameters/check the options
        if make_move(board, computer, i, True)[1]:
            move = i
            break
#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
    if move == -1:

        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        #Trigger Function 'range' with parameters
        #Repeat action till iterator completes
        for i in range(1, 10):
            #Trigger Function 'make_move' with parameters
            #Use conditional statement on parameters/check the options
            #Trigger Function 'make_move' with parameters
            #Use conditional statement on parameters/check the options
            if make_move(board, player, i, True)[1]:
                move = i
                break
#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
    if move == -1:

        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
#Trigger Function 'make_move' with parameters
#Trigger Function 'make_move' with parameters
    return make_move(board, computer, move)


#Defining a function with name space_exist
#Defining a function with name space_exist
def space_exist():
    return board.count('X') + board.count('O') != 9


player, computer = select_char()
#Trigger Function 'print' with parameters
#Trigger Function 'print' with parameters
print('Player is [%s] and computer is [%s]' % (player, computer))
result = '%%% Deuce ! %%%'
#Trigger Function 'space_exist' with parameters
#Repeat action till ###iterator### completes
#Trigger Function 'space_exist' with parameters
#Repeat action till ###iterator### completes
while space_exist():
    #Trigger Function 'print_board' with parameters
    #Trigger Function 'print_board' with parameters
    print_board()
    #Trigger Function 'print' with parameters
    #Trigger Function 'print' with parameters
    print('#Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    #Use conditional statement on parameters/check the options
    #Use conditional statement on parameters/check the options
    if not moved:
        #Trigger Function 'print' with parameters
        #Trigger Function 'print' with parameters
        print(' >> Invalid number ! Try again !')
        continue

#Use conditional statement on parameters/check the options
#Use conditional statement on parameters/check the options
    if won:
        result = '*** Congratulations ! You won ! ***'
        break
#Trigger Function 'computer_move' with parameters
#Use conditional statement on parameters/check the options
#Trigger Function 'computer_move' with parameters
#Use conditional statement on parameters/check the options
    elif computer_move()[1]:
        result = '=== You lose ! =='
        break
#Trigger Function 'print_board' with parameters
#Trigger Function 'print_board' with parameters
print_board()
#Trigger Function 'print' with parameters
#Trigger Function 'print' with parameters
print(result)
