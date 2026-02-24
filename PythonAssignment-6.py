# Python Assignment - 6
# 🟢 Easy (8 Questions) – Function Basics
# 1. Write a function without arguments that prints "Learning Python Functions".
def print_message():
    print("Learning Python Functions")

print_message()


# 2. Write a function without arguments that prints numbers from 1 to 5.
def print_num():
        for n in range(1, 6):
            print(n)

print_num()

# 3. Write a function with one argument that prints the value passed.
def print_num(n):
    print("Number passed is ", n)


a = int(input('Enter any number:'))
print_num(a)


# 4. Write a function with two arguments that prints their sum.
def sum_of_num(n1, n2):
    print("Sum of both numbers are ", (n1 + n2))


a1 = int(input('Enter first number:'))
b1 = int(input('Enter second number:'))
sum_of_num(a1, b1)


# 5. Write a function without arguments that prints today’s greeting message.
def greet():
    print("Hello dear! Hope you have a wonderful day today!")

greet()

# 6. Write a function that takes a name as an argument and prints "Hello <name>".
def result(name):
    print("Hello", name)

name = input('Enter your name:')
result(name)


# 7. Write a function without arguments that prints the square of 5.
def square_number():
    print('Square of 5 is: ', 5 * 5)

square_number()


# 8. Write a function with one argument that prints whether the number is positive.
def positive(n):
    if n > 0:
        return "Number is positive."
    elif n < 0:
        return "Number is Negative."
    else:
        return "Number is 0."


num = int(input('Enter any number:'))
print(positive(num))

# 🔵 Basic (11 Questions) – Arguments & Return Values
# 9. Write a function that takes two numbers and returns their difference.
def number_def(n1, n2):
        return n1 - n2


first_number = int(input('Enter first number:'))
second_number = int(input('Enter second number:'))
print('Difference of both the number is: ', number_def(first_number, second_number))

# 10. Write a function without arguments that returns your age.
def age():
    myAge = 50
    return myAge

print("My age is :", age())

# 11. Write a function that takes a number and returns its square.
def square_number(n):
    return n * n

number = int(input('Enter any number:'))
print('Square of number is: ', square_number(number))


# 12. Write a function that takes two arguments and returns the larger number.
def largest_number(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


first_number = int(input('Enter first number:'))
second_number = int(input('Enter second number:'))
print('Largest number is: ', largest_number(first_number, second_number))

# 13. Write a function without arguments that returns the value 100.
def abc():
    return 100

print(abc())

# 14. Write a function that takes a number and returns "Even" or "Odd".
def even_odd(n):
    if n % 2 == 1:
        return "Number is odd."
    else:
        return "Number is even."

num = int(input('Enter any number:'))
print(even_odd(num))

# 15. Write a function that takes length and breadth and returns the area of a rectangle.
def area_0f_rectangle(l, b):
    area = l * b
    return area

length = int(input('Enter length of rectangle:'))
breadth = int(input('Enter breadth of rectangle:'))
print("Area of a rectangle :",area_0f_rectangle(length, breadth))


# 16. Write a function without arguments that returns the sum of two fixed numbers.
def sum_of_number():
    n1 = 10
    n2 = 20
    return n1 + n2

print("Sum of two number is :", sum_of_number())


# 17. Write a function that takes marks as an argument and returns "Pass" or "Fail".
def result(marks):
    if marks >= 40:
        return 'PASS'
    else:
        return 'FAIL'

marks = int(input('Enter your marks:'))
print('Your result is ', result(marks))


# 18. Write a function that accepts three numbers and returns their average.
def ave(num1, num2, num3):
    average = (num1 + num2 + num3)/3
    return average

first_number = int(input('Enter first number:'))
second_number = int(input('Enter second number:'))
third_number = int(input('Enter third number:'))
print("Average of three number is :",ave(first_number, second_number, third_number))


# 19. Write a function without arguments that prints a menu message.
def menu():
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")

print(menu())
# 🟡 Medium (12 Questions) – Logic + Function Design
# 20. Write a function that takes a number and returns whether it is prime.
def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return "Number is not prime."
                break
        else:
            return "Number is prime."
    else:
        return "Number is not prime."

num = int(input('Enter any number:'))
print(prime(num))


# 21. Write a function that takes a number and returns its factorial.
def math_factorial(n):
    factorial = 1
    while n != 0:
        factorial = factorial * n
        n = n - 1

    return factorial

num = int(input('Enter any number:'))
print("Factorial is :",math_factorial(num))


# 22. Write a function that takes two numbers and an operator (+, -, *, /) and returns the
# result.
def math_ope(first_num1, second_num1, op):
    if op == '+':
        return first_num1 + second_num1
    elif op == '-':
        return first_num1 - second_num1
    elif op == '*':
        return first_num1 * second_num1
    elif op == '/':
        return first_num1 / second_num1
    else:
        return "Invalid operator"

first_number1 = int(input('Enter first number:'))
second_number1 = int(input('Enter second number:'))
operation = str(input('Enter operation from (+, -, *, /):'))
print("Result is :",math_ope(first_number1, second_number1, operation))


# 23. Write a function that takes a number and returns the sum of digits.
def sum_of_digit(num):
    sum = 0
    while num != 0:
        r = num % 10
        sum+=r
        num = num // 10
    return sum

num = int(input('Enter any number'))
print('sum of digits is: ', sum_of_digit(num))


# 24. Write a function without arguments that returns the largest of three fixed numbers.
def largest_number():
    num1 = 100
    num2 = 20
    num3 = 22
    return max(num1, num2, num3)
print('Largest number is: ', largest_number())

# 25. Write a function that takes a year and returns whether it is a leap year.
def leap_year(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return "Leap year"
    else:
        return "Not a Leap year"

y = int(input('Enter any year:'))
print(leap_year(y))

# 26. Write a function that takes a number and returns its reverse.
def reverse_num(old_num):
    new_num = 0
    while old_num > 0:
        last_digit = old_num % 10
        new_num = (new_num * 10) + last_digit
        old_num = old_num / 10
    return new_num

num = input('Enter any number:')
print(reverse_num(num))

# 27. Write a function that takes a string and returns its length without using len().
def string_length(a):
    l = 0
    for char in a:
        l += 1
    return l

str2 = input('Enter any string:')
print(string_length(str2))


# 28. Write a function that takes two numbers and returns their LCM.
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM is:", lcm(num1, num2))

# 29. Write a function that takes a number and returns whether it is a palindrome.
def palindrome(str):
    if str == str[::-1]:
        return "String is palindrome"
    else:
        return "String is not palindrome"

str1 = input('Enter any string:')
print(palindrome(str1))

# 30. Write a function that takes temperature in Celsius and returns Fahrenheit.
def temp_conversion(c_temp):
    f_temperature = (c_temp * 9/5) + 32
    return f_temperature


c_temp = int(input('Enter temperature in Celsius:'))
print('Temperature in Fahrenheit is:', temp_conversion(c_temp))


# 31. Write a function that takes basic salary and returns net salary after 10% tax.
def tax(salary):
        net_salary = salary - salary * 0.1
        return net_salary
salary = int(input('Enter your Basic Salary:'))
print('Your Net Salary is:', tax(salary))

# 🔴 Hard (4 Questions) – Strong Function Mastery
# 32. Write a function that takes marks and returns grade
# (A, B, C, Fail) based on conditions.
def result(marks):
    if marks >= 90:
        return 'Grade A'
    elif 75 <= marks <=89:
        return 'Grade B'
    elif 50 <= marks <= 74:
        return 'Grade C'
    else:
        return 'Fail'
marks = int(input('Enter your marks:'))
print('Your grades are:', result(marks))

# 33. Write a function that takes three numbers and returns the second largest number.
def second_largest(num1, num2, num3):
    if num1 == num2 == num3:
        return "No second largest number"
    if (num2 < num1 < num3) or (num2 > num1 > num3):
        return num1
    elif (num1 < num2 < num3) or (num3 < num2 < num1):
        return num2
    elif (num2 < num3 < num1) or (num1 < num3 < num2):
        return num3
    else:
        return "No second largest number"
num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
num3 = int(input('Enter third number'))
print('Second largest number is :', second_largest(num1, num2, num3))

# 34. Write a function that takes a number and returns both count of digits and sum of
# digits.
def math_op(num):
    count = 0
    sum = 0
    while num != 0:
        r = num % 10
        count+=1
        sum+=r
        num = num // 10
    return count, sum

num = int(input('Enter any number'))
count_of_digit, sum_of_digit = math_op(num)
print('sum of digits is: ', sum_of_digit)
print('count is :', count_of_digit)


# 35. Write a function that takes two numbers and returns their HCF using logic (not
# # built-in).
def hcf(num1, num2):
    h = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            h = i
    return h

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
print('hcf is :', hcf(num1, num2))