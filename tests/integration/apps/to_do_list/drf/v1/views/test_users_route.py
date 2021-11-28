import uuid

import pytest

from rest_framework.response import Response
from rest_framework.test import APIClient

from tests.support.utils import create_user


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

        response: Response = api_client.get(f"/api/v1/users/{uuid.uuid4()}")

        assert response.status_code == 404


@pytest.mark.django_db
class TestList:
    def test_should_return_all_users(self, api_client: APIClient):
        user_1 = create_user()
        user_2 = create_user()

        response: Response = api_client.get(f"/api/v1/users")

        assert response.status_code == 200
        assert len(response.json()) == 2

        user_ids = [user["id"] for user in response.json()]
        assert str(user_1.id) in user_ids
        assert str(user_2.id) in user_ids
