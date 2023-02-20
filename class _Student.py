import random


class Student:
    def __init__(self, sex, age, subjects = 3, marks = [1, 2, 3], name = 'Vanya', group = 'A'):  # конструктор
        self.sex = sex  # 0 - жен, 1 - муж
        self.age = age  # int number from 6 to 18
        self.subjects = subjects  # num of subjects from 2 to 4
        self.marks = marks  # array of int nums between 1 and 5
        self.name = name  # string of letters
        self.group = group  # 1 upper letter
        if self.sex != 0 and self.sex != 1:
            raise ValueError("Sex must be int or bool")
        if age > 18 or age < 6:
            raise ValueError("Incorrect age")
        if subjects > 4 or subjects < 2:
            raise ValueError("Inccorrect num of subjects")
        for i in marks:
            if not str(i).isdigit or i > 5 or i < 1:
                raise ValueError("Incorrect format of mark")
        if len(group) != 1 or not group.isupper():
            raise ValueError("Incorrect group name")
    
    def __str__(self):
        return f"Sex - {self.sex}, Age - {self.age}, Subjects - {self.subjects}, Marks - {'; '.join(str(x) for x in self.marks)}, Name - {self.name}, Group - {self.group}"
    

"""class Teacher:
    def __init__"""


def func(age:int = 14, name:str = 'Masha'):
    print(f"This person's name is {name} and their age is {age}")
    
    
def my_print(list_of_students:[]):
    for i in range(len(list_of_students)):
        if(list_of_students[i].sex == 0):
            print(f'Sex - жен, name - {list_of_students[i].name}, age - {list_of_students[i].age}')
        if(list_of_students[i].sex == 1):
            print(f'Sex - муж, name - {list_of_students[i].name}, age - {list_of_students[i].age}')

def main():
    func()
    func(9, "Masha")
    func(15, "Vacya")
    func(18, "Vova")
    
    list_of_students = []
    
    """student1 = Student(0, 10, 2, [3, 4], "Olya", 'A')
    student2 = Student(1, 12, 4, [3, 4, 5, 5], "Petya", 'B')
    student3 = Student(0, 13, 3, [3, 4, 2], "Masha", 'T')
    student4 = Student(1, 8, 4, [3, 4, 1, 2], "Pasha", 'T')
    student5 = Student(1, 16, 3, [3, 4, 5], "Marat", 'A')
    list_of_students.append(student1)
    list_of_students.append(student2)
    list_of_students.append(student3)
    list_of_students.append(student4)
    list_of_students.append(student5)
    
    student6 = Student(0, 7, 3, [4, 1, 2], "Dina", 'B')
    student7 = Student(0, 14, 2, [4, 5], "Madina", 'T')
    list_of_students.append(student6)
    list_of_students.append(student7)"""
    
    """list_of_students.append(Student(0, 12))
    list_of_students.append(Student(0, 12, 4))"""
    
    for i in range(10):
        sex = random.randint(-1, 2)
        age = random.randint(5, 20)
        subject = random.randint(1, 6)
        marks = [1, 2, 3]
        len_name= random.randint(1, 5)
        name = ''
        for j in range (len_name):
            _l = random.randint(141, 172)
            name += chr(_l) 
        group = "A"
        try:
            student = Student(sex, age, subject, marks, name, group)
            list_of_students.append(student)
        except ValueError as error:
            print(error)
        
        
        
    
    my_print(list_of_students)  # print for list of students
    
    for i in range(len(list_of_students)):
        print(list_of_students[i])


if __name__ == '__main__':
    main()
