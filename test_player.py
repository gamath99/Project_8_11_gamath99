import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_add_score(self):
        player = Player("Player 1 ")
        player.add_score(4)
        self.assertEqual(player.score, 4)
        
if __name__ == "__main__":
    unittest.main()
