from models import Freelancer
from utils import save_freelancers, load_freelancers

def test_save_freelancers(tmp_path):
    freelancers = [Freelancer('Anton', 'Python Developer', 5, 5),
                   Freelancer("Maria", "Designer", 10, 15),
                   Freelancer("Alex", "Backend Developer", 20, 35)]
    
    file_path = tmp_path / "test_data"

    save_freelancers(freelancers, file_path)

    assert (tmp_path / "test_data.json").exists()

def test_load_freelancers(tmp_path):
    freelancers = [Freelancer('Anton', 'Python Developer', 5, 5),
                   Freelancer("Maria", "Designer", 10, 15),
                   Freelancer("Alex", "Backend Developer", 20, 35)]
    
    file_path = tmp_path / "test_data"

    save_freelancers(freelancers, file_path)


    loaded_freelancers = load_freelancers(file_path)

    assert loaded_freelancers == freelancers

    for freelancer in loaded_freelancers:
        assert isinstance(freelancer, Freelancer)
