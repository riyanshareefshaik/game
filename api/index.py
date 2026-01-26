from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(BASE_DIR, "..", "public")

@app.route("/")
def home():
    return send_from_directory(PUBLIC_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(PUBLIC_DIR, path)
