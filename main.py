# OOP

class Student:
    group = 'B2910'
    def __init__(self, name, age):
        self.name = name
        self.age = age


stud1 = Student(name='Oleg', age=18)
print(stud1.name)
print(stud1.age)
print(stud1.group)
stud2 = Student(name='Dima', age=12)
print(stud2.name)
print(stud2.age)
print(stud2.group)

print(Student.group)

Student.group = 'V2910'

print(Student.group)
print(stud1.group)
print(stud2.group)
stud1.group = 'B2911'
print(stud1.group)
print(Student.group)
print(stud2.group)
stud2.group = '3910'
print(stud2.group)
stud3 = Student(name='Anna', age=17)
print(stud3.group)