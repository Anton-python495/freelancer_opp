from models import Freelancer, Client, Project

def test_project_creation(project):
    assert project.name == "Telegram bot"
    assert project.client.name == "Microsoft"
    assert project.client.email == "client@gmail.com"
    assert project.budget == 1500
    assert project.freelancer.name == "Anton"

def test_project_show_project(project):
    assert f'Проект: {project.name}' == 'Проект: Telegram bot'
    assert f"Клиент: {project.client.name}" == "Клиент: Microsoft"
    assert f"Email: {project.client.email}" == "Email: client@gmail.com"
    assert f"Бюджет: {project.budget}" == "Бюджет: 1500"
    assert f"Исполнитель: {project.freelancer.name}" == "Исполнитель: Anton"