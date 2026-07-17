class Player:
    """Initialize the player with a name and score"""
    
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        """Add points to the player's score"""
        self.score += points
        