import random
import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ===================== GAME LOGIC =====================
def get_gesture(fingers):
    """Convert finger array to gesture"""
    if fingers == [0, 0, 0, 0, 0]:
        return "ROCK"
    if fingers == [1, 1, 1, 1, 1]:
        return "PAPER"
    if fingers == [0, 1, 1, 0, 0]:
        return "SCISSORS"
    return "UNKNOWN"

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
@app.route("/", methods=["GET"])
def home():
    # Serve the HTML file from public directory
    try:
        with open(os.path.join(os.path.dirname(__file__), '../public/index.html'), 'r') as f:
            return f.read(), 200, {'Content-Type': 'text/html'}
    except:
        return jsonify({
            "message": "AI Rock Paper Scissors Game API",
            "endpoints": {
                "/": "Home",
                "/play": "POST - Submit your move",
                "/ai-move": "GET - Get AI's random move"
            }
        })

@app.route("/play", methods=["POST"])
def play():
    """
    POST endpoint to play a round
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

@app.route("/ai-move", methods=["GET"])
def ai_move():
    """Get a random AI move"""
    moves = ["ROCK", "PAPER", "SCISSORS"]
    return jsonify({"ai_move": random.choice(moves)})

@app.route("/rules", methods=["GET"])
def rules():
    """Get game rules"""
    return jsonify({
        "rules": {
            "ROCK": "Beats SCISSORS",
            "PAPER": "Beats ROCK",
            "SCISSORS": "Beats PAPER"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
