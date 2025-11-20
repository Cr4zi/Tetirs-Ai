import numpy as np
import random

class Tetris:
    def __init__(self):
        self._init_game()
        self.pieces = [[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]], # line
                                [[1,1], [1,1]], # square
                                [[0,1,0], [1,1,0], [0,1,0]], # t shaped
                                [[0,0,1], [0,1,1], [0,1,0]], # S shaped
                                [[1,0,0], [1,1,0], [0,1,0]], # Reversed S
                                [[0,1,0], [0,1,0], [0,1,1]], # L 
                                [[0,1,0], [0,1,0], [1,1,0]], # Reversed L
                                ]

        self.x = 4
        self.y = 0
        self.cur_piece_index = random.randint(0, len(self.pieces)-1)
        self.cur_piece = np.array(self.pieces[self.cur_piece_index])
        self.next_piece_index = random.randint(0, len(self.pieces)-1)
        self.next_piece = np.array(self.pieces[self.next_piece_index])
        self._insert_piece()


    def _init_game(self):
        self.board = np.array([[0 for _ in range(10)] for _ in range(20)])

    def _insert_piece(self):
        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                if(self.board[self.y+row][self.x+col] == 1 and self.cur_piece[row][col] == 1):
                    return

        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                self.board[self.y+row][self.x+col] ^= self.cur_piece[row][col]

    def _remove_piece(self):
        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                self.board[self.y+row][self.x+col] = 0
    
    def rotate_piece(self):
        if self.cur_piece_index == 1: # if square don't do anything
            return 

        self._remove_piece()
        self.cur_piece = np.rot90(self.cur_piece, -1)
        self._insert_piece()

    def move_down_piece(self):
        # if hit floor
        if self.y + len(self.cur_piece) == len(self.board):
            self.new_next_piece()
            self._insert_piece()
            return

        self._remove_piece()
        self.y += 1
        self._insert_piece()

    def move_right_piece(self):
        self._remove_piece()
        self.x += 1
        self._insert_piece()

    def move_left_piece(self):
        self._remove_piece()
        self.x -= 1
        self._insert_piece()

    def new_next_piece(self):
        self.x = 4
        self.y = 0

        self.cur_piece_index = self.next_piece_index
        self.cur_piece = np.array(self.pieces[self.cur_piece_index])
        self.next_piece_index = random.randint(0, len(self.pieces)-1)
        self.next_piece = np.array(self.pieces[self.next_piece_index])

    def agent_random_move(self):
        pass

