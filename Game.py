import time

class TicTacToe:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

        self.player_turn = 'X'


    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # Checks if the move is legal
    def is_valid(self, x_coord, y_coord):
        if x_coord < 0 or x_coord > 2 or y_coord < 0 or y_coord > 2:
            return False
        elif self.current_state[x_coord][y_coord] != '.':
            return False
        else:
            return True


    def is_terminated(self):
        # Check vertically
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Check horizontally
        for i in range(0, 3):
            if self.current_state[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.current_state[i] == ['O', 'O', 'O']:
                return 'O'

        # Check diagonally
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[1][1] == self.current_state[2][2]):
            return self.current_state[0][0]

        if (self.current_state[0][2] != '.' and
                self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '.'):
                    return None

        # Tie
        return '.'



