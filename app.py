from flask import Flask, flash, jsonify
from flask import render_template
from flask import request, redirect, url_for, session
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'many random bytes'


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()