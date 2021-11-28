import logging

from typing import Dict
from typing import Optional

from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_drf_playground.apps.to_do_list.models import User

logger = logging.getLogger(__name__)


class FetchUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User.
    """

    class Meta:
        model = User
        fields = "__all__"


class CreateUserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)
    identifier = serializers.CharField(max_length=50, allow_null=False, allow_blank=False)

    @staticmethod
    def validate_identifier(value: str) -> Optional[str]:
        """
        Validates if "identifier" field is unique.
        """
        logger.info("Validating if identifier is unique")

        if User.objects.filter(identifier=value).exists():
            raise ValidationError("This field must be unique.")

        return value

    def create(self, validated_data: Dict) -> Dict:
        """
        Creates an user on database.
        """
        logger.info("Creating user on database.")

        with transaction.atomic():
            user = User.objects.create(name=validated_data["name"], identifier=validated_data["identifier"])

        logger.info("User was created successfully!")
        user_data = user.__dict__
        user_data.pop("_state")  # removing model's internal stuff
        return user_data

    def update(self, instance, validated_data):
        logger.error("Update not available on this serializer.")
        raise NotImplementedError
