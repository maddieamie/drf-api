from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snake


class SnakeTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        cls.testuser1.save()

        cls.test_snake = Snake.objects.create(
            name="Slithers",
            owner=cls.testuser1,
            description="A little danger noodle without the danger.",
            color="A tortoiseshell pattern of brown and gold.",
            breed="boa"
        )
        cls.test_snake.save()

    def setUp(self):
        # Force authenticate the test user for each test
        self.client.force_authenticate(user=self.testuser1)

    def test_snake_model(self):
        snake = Snake.objects.get(id=1)
        actual_owner = str(snake.owner)
        actual_name = str(snake.name)
        actual_description = str(snake.description)
        actual_color = str(snake.color)
        actual_breed = str(snake.breed)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Slithers")
        self.assertEqual(
            actual_description, "A little danger noodle without the danger."
        )
        self.assertEqual(actual_color, "A tortoiseshell pattern of brown and gold.")
        self.assertEqual(actual_breed, "boa")

    def test_get_snake_list(self):
        url = reverse("snake_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snakes = response.data
        self.assertEqual(len(snakes), 1)
        self.assertEqual(snakes[0]["name"], "Slithers")

    def test_get_snake_by_id(self):
        url = reverse("snake_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snake = response.data
        self.assertEqual(snake["name"], "Slithers")

    def test_create_snake(self):
        url = reverse("snake_list")
        data = {
            "owner": self.testuser1.id,  # Use the authenticated user's ID
            "name": "Spoon",
            "description": "Always picking stuff up and curling up.",
            "color": "A silver snake",
            "breed": "magic"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        snakes = Snake.objects.all()
        self.assertEqual(len(snakes), 2)
        self.assertEqual(Snake.objects.get(id=2).name, "Spoon")

    def test_update_snake(self):
        url = reverse("snake_detail", args=(1,))
        data = {
            "owner": self.testuser1.id,  # Use the authenticated user's ID
            "name": "Slithers",
            "description": "Old slitherlegs.",
            "color": "Copper and gold.",
            "breed": "fancy boa."
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snake = Snake.objects.get(id=1)
        self.assertEqual(snake.name, data["name"])
        self.assertEqual(snake.owner.id, data["owner"])
        self.assertEqual(snake.description, data["description"])
        self.assertEqual(snake.color, data["color"])
        self.assertEqual(snake.breed, data["breed"])

    def test_delete_snake(self):
        url = reverse("snake_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        snakes = Snake.objects.all()
        self.assertEqual(len(snakes), 0)
