# BASIC LEVEL (10 Questions)
# Goal: Understand class structure, object creation, and instance methods
# 1. Create a class Student with a method display_info() that prints "Student
# created".
class Student:
    def display_info(self):
        print("Student created")

c = Student()
c.display_info()
# 2. Define a class Car with a method start() that prints "Car started".
class Car:
    def start(self):
        print("Car started")
d = Car()
d.start()

# 3. Create a class Calculator with a method add() that prints the sum of 10 and 20.
class Calculator:
    def add(self):
        print(10 + 20)

e = Calculator()
e.add()

# 4. Write a class Greeting with a method say_hello() that prints "Hello, World!".
class Greeting:
    def say_hello(self):
        print("Hello, World!")

f = Greeting()
f.say_hello()

# 5. Create a class Person with a method introduce() that prints "I am a person".
class Person:
    def introduce(self):
        print("I am a person")

g = Person()
g.introduce()


# 6. Define a class Circle with a method area() that prints "Area calculated".
class Circle:
    def area(self):
        print("Area calculated")

h = Circle()
h.area()


# 7. Create a class Book with a method read() that prints "Reading book".
class Book:
    def read(self):
        print("Reading book")

i = Book()
i.read()

# 8. Write a class Mobile with a method call() that prints "Calling...".
class Mobile:
    def call(self):
        print("Calling...")

j = Mobile()
j.call()

# 9. Create a class Animal with a method sound() that prints "Animal makes sound".
class Animal:
    def sound(self):
        print("Animal makes sound")

k = Animal()
k.sound()


# 10. Define a class Laptop with a method power_on() that prints "Laptop is ON".
class Laptop:
    def power_on(self):
        print("Laptop is ON")

l = Laptop()
l.power_on()

# 🟡 MEDIUM LEVEL (10 Questions)
# Goal: Use self, instance variables, and method logic
# 11. Create a class Student with attributes name and marks, and a method display() to
# print them.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name, "Marks:", self.marks)

m = Student('Atiya', 70)
m.display()


# 12. Write a class Rectangle with attributes length and breadth and a method area()
# that returns the area.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

n = Rectangle(10,30)
print('Area of Rectangle is ', n.area())

# 13. Define a class BankAccount with attribute balance and methods deposit(amount)
# and display_balance().
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print("Balance:", self.balance)

o = BankAccount(1000)
o.deposit(500)
o.display_balance()


# 14. Create a class Employee with attributes name and salary, and a method
# annual_salary().
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

p = Employee('Atiya', 1000)
print("Annual salary is ",p.annual_salary())


# 15. Write a class Temperature with attribute celsius and a method to_fahrenheit().
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

q = Temperature(32)
print("Temperature in fahrenheit is ", q.to_fahrenheit())
# 16. Define a class Movie with attributes title and rating and a method is_hit()
# (rating ≥ 8).
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def is_hit(self):
        if self.rating >= 8:
            return "Hit Movie"
        else:
            return "Not a Hit"

r = Movie('Superman', 5)
print(r.is_hit())


# 17. Create a class Counter with attribute count and methods increment() and show().
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def show(self):
        print("Count:", self.count)

s = Counter()
s.increment()
s.show()

# 18. Write a class User with attributes username and password, and a method
# check_password().
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, entered_password):
        return self.password == entered_password

t = User("Atiya", "126abc")
print(t.check_password("abc"))

# 19. Define a class ShoppingCart with attribute items (list) and method
# add_item(item).
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

u = ShoppingCart()
u.add_item('abrerc')
print(u.items)


# 20. Create a class Vehicle with attributes type and speed, and a method describe().
class Vehicle:
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def describe(self):
        print("Vehicle Type:", self.type, "Speed:", self.speed)

v = Vehicle('Tesla', 200)
v.describe()

# 🔴 HARD LEVEL (5 Questions)
# Goal: Logic + multiple methods + object interaction
# 21. Create a class BankAccount with methods:
# ● deposit(amount)
# ● withdraw(amount)
# ● display_balance()

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance)

w = BankAccount()
w.deposit(100)
w.withdraw(10)
w.display_balance()

# Ensure withdrawal is allowed only if balance is sufficient.
# 22. Write a class Student with methods:
# ● add_marks(marks_list)
# ● calculate_average()
# ● is_pass() (average ≥ 40)

class Student:
    def __init__(self):
        self.marks = []

    def add_marks(self, marks_list):
        if len(marks_list) == 0:
            print("Marks list is empty")
        else:
            self.marks = marks_list

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def is_pass(self):
        return "Pass" if self.calculate_average() >= 40 else "Fail"

x = Student()
marks = [20, 35, 100]
x.add_marks(marks)
x.calculate_average()
print('Your result is ',x.is_pass())
# 23. Create a class LoginSystem with methods:
# ● register(username, password)
# ● login(username, password)
# Store credentials inside the object.

class LoginSystem:
    def __init__(self):
        self.username = ""
        self.password = ""

    def register(self, username, password):
        if username and password:
            self.username = username
            self.password = password
            print("Registration successful")
        else:
            print("Username or password cannot be empty")

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful")
        else:
            print("Invalid credentials")

y = LoginSystem()
y.register('abcdef', '123eee')
y.login('abcdef', '123eee')


# 24. Define a class LibraryBook with methods:
# ● borrow()
# ● return_book()
# ● status()


class LibraryBook:
    def __init__(self):
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed")
        else:
            print("Book already borrowed")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned")
        else:
            print("Book was not borrowed")

    def status(self):
        print("Available" if self.is_available else "Borrowed")

z = LibraryBook()
z.borrow()
z.return_book()
z.status()


# Track availability using an instance variable.
# 25. Create a class Order with methods:
# ● add_item(price)
# ● calculate_total()
# ● apply_discount(percent)
class Order:
    def __init__(self):
        self.total = 0

    def add_item(self, price):
        self.total += price

    def calculate_total(self):
        return self.total

    def apply_discount(self, percent):
        discount = (percent / 100) * self.total
        self.total -= discount
        return self.total

zz = Order()
zz.add_item(40)
zz.calculate_total()
print('Total price is', zz.apply_discount(3))

# 🚀 MAANG-STYLE INTERVIEW QUESTIONS (Concept +
# Code Thinking)🔥 MAANG Question 1 (Amazon / Google-style)
# Problem:
# Design a class LRUCounter that:
# ● Has a method hit(key)
# ● Tracks how many times each key is accessed
# ● Has a method most_used() that returns the most accessed key
# 👉 Focus: state management inside class, method logic, clean design

    class LRUCounter:
        def __init__(self):
            self.counter = {}

        def hit(self, key):
            if key in self.counter:
                self.counter[key] += 1
            else:
                self.counter[key] = 1

        def most_used(self):
            if not self.counter:
                return None

            return max(self.counter, key=self.counter.get)

    LRU = LRUCounter()
    LRU.hit("a")
    LRU.hit("a")
    LRU.hit("b")
    LRU.hit("b")
    LRU.hit("b")
    LRU.hit("c")
    LRU.hit("c")
    LRU.hit("c")
    LRU.hit("c")

    print(LRU.most_used())

# 🔥 MAANG Question 2 (Meta / Netflix-style)
# Problem:
# Design a class RateLimiter that:
# ● Allows only N requests per user
# ● Has method allow_request(user_id)
# ● Returns True if allowed, False otherwise
# 👉 Focus: real-world object modeling + method responsibility
class RateLimiter:
    def __init__(self, limit_n):
        self.limit_n = limit_n
        self.req = {}


    def allow_request(self, user_id):
        if user_id not in self.req:
            self.req[user_id] = self.limit_n - 1
            return True
        elif self.req[user_id] > 0:
            self.req[user_id] -= 1
            return True
        else:
            return False


RL = RateLimiter(5)
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))
print(RL.allow_request("atiya"))





