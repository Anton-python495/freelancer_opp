from models import Freelancer
from utils import FreelancerManager



if __name__ == '__main__':
    anton = Freelancer("Anton", "Python Developer", 5, 5)
    maria = Freelancer("Maria", 'Designer', 10, 15)

    manager = FreelancerManager()

    manager.add_freelancer(anton)
    manager.add_freelancer(maria)

    print(manager.freelancers)
    anton = manager.get_freelancer("Anton")
    print(anton)

    anton = manager.update_freelancer("Anton", 10)
    print(anton)

    manager.save("freelancers")
    manager.load("freelancers")
    manager1 = manager
    print(manager1.freelancers)