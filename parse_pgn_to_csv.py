import chess.pgn
import pandas as pd

# Open the PGN file (make sure it's inside Data/ folder)
pgn = open("Data/chess_com_games_2025-09-17 (1).pgn", encoding="utf-8", errors="ignore")

games_data = []

while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    
    game_info = {
        "Date": game.headers.get("UTCDate", ""),
        "White": game.headers.get("White", ""),
        "Black": game.headers.get("Black", ""),
        "Result": game.headers.get("Result", ""),
        "Opening": game.headers.get("Opening", ""),
        "TimeControl": game.headers.get("TimeControl", ""),
        "Termination": game.headers.get("Termination", ""),
        "NumMoves": len(list(game.mainline_moves()))
    }
    games_data.append(game_info)

# Convert to DataFrame
df = pd.DataFrame(games_data)

# Save as CSV inside Outputs/ folder
df.to_csv("Outputs/divya_games.csv", index=False)

print("✅ PGN parsed and saved as Outputs/divya_games.csv")