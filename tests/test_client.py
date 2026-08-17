from models import Client

def test_client_creation(client):
    assert client.name == "Microsoft"
    assert client.email == "client@gmail.com"
