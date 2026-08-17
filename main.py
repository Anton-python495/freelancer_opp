from models import Freelancer, Client, Project
import json


if __name__ == '__main__':
    data = {
        'name': "Anton",
        "specialization": "Python Developer",
        "hourly_rate": 10,
        "completed_orders": 15
    }
    with open('data.json', 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)
        