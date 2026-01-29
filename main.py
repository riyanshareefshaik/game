#!/usr/bin/env python3
"""
Rock Paper Scissors Game - Main Entry Point
Runs the Flask app on Replit or local machine
"""
import os
from api.index import app

if __name__ == "__main__":
    # Get port from environment (Replit/Vercel sets this) or use 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Replit requires binding to 0.0.0.0
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"🎮 Starting Rock Paper Scissors Game on {host}:{port}")
    print(f"Visit http://localhost:{port} to play!")
    
    app.run(host=host, port=port, debug=False)
