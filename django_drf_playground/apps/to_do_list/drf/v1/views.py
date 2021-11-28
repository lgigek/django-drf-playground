import logging

from typing import Optional

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django_drf_playground.apps.to_do_list.drf.v1.serializers.user import CreateUserSerializer
from django_drf_playground.apps.to_do_list.drf.v1.serializers.user import FetchUserSerializer
from django_drf_playground.apps.to_do_list.models import User

logger = logging.getLogger(__name__)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.order_by("-created_at").all()

    def get_serializer_class(self):
        """
        Returns the correct serializer, given request's action.
        """
        request_action_to_serializer = {
            "retrieve": FetchUserSerializer,
            "list": FetchUserSerializer,
            "create": CreateUserSerializer,
        }

        return request_action_to_serializer[self.action]

    def retrieve(self, request: Request, pk: Optional[str] = None, *args, **kwargs) -> Response:
        """
        Gets the data of a specific user.

        It expects:
        - GET as http method;
        - The ID specified on the url;

        It returns:
        - HTTP status = 200;
        - A JSON like this:
            {
              "id": "b5c63e6b-fd88-475e-9d17-c3109f79eb85",
              "created_at": "2021-11-27T22:46:52.453886Z",
              "updated_at": "2021-11-27T22:46:52.453918Z",
              "name": "1st user",
              "identifier": "xpto_1"
            }
        """

        logger.info("Received a request to fetch a specific User")

        response = super().retrieve(request, pk, *args, **kwargs)
        return response

    def list(self, request: Request, *args, **kwargs) -> Response:
        """
        Gets the data of several users.

        It expects:
        - GET as http method;

        It returns:
        - HTTP status = 200;
        - A JSON like this:
            [
              {
                "id": "f0b5beaf-2df7-4793-abb1-04303940b169",
                "created_at": "2021-11-27T22:46:52.448449Z",
                "updated_at": "2021-11-27T22:46:52.448504Z",
                "name": "1st user",
                "identifier": "xpto_1"
              },
              ...
            ]
        """

        logger.info("Received a request to fetch a list of Users")

        response = super().list(request, *args, **kwargs)
        return response

    def create(self, request: Request, *args, **kwargs) -> Response:
        """
        Creates a User.

        It expects:
        - POST as http method;
        - A JSON like this:
            {
                "name": "some name",
                "identifier": "some unique identifier"
            }

        It returns:
        - HTTP status = 201;
        - A JSON like this:
            [
              {
                "id": "f0b5beaf-2df7-4793-abb1-04303940b169",
                "created_at": "2021-11-27T22:46:52.448449Z",
                "updated_at": "2021-11-27T22:46:52.448504Z",
                "name": "some name",
                "identifier": "some unique identifier"
              },
              ...
            ]
        """

        request_data = request.data
        logger.info("Received a request with the following data: %s", request_data)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request_data)

        logger.info("Checking if received data is valid.")
        if not serializer.is_valid():
            logger.warning("Received a request without valid body, returning 400.")
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

        logger.info("Received data is valid, proceeding with User creation.")
        user = serializer.create(serializer.validated_data)

        logger.info("Everything went good, returning 201!")
        return Response(status=status.HTTP_201_CREATED, data=user)
