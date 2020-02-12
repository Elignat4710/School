class School:

    def __init__(self):
        self.personal = []
        self.students = []
        self.director = []
        self.teachers = []

    def assigment_person(self):
        for i in self.personal:
            if i.role == 'student':
                self.students.append(i)
            if i.role == 'director':
                self.director.append(i)
            if i.role == 'teacher':
                self.teachers.append(i)

    def statiscic(self):
        managers = self.director + self.teachers
        student = self.students
        self.get_info(managers, 'Управляющие')
        self.get_info(student, 'Студенты')
        
    def get_info(self, data, role):
        print(' '*10, role)
        for i in data:
            print(i)
            print('*'*10)
