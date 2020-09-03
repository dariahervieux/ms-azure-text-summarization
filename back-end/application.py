from flask import Flask, render_template
# 'app' is a standard name for Flask app object
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

    
@app.route("/text")
def hello():
    return jsonify({'text':'Hello World!'})