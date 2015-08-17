#############################################################
# FILE: GetToTheZero.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex5 2013-2014
# Description:
# A function which checks a given row with numbers
# represnting the amount of jumps i can do to a previous or next
# cell in the board, if it is solveable
#############################################################

FIRST_CELL_IN_BOARD = 0
def is_solvable(start, board):

    # checks if the starting position is within the range of list
    if start < FIRST_CELL_IN_BOARD or start > (len(board)-1):
        return False
    else:
        #calls the actual recursive function
        moving_list = []
        for cell in range(len(board)):
            moving_list.append(False)
    return james_on_the_move(start, board, moving_list)

# The recursive function which makes Bond's moves
def james_on_the_move(start, board, moving_list):
    # We Got to the zero !
    if start == len(board)-1:
        return True
    
    # checks if your move is out of the list size
    if start >= len(board) or start < FIRST_CELL_IN_BOARD:
        return False
    
    # checks if i already been in this cell
    if moving_list[start] == True:
        return False
    
    # conclusion - we are not in the right place and we can make a valid move
    # mark the cell we are on
    moving_list[start] = True
    return james_on_the_move(start+board[start], board, moving_list) or (
        james_on_the_move(start-board[start], board, moving_list))
