from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .tasks import save_user_to_elastic


@receiver(post_save, sender=User)
def user_post_save(**kwargs):
    user = kwargs.get('instance')
    save_user_to_elastic.delay({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'address': user.address,
        'birthday': user.birthday.isoformat(),
        'description': user.description,
    })
