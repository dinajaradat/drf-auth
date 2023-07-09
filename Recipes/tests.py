from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Recipe


class ThingTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Recipe.objects.create(
            name="rake",
            owner=testuser1,
            recipe_box="Better for collecting leaves than a shovel.",
        )
        test_thing.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_Recipe_model(self):
        Recipe = Recipe.objects.get(id=1)
        actual_owner = str(Recipe.owner)
        actual_name = str(Recipe.name)
        actual_recipe_box = str(Recipe.recipe_box)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_recipe_box, "Better for collecting leaves than a shovel."
        )

    # def test_get_Recipe_list(self):
    #     url = reverse("Recipe_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     Recipes = response.data
    #     self.assertEqual(len(Recipes), 1)
    #     self.assertEqual(Recipes[0]["name"], "rake")

    # def test_get_Recipe_by_id(self):
    #     url = reverse("Recipe_detail", args=(1,))
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     Recipe = response.data
    #     self.assertEqual(Recipe["name"], "rake")

    # def test_create_Recipe(self):
    #     url = reverse("Recipe_list")
    #     data = {"owner": 1, "name": "spoon", "description": "good for cereal and soup"}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     Recipes = Recipe.objects.all()
    #     self.assertEqual(len(Recipes), 2)
    #     self.assertEqual(Recipe.objects.get(id=2).name, "spoon")

    # def test_update_Recipe(self):
    #     url = reverse("Recipe_detail", args=(1,))
    #     data = {
    #         "owner": 1,
    #         "name": "rake",
    #         "description": "pole with a crossbar toothed like a comb.",
    #     }
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     Recipe = Recipe.objects.get(id=1)
    #     self.assertEqual(Recipe.name, data["name"])
    #     self.assertEqual(Recipe.owner.id, data["owner"])
    #     self.assertEqual(Recipe.recipe_box, data["recipe_box"])

    # def test_delete_Recipe(self):
    #     url = reverse("Recipe_detail", args=(1,))
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     Recipes = Recipe.objects.all()
    #     self.assertEqual(len(Recipes), 0)

    # # class 32
    # def test_authentication_required(self):
    #     self.client.logout()
    #     url = reverse("Recipe_list")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)