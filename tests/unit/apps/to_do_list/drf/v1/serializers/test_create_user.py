import pytest

from rest_framework.exceptions import ValidationError

from django_drf_playground.apps.to_do_list.drf.v1.serializers.user import CreateUserSerializer
from django_drf_playground.apps.to_do_list.models import User
from tests.support.utils import create_user


@pytest.mark.django_db
class TestValidateIdentifier:
    def test_should_return_value_if_unique(self):
        unique_identifier = "xpto"
        assert CreateUserSerializer.validate_identifier(unique_identifier) == unique_identifier

    def test_should_raise_if_duplicated(self):
        duplicated_identifier = "xpto"
        create_user(identifier=duplicated_identifier)

        with pytest.raises(ValidationError, match="This field must be unique."):
            CreateUserSerializer.validate_identifier(duplicated_identifier)


@pytest.mark.django_db
class TestCreate:
    def test_should_create_user(self):
        data_to_be_created = {"name": "Gigek", "identifier": "some_unique_identifier"}

        serializer = CreateUserSerializer(data=data_to_be_created)
        serializer.is_valid()

        serializer.create(serializer.validated_data)

        assert User.objects.all().count() == 1

        created_user = User.objects.get()
        assert created_user.name == data_to_be_created["name"]
        assert created_user.identifier == data_to_be_created["identifier"]


class TestUpdate:
    def test_should_raise_not_implemented(self):
        serializer = CreateUserSerializer(data={})

        with pytest.raises(NotImplementedError):
            serializer.update(None, None)
