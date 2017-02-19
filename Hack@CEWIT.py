from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from python.Recipe import recipe_from_dict
import requests
import json

app = Flask(__name__)


@app.route('/')
def homeHelper():
    return redirect(url_for('home'))

@app.route('/ingredients', methods=["POST"])
def ingredients():
    client = MongoClient('130.245.183.174', 80)
    db = client.pantry
    ingredients = db.ingredients

    ingredients_list = request.get_json()
    ingredients_list = ingredients_list['ingredients'].split(';')

    new_ingredients = [{"name":x} for x in ingredients_list]
    new_ingredients = new_ingredients[0:len(new_ingredients)-1]
    ingredients.insert_many(new_ingredients)

@app.route('/index')
def index():
    client = MongoClient('130.245.183.174', 80)
    db = client.pantry
    ingredients = db.ingredients

    ingredients_list = ','.join(ingredient['name'] for ingredient in ingredients.find())
    number_of_ingredients = len(ingredients_list.split(','))
    r = requests.post('http://food2fork.com/api/search', data={'key': 'f04d32b283259970d11efb96b6ef215a', 'q': ingredients_list})
    r = r.content.decode('utf-8')
    r = json.loads(r)

    r["recipes"] = r["recipes"][:4]

    recipe_list = []

    for recipe in r["recipes"]:
        r = requests.post('http://food2fork.com/api/get',
                          data={'key': 'f04d32b283259970d11efb96b6ef215a', 'rId': recipe['recipe_id']})
        r = r.content.decode('utf-8')
        r = json.loads(r)
        r = r['recipe']
        recipe_dict = {
            'f2f_url': r['f2f_url'],
            'ingredients': r['ingredients'],
            'recipe_id': r['recipe_id'],
            'image_url': r['image_url'],
            'num_items': len(r['ingredients']),
            'percentage' : int(((number_of_ingredients/len(r['ingredients']))*100)),
            'title': r['title']
        }
        recipe_list.append(recipe_dict)

    recipe_list.sort(key=lambda x: x['num_items'])
    # recipes = [recipe_from_dict(x) for x in recipe_list]
    return render_template("index.html", recipe_list=recipe_list)

@app.route('/search')
def search():
    client = MongoClient('130.245.183.174', 80)
    db = client.pantry
    ingredients = db.ingredients

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
