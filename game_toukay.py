""" Project 2
Gama Mathurin 
The count and capture Game 
The game consists in collecting more points (stones) then the opponents while moving the points (stones) in a clockwise way from a board 2*6. 
The Player scores by adding a point in a 3 point cell, 
but he can only capture the stones if the last distributed point drop in the 3 point cell. 

"""
from board import Board
from player import Player
from save_load import save_game, load_game, save_result

def start_menu(game):
    """Allow the user to start or load a game."""

    while True:
        print("\nTOUKAY")
        print("1. New game")
        print("2. Load saved game")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            if load_game(game):
                return True

        elif choice == "3":
            print("Goodbye.")
            return False

        else:
            print("Choose 1, 2, or 3.")

class Toukay_game:
    """Initialize the game, distribute points"""

    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        
        self.current_player = self.player1  # Start with player 1

        self.last_capturing_player = None
        self.quit_requested = False


        self.game_over = False

    def switch_player(self):
        """Switch the current player"""
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def get_player_move(self):
        """Get the player's move (row and column)"""
        while True:
            choice = input("Enter row (0-5), S to save, or Q to quit:").strip().lower()

            if choice == "s":
                save_game(self)
                continue

            if choice == "q":
                save_game(self)
                self.quit_requested = True
                print("The game was saved before exiting.")
                self.game_over = True
                return None
            
            try:
                row = int(choice)
                
                if 0 <= row < 6 :
                    return row
                else:
                    print("Invalid input. Please enter valid row.")
            except ValueError:
                print("Enter a row number, S, or Q.")    

    def play(self):
        # Implement the main game loop here
        while not self.game_over:
            
            self.board.display_board()

            print(f"{self.current_player.name}'s turn.")
            print("\nScore:")
            print(f"{self.player1.name}: {self.player1.score}"
                  )
            print(f"{self.player2.name}: {self.player2.score}")

            #End when the entire board is empty
            if self.board.board_empty():
                self.game_over =True
                break

            #Determine the current player's column
            col = 0
            if self.current_player == self.player1:
                col = 0  # Player 1 chooses column 0
            else:
                col = 1  # Player 2 chooses column 1
            
            if not self.board.legal_move(col):
                print(f"{self.current_player.name} has no legal move.")
                remaining_stones = self.board.count_remaining_stones()

                if remaining_stones == 4: 
                    if self.last_capturing_player is None:
                        raise RuntimeError("Four stones remain, but no capturing player was recorded.")
                        
                    self.last_capturing_player.add_score(4)
                    print(f"The final stones go to {self.last_capturing_player.name}.")

                    self.board.clear_board()
                    self.game_over = True
                    break
                

                self.switch_player()
                continue
            
            row = self.get_player_move()

            if row is None:
                break
            

            if self.board.board[row][col] == 0:
                print("That cell is empty Choose another cell.")
                continue

           
            captured_points = self.board.distribute_stones(row, col)


            if captured_points > 0 :
                self.current_player.add_score(captured_points)

                self.last_capturing_player = self.current_player
                                
                if self.board.board_empty():
                    self.game_over = True
                else:
                    print(f"{self.current_player.name} receives "
                      "a free turn"
                      )
                continue

            if self.board.board_empty():
                self.game_over = True
            else:
                self.switch_player()
        if not self.quit_requested:
            self.show_results()

    def show_results(self):
        print("\nGame Over")
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")

        if self.player1.score > self.player2.score: 
            print("Player 1 wins!")
        elif self.player2.score > self.player1.score:
            print("Player 2 wins!")
        else:
            print("The game is a draw.")

        save_result(self)

                    
    

if __name__ == "__main__":
    game = Toukay_game()

    if start_menu(game):
        game.play()  # Start the game loop