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
