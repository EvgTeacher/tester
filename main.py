# OOP

class Student:
    group = 'B2910'
    def __init__(self, name, age, height=160):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'Name student {self.name} \nAge student {self.age} old'

    def __del__(self):
        print('DELETE object')

    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
    def info_student(self):
        print(f'Name student {self.name}\n'
              f'Age student {self.age} old')


stud1 = Student(name=None, age=18)
stud2 = Student(name='Dima', age=12)
print(stud1)
print(stud2)
print(bool(stud1))
print(bool(stud2))
print(len(stud1))

# print(stud1.name)
# print(stud1.age)
# print(stud1.group)
#
# print(stud2.name)
# print(stud2.age)
# print(stud2.group)
#
# print(Student.group)
#
# Student.group = 'V2910'
#
# print(Student.group)
# print(stud1.group)
# print(stud2.group)
# stud1.group = 'B2911'
# print(stud1.group)
# print(Student.group)
# print(stud2.group)
# stud2.group = '3910'
# print(stud2.group)
# stud3 = Student(name='Anna', age=17)
# print(stud3.group)