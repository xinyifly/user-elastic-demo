import factory

from . import models


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    password = factory.PostGenerationMethodCall('set_unusable_password')
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    address = factory.Faker('address')
    birthday = factory.Faker('date_of_birth')
    description = factory.Faker('sentence')
