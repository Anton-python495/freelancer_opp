from models import Freelancer, Client, Project
from exceptions import InvalidRateError, InvalidOrderError, InvalidIncreaseError
import pytest

@pytest.mark.parametrize(
        "rate",
        [
            5,
            10,
            50,
            100
        ]
)
def test_valid_rate(rate):
    freelancer = Freelancer('Anton', 'Python Developer', rate, 5)

    assert freelancer.hourly_rate == rate

def test_freelancer_creation(freelancer):
    assert freelancer.name == 'Anton'
    assert freelancer.specialization == 'Python Developer'
    assert freelancer.hourly_rate == 5
    assert freelancer.completed_orders == 5

def test_freelancer_to_dict(freelancer):
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

def test_rate_increase(freelancer):
    freelancer.increase_rate(10)

    assert freelancer.hourly_rate == 15

def test_complete_orders(freelancer):
    freelancer.complete_orders(3)

    assert freelancer.completed_orders == 8

def test_calculate_income(freelancer):
    hours = 5

    assert freelancer.calculate_income(hours) == 25

def test_add_project(freelancer, project):
    freelancer.add_project(project)

    assert freelancer.projects == [project]

def test_get_project_count(freelancer, project):
    assert freelancer.get_project_count() == 0

    freelancer.add_project(project)

    assert freelancer.get_project_count() == 1 