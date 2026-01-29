# 🎮 Rock Paper Scissors Game - Web Version

An interactive Rock Paper Scissors game with Flask backend and HTML frontend.

## Play Online
- **Vercel**: https://game-rho-opal.vercel.app
- **Replit**: Deploy your own instance (see below)

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

Then visit: `http://localhost:5000`

## Deploy to Vercel

1. Push to GitHub
2. Visit https://vercel.com/new
3. Import your GitHub repository
4. Vercel auto-detects Python and deploys!

## Deploy to Replit

1. Click **Import from GitHub** on Replit.com
2. Enter: `https://github.com/riyanshareefshaik/game`
3. Click **Import**
4. Replit auto-runs and provides a live URL

## API Endpoints

- `GET /` - Game UI
- `POST /api/play` - Play a round
  - Request: `{"player_move": "ROCK|PAPER|SCISSORS"}`
  - Response: `{"player_move": "...", "ai_move": "...", "result": "..."}`
- `GET /api/ai-move` - Get random AI move
- `GET /api/rules` - Get game rules

## How to Play

1. Click Rock 🪨, Paper 📄, or Scissors ✂️
2. AI plays randomly
3. Winner is displayed
4. Stats saved in browser

## Files

- `api/index.py` - Flask application
- `main.py` - Entry point
- `public/index.html` - Game UI
- `rpc.py` - Original desktop version
- `vercel.json` - Vercel config
- `.replit` - Replit config
