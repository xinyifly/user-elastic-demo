from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'id', 'password', 'username', 'first_name', 'last_name',
            'address', 'birthday', 'description'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    username = serializers.RegexField(
        r'^[a-z0-9_-]+$',
        min_length=4,
        validators=[UniqueValidator(queryset=User.objects.all())],
        error_messages={
            'invalid': 'Ensure this field has only lower case characters.'
        })
    first_name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
