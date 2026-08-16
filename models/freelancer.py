from exceptions import InvalidIncreaseError, InvalidRateError, InvalidOrderError


class Freelancer:

    def __init__(self, name, specialization, hourly_rate, completed_orders=0):
        self.name = name
        self.specialization = specialization
        self.hourly_rate = hourly_rate
        self.completed_orders = completed_orders
        self.projects = []

    def __str__(self):
         return f'{self.name} - {self.specialization} - {self.hourly_rate}$'

    def __repr__(self):
         return (
              f'Freelancer('
              f'name = "{self.name}", '
              f'specialization = "{self.specialization}", '
              f'hourly_rate = {self.hourly_rate}, '
              f'completed_orders = {self.completed_orders})'
              )
    
    def __len__(self):
         return len(self.projects)

    def __eq__(self, other):
         if not isinstance(other, Freelancer):
              return NotImplemented
         return (self.name == other.name and self.specialization == other.specialization)

    @classmethod
    def from_dict(cls, data):
         return cls(
              data['name'],
              data['specialization'],
              data['hourly_rate'],
              data['completed_orders']
         )
    
    @property
    def hourly_rate(self):
         return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
         if not isinstance(value, (int, float)):
              raise TypeError('Значение не может быть не числом')
         if value < 5:
              raise InvalidRateError('Меньше 5 нельзя')
         self.__hourly_rate = value

    @property
    def completed_orders(self):
         return self.__completed_orders

    @completed_orders.setter
    def completed_orders(self, value):
         if not isinstance(value, int):
              raise TypeError('Значение не может быть не числом')
         if value < 0:
              raise InvalidOrderError('Количество заказов не может быть отрицательным')
         self.__completed_orders = value

    @property
    def specialization(self):
         return self.__specialization

    @specialization.setter
    def specialization(self, value):
         if not isinstance(value, str):
              raise TypeError('Значение не может быть не строкой')
         if not value.strip():
              raise ValueError('Значение не может быть пустой строкой')
         self.__specialization = value
         
    def complete_orders(self, count):
        self.completed_orders += count

    def get_project_count(self):
         return len(self.projects)

    def increase_rate(self, amount):
        if amount<0:
             raise InvalidIncreaseError('Размер увеличения не может быть отрицательным')
        self.hourly_rate += amount

    def calculate_income(self, hours):
        return self.hourly_rate * hours
    
    def work(self):
         return 'Фрилансер выполняет работу'

    def add_project(self, project):
         self.projects.append(project)

    def show_projects(self):
         print(f'Проекты {self.name}:')
         for i, project in enumerate(self.projects, start=1):
              print(f'{i}. {project.name}')

    def to_dict(self):
         return {'name': self.name, 
                 'specialization': self.specialization,
                 'hourly_rate': self.hourly_rate,
                 'completed_orders': self.completed_orders
                 }
    

    def info(self):
            return f"""
    Имя: {self.name}
    Специализация: {self.specialization}
    Ставка: {self.hourly_rate}$
    Выполненные работы: {self.completed_orders}
    """

if __name__ == "__main__":
    print('Module loaded')