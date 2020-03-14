from django.urls import reverse
import pytest
from unittest import mock

@mock.patch("aula10.context_processors.total_pets")
def test_status_code(mock_total_pets, client):
    mock_total_pets.return_value = {"total_pet": 3}
    response = client.get(reverse("aula10"))
    assert response.status_code == 200