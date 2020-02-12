class Person:

    def parse(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.set_role(data)
        self.set_additional_data(data)

    def set_role(self, data):
        pass

    def set_additional_data(self, data):
        pass

    def __str__(self):
        pass


class Student(Person):
    def __init__(self, data):
        self.parse(data)

    def set_role(self, data):
        self.role = 'student'

    def set_additional_data(self, data):
        self.avarage_mark = data['additional_data']['avarage_mark']

    def __str__(self):
        return (
            f'First name: {self.first_name}\nLast name: {self.last_name}\n'
            f'Age {self.age}\nRole: {self.role}\nAvarage mark: {self.avarage_mark}'
        )
          
  

class Director(Person):
    def __init__(self, data):
        self.parse(data)
    
    def set_role(self, data):
        self.role = 'director'

    def set_additional_data(self, data):
        temp = data['additional_data']
        self.exp = temp['exp_month']
        self.salary = temp['salary']

    def __str__(self):
        return (
            f'First name: {self.first_name}\nLast name: {self.last_name}\n'
            f'Age {self.age}\nRole: {self.role}\nExpierens: {self.exp}\n'
            'Salary: {0} {1}'.format(self.salary['amount'], self.salary['currency'])
        )


class Teacher(Person):
    def __init__(self, data):
        self.parse(data)
    
    def set_role(self, data):
        self.role = 'teacher'

    def set_additional_data(self, data):
        temp = data['additional_data']
        self.exp = temp['exp_month']
        self.salary = temp['salary']
    
    def __str__(self):
        return (
            f'First name: {self.first_name}\nLast name: {self.last_name}\n'
            f'Age {self.age}\nRole: {self.role}\nExpierens: {self.exp}\n'
            'Salary: {0} {1}'.format(self.salary['amount'], self.salary['currency'])
        )
