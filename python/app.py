from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask with Docker - Secure Distroless Edition!"

@app.route('/version')
def version():
    return {
        "app": "secure-flask-app",
        "version": "distroless",
        "message": "This image has no shell access!"
    }

if __name__ == "__main__":
    # Never run in debug mode in production
    app.run(host="0.0.0.0", port=5000, debug=False)
