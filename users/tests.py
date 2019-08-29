from django.test import TestCase

from .factories import UserFactory
from .models import User


class UserTest(TestCase):
    def test_create(self):
        UserFactory().save()
        self.assertTrue(User.objects.exists())
