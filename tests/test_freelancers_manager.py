from models import Freelancer
from utils import FreelancerManager

def test_add_freelancer():
    manager = FreelancerManager()
    freelancer = Freelancer("Anton", "Python Developer", 5, 5)
    manager.add_freelancer(freelancer)
    assert len(manager.freelancers) == 1
    assert manager.freelancers[0] == freelancer

def test_get_freelancer():
    anton = Freelancer("Anton", "Python Developer", 5, 5)
    maria = Freelancer("Maria", "Designer", 10, 15)

    manager = FreelancerManager()

    manager.add_freelancer(anton)
    manager.add_freelancer(maria)
  
    result = manager.get_freelancer("Anton")
    assert result == anton
    result = manager.get_freelancer("Maria")
    assert result == maria
    result = manager.get_freelancer("Vasia")
    assert result is None

def test_update_freelancer():
    anton = Freelancer("Anton", "Python Developer", 5, 5)

    manager = FreelancerManager()
    manager.add_freelancer(anton)

    new_anton = manager.update_freelancer("Anton", 15)
    unknown = manager.update_freelancer("Vasia", 20)

    assert new_anton.hourly_rate == 15
    assert new_anton is anton
    assert unknown is None

def test_delete_freelancer():
    anton = Freelancer("Anton", "Python Developer", 5, 5)

    manager = FreelancerManager()
    manager.add_freelancer(anton)

    deleted_anton = manager.delete_freelancer("Anton")
    unknown = manager.delete_freelancer("Vasia")

    get_anton = manager.get_freelancer('Anton')

    assert deleted_anton is anton
    assert len(manager.freelancers) == 0
    assert get_anton is None

    assert unknown is None

def test_save_freelancers(tmp_path):
    anton = Freelancer("Anton", "Python Developer", 5, 5)
    maria = Freelancer("Maria", "Designer", 10, 15)
    alex = Freelancer("Alex", "Backend Developer", 20, 25)
    
    file_path = tmp_path / "test_data"

    manager = FreelancerManager()
    manager.add_freelancer(anton)
    manager.add_freelancer(maria)
    manager.add_freelancer(alex)

    manager.save(file_path)

    assert (tmp_path / "test_data.json").exists()

def test_load_freelancers(tmp_path):
    anton = Freelancer("Anton", "Python Developer", 5, 5)
    maria = Freelancer("Maria", "Designer", 10, 15)
    alex = Freelancer("Alex", "Backend Developer", 20, 25)

    freelancers = [anton, maria, alex]

    file_path = tmp_path / "test_data"

    manager = FreelancerManager()

    manager.add_freelancer(anton)
    manager.add_freelancer(maria)
    manager.add_freelancer(alex)

    manager.save(file_path)

    manager.load(file_path)

    loaded_manager = manager

    assert loaded_manager.freelancers == freelancers 

    for freelancer in loaded_manager.freelancers:
        assert isinstance(freelancer, Freelancer)