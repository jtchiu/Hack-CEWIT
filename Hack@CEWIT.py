from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('130.245.183.174',80)
db = client.pantry
ingredients = db.ingredients


@app.route('/')
def homeHelper():
    return redirect(url_for('home'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    ingredients_list = [ingredient['name'] for ingredient in ingredients.find()]

    return render_template("search.html",ingredients_list=ingredients_list)

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/home')
def home():
    return render_template("home.html")

#@app.route('/')


if __name__ == '__main__':
    app.run()
