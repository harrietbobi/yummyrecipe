import unittest
from models import User,Category,Recipe

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Harriet", "har@gmail.com", "password")

   
    def test_add_category(self):
        self.assertEqual( self.user.add_category("dinner"),
                        True)

    def test_add_category_name_already_exists(self):
        self.user.add_category("dinner")
        self.assertEqual( self.user.add_category
                         ("dinner"),
                         False)


    def test_edit_category_not_found(self):
        self.assertEqual( self.user.edit_category("absent", "newtype"),
                         False)

    def test_edit_category_successful(self):
        self.user.add_category("Snacks")
        self.assertEqual( self.user.edit_category("Snacks","local foods"),True)
        
    def test_delete_category_not_found(self):
        self.assertEqual( self.user.delete_category("not exist"), False)

    def test_delete_category_deleted(self):
        self.user.add_category("lunch recipes")
        self.assertEqual( self.user.delete_category("lunch recipes"),
                         True)
        
    
class Recipe_categoryTest(unittest.TestCase):
    
    def setUp(self):
        self.recipes = Category("title")

    
    def test_add_recipe_added(self):
        self.assertEqual(self.recipes.add_recipe('description'), True)

    def test_add_recipe_exists(self):
        self.recipes.add_recipe('description')
        self.assertEqual(self.recipes.add_recipe('description'), False)

    def test_edit_recipe_not_found(self):
        self.assertEqual(self.recipes.edit_recipe(
            'description', 'new_description'), False)

   
    def test_edit_recipe_edited_succesfully(self):
         self.recipes.add_recipe('description')
         self.assertEqual(self.recipes.edit_recipe( 'description', 'new_description'), True)

    def test_delete_recipe_not_found(self):
        self.assertEqual(self.recipes.delete_recipe('description'), False)

    def test_recipe_deleted(self):
        self.recipes.add_recipe('description')
        self.assertEqual(self.recipes.delete_recipe('description'), True)

class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe("description")


    def test_create_item_instance(self):
        self.assertIsInstance(self.recipe, Recipe, "Failed to create instance")
