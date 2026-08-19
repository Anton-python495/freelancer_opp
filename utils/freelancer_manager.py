from utils import save_freelancers, load_freelancers

class FreelancerManager:

    def __init__(self):
        self.freelancers = []

    def add_freelancer(self, freelancer):
        self.freelancers.append(freelancer)

    def get_freelancer(self, name):
        for freelancer in self.freelancers:
            if freelancer.name == name:
                return freelancer
        return None

    def update_freelancer(self, name, new_rate):
        for freelancer in self.freelancers:
            if freelancer.name == name:
                freelancer.hourly_rate = new_rate
                return freelancer
        return None

    def delete_freelancer(self, name):
        for freelancer in self.freelancers:
            if freelancer.name == name:
                self.freelancers.remove(freelancer)
                return freelancer
        return None

    def save(self, filename):
        save_freelancers(self.freelancers, filename)

    def load(self, filename):
        self.freelancers = load_freelancers(filename)