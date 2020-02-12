import json
import role
from school import School




def main():
    with open('persons.json') as f:
        persons = json.load(f)

    s = School()

    for i in persons:
        if i['role'] == 'student':
            s.personal.append(role.Student(i))
        if i['role'] == 'director':
            s.personal.append(role.Director(i))
        if i['role'] == 'teacher':
            s.personal.append(role.Teacher(i))

    s.assigment_person()
    s.statiscic()


if __name__ == "__main__":
    main()