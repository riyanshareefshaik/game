from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def decide_winner(player_move, ai_move):
    if player_move == ai_move:
        return "DRAW"
    if (player_move == "ROCK" and ai_move == "SCISSORS") or \
       (player_move == "SCISSORS" and ai_move == "PAPER") or \
       (player_move == "PAPER" and ai_move == "ROCK"):
        return "PLAYER WINS"
    return "AI WINS"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "API running"})

@app.route("/api/play", methods=["POST"])
def play():
    data = request.get_json()
    player_move = data.get("player_move", "").upper()

    valid = ["ROCK", "PAPER", "SCISSORS"]
    if player_move not in valid:
        return jsonify({"error": "Invalid move"}), 400

    ai_move = random.choice(valid)
    result = decide_winner(player_move, ai_move)

    return jsonify({
        "player_move": player_move,
        "ai_move": ai_move,
        "result": result
    })

# ❌ DO NOT use app.run() on Vercel
