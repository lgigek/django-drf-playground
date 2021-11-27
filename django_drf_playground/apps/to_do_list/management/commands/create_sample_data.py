import logging

from django.core.management import BaseCommand

from django_drf_playground.apps.to_do_list.models import Task
from django_drf_playground.apps.to_do_list.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Creates some models for local development"

    def handle(self, *args, **options):
        logger.info("Starting creating sample data.")

        if User.objects.count() > 0:
            logger.info("There are already some data created, skipping process...")
            return

        logger.info("Creating models...")
        user_1 = User.objects.create(name="1st user", identifier="xpto_1")
        user_2 = User.objects.create(name="2nd user", identifier="xpto_2")
        user_3 = User.objects.create(name="3rd user", identifier="xpto_3")

        Task.objects.create(
            title="Draw project's architecture",
            description="Create some diagrams with project's tables, routes, etc.",
            user=user_1,
        )
        Task.objects.create(
            title="Setup django app",
            description="Install Django and add initial files to start project development.",
            user=user_2,
        )
        Task.objects.create(
            title="Create GET route for User",
            description="Create a GET route which allows fetching user data via api.",
            user=user_3,
        )
