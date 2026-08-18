from utils.json_manager import save_json, load_json

def test_save_json(tmp_path):
    data = {'name': 'Anton', "hourly_rate": 10}
    file_path = tmp_path / "test_data"
    save_json(data, file_path)
    assert (tmp_path / "test_data.json").exists()

def test_load_json(tmp_path):
    data = {"name": "Anton", "hourly_rate": 10}
    file_path = tmp_path / "test_data"
    save_json(data, file_path)
    loaded_data = load_json((file_path))
    assert loaded_data == data