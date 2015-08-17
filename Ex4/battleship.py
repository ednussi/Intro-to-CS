#############################################################
# FILE: battleship.py
# WRITER: Eran Nussinovitch a.k.a ednussi
# EXERCISE : intro2cs ex4 2013-2014
# Description
# A FULL WORKING BATTLE SHIP CODE
#############################################################

MINIMUM_WIDTH = 1
MINIMUM_HEIGHT = 1
MINIMUM_SHIP_LENGTH = 1
MINIMIMAL_BOARD_PLACE = 0

############################# Assignment 4 ####################################
"""Implement the following function according the description in ex4"""


# The function which creates the game board
def new_board(width = 10 , height = None):
      
    # checks the inputs.
    if height==None: # in case user didn't enter height uses defalut
        height = width
    if width < MINIMUM_WIDTH or height < MINIMUM_HEIGHT:
        return None
    
    # creates the game board.
    board=[]
    for colums in range(0,height):
        board.append(None)
        temp_list=[]
        for rows in range(0,width):
            temp_list.append(None)
            board[colums]=(temp_list.copy())
    return board

    """creates a new board game for a Battleship game.

    Args:
    -width: a positive int - the width of the board - default value 10
    -height: a positive int - the height of the board - if not spcified
    should be as width

    return: a NEW enpty board - each inner arrays is a list of 'None's.

    n case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    
# A function which places the ship on the board
def place_ship(board,ship_length,bow,ship_direction):
    
    # checking inputs
    if (ship_length < MINIMUM_SHIP_LENGTH or bow[0] < MINIMIMAL_BOARD_PLACE
        or bow[1] < MINIMIMAL_BOARD_PLACE or bow[0] >= len(board[0]) or
        bow[1] >= len(board)):
        return None
    if (ship_direction != (1,0) and ship_direction != (-1,0) and
        ship_direction != (0,1) and ship_direction != (0,-1)):
        return None
    
    # checking if ship is placeable
    if ship_direction[0] == 0:
        
        # north/south check
        if ((bow[1] + 1  - (ship_length * ship_direction [1])) < 0 or
            (bow[1] - (ship_length * ship_direction [1])) > len(board)):
            return None
    else:
        
        # east/west check
        if ((bow[0] + 1  - (ship_length * ship_direction [0])) < 0 or
            (bow[0] - (ship_length * ship_direction [0])) > len(board[0])):
            return None
            
    # checking if the cells are empty
    check_place = bow  
    if board[bow[1]][bow[0]] == None:
        for ta in range(0,ship_length):
            
            # checks north / south cells
            if ship_direction[0] == 0:
                if board[bow[1] -(ta * ship_direction[1])][bow[0]] != None:
                    return None
                
            # checks east / west cells
            if ship_direction[1] == 0:
                if board[bow[1]][(bow[0]-(ta * ship_direction[0]))] != None:
                    return None
    else:
        return None

    # finding the highest index of a ship on board
    max_index = 0
    for colums in range(0,len(board)):
        for rows in range(0,len(board[0])):    
            if board[colums][rows] != None:
                if board[colums][rows][0] > max_index:
                    
                    # validating max index is the heighest index of a ship
                    max_index = board[colums][rows][0]
                    
    # giving it its new value
    max_index += 1
        
    # creating a pointer to be appointed later in order to chnage
    # the remainning size of a ship in case it gets "hit"
    size_pointer = [ship_length]
    
    # entering a ship
    for draw_cell in range(0,ship_length):

        # entering a ship to north / south from original bow
        if ship_direction[0] == 0:
            board[bow[1] -(
                draw_cell * ship_direction[1])][bow[0]] =  (
                    max_index, draw_cell, size_pointer)
            
        # entering a ship to east / west from original bow
        if ship_direction[1] == 0:
            board[bow[1]][bow[0]-(
                draw_cell * ship_direction[0])] =  (
                    max_index, draw_cell, size_pointer)
            
    # returning the index of the last ship entered
    return max_index

"""Put a new ship on the board

    put a new ship (with unique index) on the board.
    in case of successful placing edit the board according to the definitions
    in the ex description.

    Args:
    -board - battleshipe board - you can assume its legal
    -ship_length: a positive int the length of the ship
    -bow: a tuple of ints the index of the ship's bow
    -ship_direction: a tuple of ints representing the direction the ship
    is facing (dx,dy) - should be out of the 4 options(E,N,W,S):
    (1,0) -facing east, rest of ship is to west of bow,
    (0,-1) - facing north, rest of ship is to south of bow, and etc.

    return: the index of the placed ship, if the placement was successful,
    and 'None' otherwise.

    In case of bad input: values are out of range returns None

     You can assume the board is legal. You can assume the other inputs
     are of the right form. You need to check that they are legal."""
    
# A function which gives the user to ability to hit the placed ships
def fire(board,target):
    
    # checks if shot is valid
    if target[1] < MINIMIMAL_BOARD_PLACE or target[1] >= len(board):
        return None
    if target[0] < MINIMIMAL_BOARD_PLACE or target[0] >= len(board[0]):
        return None
    
    # logic of a valid shot
    if board[target[1]][target[0]]==None:
        
        # if missing the shot
        hit = False
        ship = 0
        return (hit,ship)
    else:

        # if hitting a ship
        hit = True
        
        # logic of ship destraction
        board[target[1]][target[0]][2][0] -= 1 # decreasing size of ship

        # returning 0 or ship index if it was hit or destryoed
        ship = 0
        if board[target[1]][target[0]][2][0]==0:
            ship = board[target[1]][target[0]][0]  
        board[target[1]][target[0]] = None 
        return(hit,ship)

    
    """implement a fire in battleship game

    Calling this function will try to destroy a part in one of the ships on the
    board. In case of successful fire destroy the relevant part
    in the damaged ship by deleting it from the board. deal also with the case
    of a ship which was completely destroyed

    -board - battleshipe board - you can assume its legal
    -target: a tuple of ints (x,y) indices on the board
    in case of illegal target return None

    returns: a tuple (hit,ship), where hit is True/False depending if the the
    shot hit, and ship is the index of the ship which was completely
    destroyed, or 0 if no ship was completely destroyed. or 0 if no ship
    was completely destroyed.

    Return None in case of bad input

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""
