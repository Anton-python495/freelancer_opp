from models import Freelancer
from utils import save_json, load_json



if __name__ == '__main__':
    freelancers = [Freelancer("Anton", "Python Developer", 10, 15),
                   Freelancer("Maria", "Designer", 15, 20),
                   Freelancer("Alex", "Backend Developer", 25, 30)]
    
    data = [freelancer.to_dict() for freelancer in freelancers]

    save_json(data, "freelancers")

    loaded_data = load_json("freelancers")

    freelancers = [Freelancer.from_dict(data) for data in loaded_data]
    print(freelancers)
