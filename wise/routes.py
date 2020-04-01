from . import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')