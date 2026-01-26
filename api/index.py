from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(
        os.path.join(os.getcwd(), "public"),
        "index.html"
    )

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(
        os.path.join(os.getcwd(), "public"),
        path
    )
