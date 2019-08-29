from celery import shared_task
from django.conf import settings
import requests


@shared_task
def save_user_to_elastic(user_dict):
    requests.put(settings.ELASTIC_URL +
                 '/users/_doc/{}'.format(user_dict.pop('id')),
                 json=user_dict)
