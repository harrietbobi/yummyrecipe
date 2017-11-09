
""" This module contains various objects  for the recipe app """


class User:
    ''' This class describes the user model '''

    def __init__(self, name, username, password):
        self.username = name
        self.username = username
        self.password = password
        self.categories = {}

    def add_category(self, title):
        """ Adds a new category to the users category"""
        if title not in self.categories and title != "":
            self.categories[title] = Category(title)
            return True
        return False

    def edit_category(self, title, newtitle):
        ''' updates the category with  newtitle'''
        if title in self.categories:
            self.categories[newtitle] = self.categories.pop(title)
            return True
        return False

    def delete_category(self, title):
        """ deletes an existing category"""
        if title in self.categories:
            self.categories.pop(title)
            return True
        return False


class Category:
    """ descibe the category model """

    def __init__(self, title):
        self.title = title
        self.recipes = {}

    def add_recipe(self, description):
        """ Adds a new recipe to the categories"""
        if description not in self.recipes and description != "":
            self.recipes[description] = Recipe(description)
            return True
        return False

    def edit_recipe(self, description, new_description):
        ''' update an existing recipe with a new one'''
        if description in self.recipes:
            self.recipes[new_description] = self.recipes.pop(description)
            return True
        return False

    def delete_recipe(self, description):
        """ deletes an existing recipe """
        if description in self.recipes:
            self.recipes.pop(description)
            return True
        return False


class Recipe:
    """describe the recipe model """

    def __init__(self, description):
        self.recipe_description = description
