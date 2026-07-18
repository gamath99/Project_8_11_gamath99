""" Project 2
Gama Mathurin 
The count and capture Game 
The game consists in collecting more points (stones) then the opponents while moving the points (stones) in a clockwise way from a board 2*6. 
The Player scores by adding a point in a 3 point cell, 
but he can only capture the stones if the last distributed point drop in the 3 point cell. 

"""
from board import Board
from player import Player

class Toukay_game:
    """Initialize the game, distribute points"""

    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        
        self.current_player = self.player1  # Start with player 1

    def switch_player(self):
        """Switch the current player"""
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_player_move(self):
        """Get the player's move (row and column)"""
        while True:
            try:
                row = int(input("Enter the row (0-5): "))
                


                if 0 <= row < 6 :
                    return row
                else:
                    print("Invalid input. Please enter valid row.")
            except ValueError:
                print("Invalid input. Please enter integers for row.")    

    def play(self):
        # Implement the main game loop here
        while not self.game_over:
            
            self.board.display_board()

            print(f"{self.current_player.name}'s turn."
                  f"Score: {self.current_player.score}"
                  )
            row = self.get_player_move()
            col = 0
            if self.current_player == self.player1:
                col = 0  # Player 1 chooses column 0
            else:
                col = 1  # Player 2 chooses column 1



            


        pass



if __name__ == "__main__":
    game = Toukay_game()
    game.play()  # Start the game loop