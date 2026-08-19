from models import Freelancer
from utils import save_json, load_json

def save_freelancers(freelancers, filename):
    data = [freelancer.to_dict() for freelancer in freelancers]
    save_json(data, filename)

def load_freelancers(filename):
    loaded_data = load_json(filename)
    freelancers = [Freelancer.from_dict(data) for data in loaded_data]
    return freelancers

