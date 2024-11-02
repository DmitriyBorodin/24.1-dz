from datetime import timedelta

from celery import shared_task
import logging
from django.utils import timezone
from users.models import User

logger = logging.getLogger(__name__)


@shared_task()
def deactivate_user():
    today = timezone.now().today().date()
    delta = today - timedelta(days=30)
    users = User.objects.filter(is_active=True, last_login__lt=delta)
    logger.info(users)
    if users:
        for user in users:
            user.is_active = False
            user.save()
            logger.info(user)
