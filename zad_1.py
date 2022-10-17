from statistics import mean


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return True if (mean(self.marks) > 50) else False


a = Student("Piotr", [1, 2, 3])
b = Student("Rafał", [10000000000, 2, 3])
print(a.is_passed())
print(b.is_passed())
