
class Recipe():
    def __init__(self, title, recipe_id, image_url, f2f_url):
        self = title
        self = recipe_id
        self = image_url
        self = f2f_url


def recipe_from_dict(dict):
    return Recipe(dict['title'], dict['recipe_id'], dict['image_url'], dict['f2f_url'])