from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def homeHelper():
    return redirect(url_for('home'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/search')
def search():

    return render_template("search.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/home')
def home():
    return render_template("home.html")

#@app.route('/')


if __name__ == '__main__':
    app.run()
