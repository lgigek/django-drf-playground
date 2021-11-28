import uuid

from django_drf_playground.apps.to_do_list.models import User


def create_user(**kwargs) -> User:
    return User.objects.create(
        name=kwargs.get("name", "default name"), identifier=kwargs.get("identifier") or str(uuid.uuid4())
    )
