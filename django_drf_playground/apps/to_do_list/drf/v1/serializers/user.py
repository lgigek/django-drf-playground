from rest_framework import serializers

from django_drf_playground.apps.to_do_list.models import User


class FetchUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User.
    """

    class Meta:
        model = User
        fields = "__all__"
