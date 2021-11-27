import logging

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Creates super user for local development"

    def handle(self, *args, **options):
        user_model = get_user_model()

        username = "admin"
        password = "test"
        email = ""

        if user_model.objects.filter(username=username).count() == 0:
            logger.info("Superuser created.")
            user_model.objects.create_superuser(username, email, password)

        else:
            logger.info("Superuser creation skipped.")
