import numpy as np
import random
from enum import Enum

class Hit(Enum):
    NO_HIT = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

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
        self.board = [[1 if i == 0 or i == 10 else 0  for i in range(11)] for _ in range(20)]
        self.board.append([1 for _ in range(11)]) # padding down
        self.board = np.array(self.board)

    def _insert_piece(self):
        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                self.board[self.y+row][self.x+col] ^= self.cur_piece[row][col]
        print(self.board)

    def _remove_piece(self):
        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                self.board[self.y+row][self.x+col] = 0

    def can_draw(self, x, y, checkLeft=False):
        for row in range(len(self.cur_piece)):
            for col in range(len(self.cur_piece[0])):
                if self.cur_piece[row][col] == 1:
                    if (row == len(self.cur_piece) - 1 or self.cur_piece[row + 1][col] == 0):
                        if self.board[row + y][col + x] == 1:
                            return Hit.DOWN

                        '''
                        if (col == 0 or col == len(self.cur_piece[0]) - 1 or self.cur_piece[row][col + 1] == 0):
                            if self.board[row + y][col + x] == 1:
                                return Hit.SIDE 
                        '''

                        if checkLeft:
                            if col == 0 or self.cur_piece[row][col - 1] == 0:
                                if self.board[row + y][col + x] == 1:
                                    return Hit.LEFT
                        else:
                            if col == len(self.cur_piece[0]) - 2 or self.cur_piece[row][col + 1] == 0:
                                if self.board[row + y][col + x] == 1:
                                    return Hit.RIGHT

        return Hit.NO_HIT

    
    def rotate_piece(self):
        if self.cur_piece_index == 1: # if square don't do anything
            return 

        self._remove_piece()
        self.cur_piece = np.rot90(self.cur_piece, -1)
        self._insert_piece()

    def move_down_piece(self):
        if self.can_draw(self.x, self.y+1) == 1: 
            self.new_next_piece()
            self._insert_piece()

        self._remove_piece()
        self.y += 1
        self._insert_piece()

    def move_right_piece(self):
        print(self.can_draw(self.x + 1, self.y, False))
        if self.can_draw(self.x + 1, self.y, False) == Hit.RIGHT:
            return

        self._remove_piece()
        self.x += 1
        self._insert_piece()

    def move_left_piece(self):
        if self.can_draw(self.x - 1, self.y, True) == Hit.LEFT:
            return

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

