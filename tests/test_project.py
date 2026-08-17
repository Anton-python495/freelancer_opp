import pytest

from models import Freelancer, Client, Project

def test_project_creation(project):
    assert project.name == "Telegram bot"
    assert project.client.name == "Microsoft"
    assert project.client.email == "client@gmail.com"
    assert project.budget == 1500
    assert project.freelancer.name == "Anton"

def test_project_show_project(project, capsys):
    project.show_info()

    captured = capsys.readouterr()

    assert "Telegram bot" in captured.out
    assert "Microsoft" in captured.out
    assert "client@gmail.com" in captured.out
    assert "1500" in captured.out
    assert "Anton" in captured.out