import csv

class Name:
    def __init__(self, name):
        self._name = name
        
    def __set__(self, obj, value: str):
        if not value.isalpha() or not value.istitle():
            raise ValueError('Некорректное имя!')
        obj.__dict__[self._name] = value

    def __get__(self, obj, cls):
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        raise AttributeError('Атрибут не найден')

    # def __del__(self):
    #     raise AttributeError('Мы не можем оставить человека без имени!')


class Student:
    firstname = Name('firstname')
    lastname = Name('lastname')

    def __init__(self, firstname, lastname, file=None):
        self._firstname = firstname
        self._lastname = lastname
        self._subjects = {}
        if file:
            with open(file, 'r', encoding = 'utf-8') as data:
                rows = csv.reader(data)
                for row in rows:
                    self._subjects[row[0]] = {'test': row[1], 'grade': row[2]}
        
         
    @property
    def subjects(self):
        return self._subjects
    
    @subjects.setter
    def set_subjects(self, file):
        raise AttributeError('Изменение невозможно!')

    @subjects.deleter
    def del_subjects(self):
        raise AttributeError('Удаление невозможно!')


    def average(self):
        if not self._subjects:
            return 'Нет пройденных тестов'
        total_test = 0
        total_grade = 0
        for i in self._subjects:
            total_test += int(self._subjects[i]['test'])
            total_grade += int(self._subjects[i]['grade'])
        return (total_test/len(self._subjects), total_grade/len(self._subjects))
        

    def __repr__(self):
        return f'Student("{self._firstname}", "{self._lastname}")'

with open('grades.csv', 'w', encoding = 'utf-8', newline = '') as output_file:
    data = [['math', 77, 4], ['chemistry', 88, 4], ['physics', 45, 3]]
    writer = csv.writer(output_file)
    writer.writerows(data)

student = Student('Иван', 'Иванов', 'grades.csv')
print(student)
print(student.subjects)
print(student.average())

