class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # single list for 3x3 board
        self.current_winner = None # keep track of winner
