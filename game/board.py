from game import game_manager

board = [0 for i in range(9)]

def clear():
    global board
    board = [0 for i in range(9)]

def press_square(box_number,symbol):
    board[box_number-1]=symbol

def check_if_pressed(box_number):
    if board[box_number-1]:
        return True
    return False

def get_board():
    global board
    return board

def check_win():
    for i in range(0,9,3):
        if all((board[i],board[i+1],board[i+2])) and board[i]==board[i+1]==board[i+2]:
            return True
        
    for i in range(3):
        if all((board[i],board[i+3],board[i+6])) and board[i]==board[i+3]==board[i+6]:
            return True
        
    if all((board[0],board[4],board[8])) and board[0]==board[4]==board[8]:
        return True
    
    if all((board[2],board[4],board[6])) and board[2]==board[4]==board[6]:
        return True
    
    else:
        return False

def is_full():
    return True if all(board) else False
    
