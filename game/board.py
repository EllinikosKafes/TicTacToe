from game import game_manager


class Board:

    def __init__(self):
        self.board = [0 for i in range(9)]

    def clear(self):
        self.board = [0 for i in range(9)]

    def press_square(self,box_number,symbol):
        self.board[box_number-1]=symbol

    def check_if_pressed(self,box_number):
        if self.board[box_number-1]:
            return True
        return False

    def get_board(self):
        return self.board

    def check_win(self):
        for i in range(0,9,3):
            if all((self.board[i],self.board[i+1],self.board[i+2])) and self.board[i]==self.board[i+1]==self.board[i+2]:
                return True
            
        for i in range(3):
            if all((self.board[i],self.board[i+3],self.board[i+6])) and self.board[i]==self.board[i+3]==self.board[i+6]:
                return True
            
        if all((self.board[0],self.board[4],self.board[8])) and self.board[0]==self.board[4]==self.board[8]:
            return True
        
        if all((self.board[2],self.board[4],self.board[6])) and self.board[2]==self.board[4]==self.board[6]:
            return True
        
        else:
            return False

    def is_full(self):
        return True if all(self.board) else False
    
