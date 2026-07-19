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

def load_game(game):
    """Load a saved game into an exist Toukaygame"""
    
    try:
        with SAVE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        game.board.board = data["board"]

        game.player1.name = data["player1"]["name"]
        game.player1.score = data["player1"]["score"]

        game.player2.name = data["player2"]["name"]
        game.player2.score = data["player2"]["score"]

        if data["current_player"] == game.player1.name:
            game.current_player = game.player1
        else:
            game.current_player = game.player2

        last_player = data.get("last_capturing_player")

        if last_player == game.player1.name:
            game.last_capturing_player = game.player1

        elif last_player == game.player2.name:
            game.last_capturing_player = game.player2

        else:
            game.last_capturing_player = None

        game.game_over = data.get("game_over", False)

        print("Saved game loaded successfully.")
        return True

    except FileNotFoundError:
        print("No saved game was found.")
        return False

    except json.JSONDecodeError:
        print("The saved-game file contains invalid JSON.")
        return False

    except KeyError as error:
        print(f"The saved game is missing this information: {error}")
        return False

    except OSError as error:
        print(f"Unable to load the game: {error}")
        return False

