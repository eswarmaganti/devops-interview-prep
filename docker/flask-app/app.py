from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  print("Successfully Started the Flask App")
  return render_template('index.html')