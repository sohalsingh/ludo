import random

# Class representing a Ludo game
class LudoGame:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.players = ['Red', 'Green', 'Yellow', 'Blue']
        self.player_positions = {'Red': [], 'Green': [], 'Yellow': [], 'Blue': []}
        self.current_player = None

    def setup(self):
        random.shuffle(self.players)
        self.current_player = self.players[0]

    def roll_dice(self):
        return random.randint(1, 6)

    def move(self, player, piece, steps):
        if player != self.current_player:
            print("It's not your turn!")
            return
        
        if steps == 6 and len(self.player_positions[player]) == 0:
            self.player_positions[player].append(piece)
        elif piece in self.player_positions[player]:
            current_position = self.player_positions[player].index(piece)
            new_position = current_position + steps
            if new_position < len(self.board):
                self.player_positions[player][current_position] = new_position
            else:
                print("Invalid move!")
                return
        else:
            print("Invalid move!")
            return

        self.current_player = self.players[(self.players.index(player) + 1) % len(self.players)]

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    print('.', end=' ')
                elif self.board[i][j] == 1:
                    print('R', end=' ')
                elif self.board[i][j] == 2:
                    print('G', end=' ')
                elif self.board[i][j] == 3:
                    print('Y', end=' ')
                elif self.board[i][j] == 4:
                    print('B', end=' ')
            print()

# Usage example
game = LudoGame()
game.setup()
game.print_board()

while True:
    player = game.current_player
    roll = game.roll_dice()
    print(f"{player} rolled a {roll}.")

    piece = input("Enter piece number (1-4): ")
    game.move(player, int(piece), roll)

    game.print_board()
    print()

    if len(game.player_positions[player]) == 4:
        print(f"{player} wins!")
        break
