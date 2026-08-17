from models import Client

def test_client_creation(client):
    assert client.name == "Microsoft"
    assert client.email == "client@gmail.com"

def test_to_dict(client):
    data = {'name': client.name, 'email': client.email}
    assert data == {'name':'Microsoft', 'email':'client@gmail.com'}