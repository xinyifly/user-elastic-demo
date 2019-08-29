from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import UserFactory
from .models import User


class UserTest(TestCase):
    def test_create(self):
        UserFactory().save()
        self.assertTrue(User.objects.exists())


class UserAPITest(APITestCase):
    def test_index(self):
        UserFactory().save()
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        user = UserFactory.build()
        response = self.client.post(
            '/users/', {
                'password': "it's a secrect",
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'address': user.address,
                'birthday': user.birthday,
                'description': user.description,
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.exists())
