class School:
    def __init__(self, course, activity):
        self.course = course
        self.activity = activity

    def course(self):
        return self.course

    def account(self):
        return self.account


class Student(School):
    def __init__(self, name):
        self.name = name

    def info(self):
        return "My name is ", self.name

a1 = Student("Math", "Cricket")
print(a1.course, a1.activity)
