import pytest

from models import Freelancer, Client, Project

@pytest.fixture
def freelancer():
    return Freelancer('Anton', 'Python Developer', 5, 5)

@pytest.fixture
def client():
    return Client('Microsoft', 'client@gmail.com')

@pytest.fixture
def project(client, freelancer):
    return Project('Telegram bot', client, 1500, freelancer)