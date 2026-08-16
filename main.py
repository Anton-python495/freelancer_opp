from models import Freelancer, Client, Project
import json


if __name__ == '__main__':
    anton = Freelancer('Anton', 'Python Developer', 5, 5)
    maria = Freelancer('Maria', 'Designer', 10, 10)
    alex = Freelancer('Alex', 'Python Developer', 15, 20)
    freelancers = [anton, maria, alex]
    data = anton.to_dict()
    with open("freelancer.json", 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    with open("freelancer.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    anton_loaded = Freelancer.from_dict(data)
    print(anton_loaded)

    data = [freelancer.to_dict() for freelancer in freelancers]
    with open("freelancers.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    with open("freelancers.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    loaded_freelancers = [Freelancer.from_dict(item) for item in data]
    print(*loaded_freelancers, sep='\n')