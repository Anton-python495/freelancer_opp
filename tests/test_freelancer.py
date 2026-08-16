from models.freelancer import Freelancer
from exceptions.errors import (InvalidRateError, InvalidOrderError, InvalidIncreaseError)
import pytest

def test_freelancer_creation():
    freelancer = Freelancer('Anton', 'Python Developer', 5, 5)

    assert freelancer.name == 'Anton'
    assert freelancer.specialization == 'Python Developer'
    assert freelancer.hourly_rate == 5
    assert freelancer.completed_orders == 5

def test_freelancer_to_dict():
    freelancer = Freelancer('Anton', 'Python Developer', 5, 5)

    data = freelancer.to_dict()

    assert data['name'] == 'Anton'
    assert data['specialization'] == 'Python Developer'
    assert data['hourly_rate'] == 5
    assert data['completed_orders'] == 5

def test_freelancer_from_dict():
    data = {'name': 'Anton', 'specialization': 'Python Developer', 'hourly_rate': 5, 'completed_orders': 5}

    freelancer = Freelancer.from_dict(data)

    assert freelancer.name == 'Anton'
    assert freelancer.specialization == 'Python Developer'
    assert freelancer.hourly_rate == 5
    assert freelancer.completed_orders == 5

def test_invalid_rate():
    with pytest.raises(InvalidRateError):
        Freelancer('Anton', 'Python Developer', 2, 5)

def test_invalid_order():
    with pytest.raises(InvalidOrderError):
        Freelancer('Anton', 'Python Developer', 5, -5)

def test_invalid_increase():
    freelancer = Freelancer('Anton', 'Python Developer', 5, 5)

    with pytest.raises(InvalidIncreaseError):
        freelancer.increase_rate(-10)

def test_rate_increase():
    freelancer = Freelancer('Anton', 'Python Developer', 5, 5)

    freelancer.increase_rate(10)

    assert freelancer.hourly_rate == 15
