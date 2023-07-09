from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe

# Create your tests here.

class Recipe_Tests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_Recipe = Recipe.objects.create(name='pasta', owner=testuser1, recipe_box="test desc ...")
        test_Recipe.save()

    def  Recipes_model(self):
        Recipe =  Recipe.objects.get(id=1)
        actual_owner= str(Recipe.owner)
        actual_name = str(Recipe.name)
        actual_recipe_box = str(Recipe.recipe_box)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"pasta")
        self.assertEqual(actual_recipe_box,"test desc ...")