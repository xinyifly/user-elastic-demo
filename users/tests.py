from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from unittest import mock

from .factories import UserFactory
from .models import User
from .tasks import save_user_to_elastic


class UserTest(TestCase):
    def test_create(self):
        UserFactory().save()
        self.assertTrue(User.objects.exists())

    @mock.patch('requests.put')
    def test_save_to_elastic(self, mock_put):
        user = UserFactory()
        user.save()
        save_user_to_elastic({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': user.address,
            'birthday': user.birthday.isoformat(),
            'description': user.description,
        })
        mock_put.assert_called_once()


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

    @mock.patch('requests.post')
    def test_search(self, mock_post):
        mock_post.return_value.status_code = status.HTTP_200_OK
        response = self.client.get('/search/')
        mock_post.assert_called_once()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.has_header('X-Total-Count'))
