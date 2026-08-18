from models import Freelancer
from utils.json_manager import save_json, load_json



if __name__ == '__main__':
    data = {
        'name': "Anton",
        "specialization": "Python Developer",
        "hourly_rate": 10,
        "completed_orders": 15
    }
    save_json(data, 'data')

    loaded_data = load_json('data')

    freelancer = Freelancer.from_dict(loaded_data)
    print(freelancer.info())