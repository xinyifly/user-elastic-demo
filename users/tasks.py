from celery import shared_task
from celery.exceptions import Reject
from django.conf import settings
import requests


@shared_task(acks_late=True)
def save_user_to_elastic(user_dict):
    try:
        requests.put(settings.ELASTIC_URL +
                     '/users/_doc/{}'.format(user_dict['id']),
                     json=user_dict)
    except Exception as exc:
        raise Reject(exc)
