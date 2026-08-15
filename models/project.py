class Project:
    def __init__(self, name, client, budget, freelancer):
        self.name = name
        self.client = client
        self.budget = budget
        self.freelancer = freelancer
    def show_info(self):
         print(f'Проект: {self.name}')
         print(f"Клиент: {self.client.name}")
         print(f"Email: {self.client.email}")
         print(f"Бюджет: {self.budget}")
         print(f"Исполнитель: {self.freelancer.name}")
