from typing import Optional

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django_drf_playground.apps.to_do_list.drf.v1.serializers.user import FetchUserSerializer
from django_drf_playground.apps.to_do_list.models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.order_by("-created_at").all()

    def get_serializer_class(self):
        """
        Returns the correct serializer, given request's action.
        """
        request_action_to_serializer = {
            "retrieve": FetchUserSerializer,
            "list": FetchUserSerializer,
            "update": None,
            "destroy": None,
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

        response = super().list(request, *args, **kwargs)
        return response
