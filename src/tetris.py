import numpy as np

class Tetris:
    def __init__(self):
        self._init_game()
        self.pieces = np.array([[[1,1,1,1]], # line
                                [[1,1], [1,1]], # square
                                [[0,1], [1,1], [0,1]], # t shaped
                                [[0,1], [1,1], [1,0]], # S shaped
                                [[1,0], [1,1], [0,1]], # Reversed S
                                [[1,0], [1,0], [1,1]], # L 
                                [[0,1], [0,1], [1,1]], # Reversed L
                                ])
        self.cur_piece = np.random.choice(self.pieces)
        self.next_piece = np.random.choice(self.pieces)


    def _init_game(self):
        self.board = np.array([[0 for _ in range(10)] for _ in range(24)])

    def insert_piece(self, x, y, piece):
        pass

    def rotate_piece(self, x, y, piece):
        pass

    def move_piece(self, x, y, piece):
        pass

    def new_next_piece(self):
        self.cur_piece = self.next_piece
        self.next_piece = np.random.choice(self.pieces)

    def agent_random_move(self):
        pass

