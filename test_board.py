import unittest
from board import Board

class TestBoard(unittest.TestCase):
    """Run test on the board"""

    def test_initial_board(self):
        """The board should be 2*6 with 4 stones in each cells"""

        board = Board()

        self.assertEqual(len(board.board), 6)

        for row in board.board:
            self.assertEqual(row,[4,4])

    def test_board_empty(self):
        """Identify if there is stones remained in board"""

        board = Board()

        self.assertFalse(board.board_empty())

        board.board = [
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0]
        ]

        self.assertTrue(board.board_empty())

    def test_legal_move(self):
        """Verify if a column has at least a stone in cell as  legal mov. """

        board = Board()

        self.assertTrue(board.legal_move(0))
        self.assertTrue(board.legal_move(1))

        board.board = [
            [3,0],
            [3,0],
            [1,0],
            [0,0],
            [0,0],
            [0,0]
        ]

        self.assertTrue(board.legal_move(0))
        self.assertFalse(board.legal_move(1))

if __name__ == "__main__":
    unittest.main()


