import json
from datetime import datetime
from pathlib import Path

SAVE_FILE = Path(__File__).parent / "savegame.json"
RESULTS

def save_game(game):
    """Save the current Toukay game to a JSON file."""

    data = {
        "board": game.board.board,
        "player1": {
            "name": game.player1.name,
            "score": game.player1.score
        },
        "player2": {
            "name": game.player2.name,
            "score": game.player2.score
        },
        "current_player": game.current_player.name,
        "last_capturing_player": (
            game.last_capturing_player.name
            if game.last_capturing_player is not None
            else None
        ),
        "game_over": game.game_over
    }

    try:
        with SAVE_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Game saved successfully.")

    except OSError as error:
        print(f"Unable to save the game: {error}")