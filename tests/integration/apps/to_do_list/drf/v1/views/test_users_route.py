import uuid

import pytest

from rest_framework.response import Response
from rest_framework.test import APIClient

from django_drf_playground.apps.to_do_list.models import User
from tests.support.utils import create_user

ROUTE_URI = "/api/v1/users"


@pytest.mark.django_db
class TestRetrieve:
    def test_should_return_a_specific_user(self, api_client: APIClient):
        user_to_be_fetched = create_user()
        create_user()  # creating another user to guarantee that it doesn't return on the route

        response: Response = api_client.get(f"/api/v1/users/{user_to_be_fetched.id}")

        assert response.status_code == 200
        assert response.json()["id"] == str(user_to_be_fetched.id)
        assert response.json()["name"] == user_to_be_fetched.name
        assert response.json()["identifier"] == user_to_be_fetched.identifier

    def test_should_return_404_if_user_does_not_exist(self, api_client: APIClient):
        # creating some users
        create_user()
        create_user()

        response: Response = api_client.get(f"{ROUTE_URI}/{uuid.uuid4()}")

        assert response.status_code == 404


@pytest.mark.django_db
class TestList:
    def test_should_return_all_users(self, api_client: APIClient):
        user_1 = create_user()
        user_2 = create_user()

        response: Response = api_client.get(ROUTE_URI)

        assert response.status_code == 200
        assert len(response.json()) == 2

        user_ids = [user["id"] for user in response.json()]
        assert str(user_1.id) in user_ids
        assert str(user_2.id) in user_ids


@pytest.mark.django_db
class TestCreate:
    def test_should_return_201_and_return_created_user(self, api_client: APIClient):

        request_data = {"name": "Gigek", "identifier": "some_cool_and_unique_identifier"}

        response: Response = api_client.post(ROUTE_URI, request_data, format="json")

        assert response.status_code == 201
        assert User.objects.all().count() == 1

        created_user = User.objects.get()
        assert str(created_user.id) == response.json()["id"]
        assert created_user.name == request_data["name"]
        assert created_user.identifier == request_data["identifier"]

    def test_should_return_400_for_invalid_body(self, api_client: APIClient):

        request_data = {"invalid": "body"}

        response: Response = api_client.post(ROUTE_URI, request_data, format="json")

        assert response.status_code == 400
        assert User.objects.all().count() == 0

    def test_should_return_400_for_duplicated_identifier(self, api_client: APIClient):

        duplicated_identifier = "xpto"
        create_user(identifier=duplicated_identifier)
        request_data = {"name": "Gigek", "identifier": duplicated_identifier}

        response: Response = api_client.post(ROUTE_URI, request_data, format="json")

        assert response.status_code == 400
        assert User.objects.all().count() == 1  # from user previously created
