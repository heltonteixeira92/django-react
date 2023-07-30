import pytest

from customers.models import Customers


@pytest.mark.django_db
def test_list_customers(client):
    resp = client.get('/api/customers/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_create_customer(client):
    data = {
        "first_name": "Customer 096",
        "last_name": "Customer 096",
        "email": "customer096@email.com",
        "phone": "123456789",
        "address": "Customer 096 Address",
        "description": "Customer 096 description"
    }

    resp = client.post('/api/customers/', data=data, content_type="application/json")
    assert resp.status_code == 201


@pytest.mark.django_db
def test_update_customer(client):
    data = {"id": 1,
            "first_name": "Customer 155",
            "last_name": "Customer 155",
            "email": "customer155@email.com",
            "phone": "123456789",
            "address": "Customer 0155 Address",
            "description": "Customer 0155 description"
            }

    resp = client.put('/api/customers/1/', data=data, content_type="application/json")
    assert resp.status_code == 200

