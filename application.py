from flask import Flask
# 'app' is a standard name for Flask app object
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"