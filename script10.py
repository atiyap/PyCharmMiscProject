class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def info(self):
        print('Dog name is', self.name, 'and age is', self.age, 'color is ', self.color)

labrador = Dog("rocky", "white", 7)
labrador.info()

