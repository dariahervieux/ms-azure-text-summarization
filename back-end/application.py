from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from computer_vision.read_text import ReadText

# 'app' is a standard name for Flask app object
app = Flask(__name__)
app.config.from_object('config.Config')

"""Application entry point"""
@app.route("/")
def index():
   return render_template("index.html")


UPLOAD_ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
"""Starts the flow: uploading file, returns unique id to follow the process"""    
@app.route("/start", methods = ['POST'])
def start():
   if request.method == 'POST':
      f = request.files['file']
      file_name = secure_filename(f.filename)
      f.save(secure_filename(f.filename))
      reader = ReadText()
      return reader.read(file_name)