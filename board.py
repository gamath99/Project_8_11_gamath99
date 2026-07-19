class Board:
    """initialize the board with 2 columns and 6 rows, each cell containing 4 seeds"""

    def __init__(self):
        self.board = [ #create the 2*6 board with one column for each player and a row for each cell
            [4,4],
            [4,4],
            [4,4],
            [4,4],
            [4,4],
            [4,4]
        ]

        self.path =[
            (0,0),
            (0,1),
            (1,1),
            (2,1),
            (3,1),
            (4,1),
            (5,1),
            (5,0),
            (4,0),
            (3,0),
            (2,0),
            (1,0)
        ]
    
    def display_board(self):
        # Display the initial board 
        print("\nToukay Board")
        print("------------------------------")
        print("|Row|       |P1|       |P2|")
        
        for i in range(len(self.board)):
            print("------------------------------")
            print("|",i,"|", "    ", "|",self.board[i][0],"|", "    ", "|",self.board[i][1],"|")
            print("------------------------------")

    def board_empty(self):
        """Check if the board is empty"""
        for row in self.board:
            if any(cell > 0 for cell in row):
                return False
        return True
    
    def distribute_stones(self, start_row, start_col):
        """Distribute stones from the selected cell in a clockwise manner"""
        current_row = start_row
        current_col = start_col

        while True:

            stones = self.board[current_row][current_col]
            self.board[current_row][current_col] = 0  # Remove all stones from the selected cell

            current_index = self.path.index((current_row, current_col))
            last_cell_was_empty = False

            while stones > 0: 
                current_index = (current_index + 1) % len(self.path)
                row, col = self.path[current_index]
                
                was_empty = self.board[row][col] == 0  #check the cell before placing the stone

                self.board[row][col] += 1
                stones -= 1

                if stones == 0: 
                    last_cell_was_empty = was_empty

            if self.board[row][col] == 4:  # Check if the last cell has 3 stones
                self.board[row][col] = 0  # Remove the stones from the cell

                print(f"Captured 4 stones from {row}, column {col}.")
                return 4

            if last_cell_was_empty:
                return 0  # Return the last cell where a stone was dropped          
            current_row = row
            current_col = col 


          
    
    
    
