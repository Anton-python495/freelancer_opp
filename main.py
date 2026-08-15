from models import Freelancer, Client, Project


if __name__ == '__main__':
    anton = Freelancer('Anton', 'Python Developer', 5, 5)
    client = Client('Microsoft', 'client@gmail.com')
    project = Project('Telegram bot', client, 1500, anton)
    anton.add_project(project)
    print(anton)
    print(len(anton))
    project.show_info()