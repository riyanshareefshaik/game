from flask import Flask, send_from_directory, jsonify, request
import os
import random

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "..", "public")

# ===================== GAME LOGIC =====================
def decide_winner(player_move, ai_move):
    """Determine winner between two moves"""
    if player_move == ai_move:
        return "DRAW"
    if (player_move == "ROCK" and ai_move == "SCISSORS") or \
       (player_move == "SCISSORS" and ai_move == "PAPER") or \
       (player_move == "PAPER" and ai_move == "ROCK"):
        return "PLAYER WINS"
    return "AI WINS"

# ===================== ROUTES =====================
@app.route("/")
def home():
    return send_from_directory(PUBLIC_DIR, "index.html")

@app.route("/api/play", methods=["POST"])
def play():
    """
    Play a round against the AI
    Expected JSON: {"player_move": "ROCK|PAPER|SCISSORS"}
    """
    try:
        data = request.json
        player_move = data.get("player_move", "").upper()

        # Validate move
        valid_moves = ["ROCK", "PAPER", "SCISSORS"]
        if player_move not in valid_moves:
            return jsonify({
                "error": f"Invalid move. Must be one of: {valid_moves}"
            }), 400

        # AI plays random move
        ai_move = random.choice(valid_moves)

        # Determine winner
        result = decide_winner(player_move, ai_move)

        return jsonify({
            "player_move": player_move,
            "ai_move": ai_move,
            "result": result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/ai-move", methods=["GET"])
def ai_move():
    """Get a random AI move"""
    moves = ["ROCK", "PAPER", "SCISSORS"]
    return jsonify({"ai_move": random.choice(moves)})

@app.route("/api/rules", methods=["GET"])
def rules():
    """Get game rules"""
    return jsonify({
        "rules": {
            "ROCK": "Beats SCISSORS",
            "PAPER": "Beats ROCK",
            "SCISSORS": "Beats PAPER"
        }
    })

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(PUBLIC_DIR, path)
