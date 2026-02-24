# Python Assignment - 4
# Basic Level (1–5)
# 1. Even or Odd
# Write a program that takes a number as input and checks whether it is even or odd using if
# and else.
print('----# 1. Even or Odd--------------------')
number = int(input('Enter a number:'))
if number % 2 == 0:
    print('even')
else:
    print('odd')

# 2. Positive, Negative, or Zero
# Take a number from the user and determine whether it is:
# ● Positive
# ● Negative
# ● Zero
# Use if, elif, and else.
print('----# 2. Positive, Negative, or Zero--------------------')
number1 = int(input('Enter a number:'))
if number1 > 0:
    print('positive')
elif number1 < 0:
    print('negative')
else:
    print('zero')
# 3. Voting Eligibility
# Ask the user for their age and check:
# ● If age is 18 or above → eligible to vote
# ● Otherwise → not eligible
print('----# 3. Voting Eligibility--------------------')
age = int(input('Enter your age:'))
if age >= 18:
    print('you are eligible to vote')
else:
    print('you are not eligible to vote')
# 4. Pass or Fail
# Take marks as input and check:
# ● If marks are 40 or more, print "Pass"
# ● Else print "Fail"
print('----# 4. Pass or Fail--------------------')
# 5. Largest of Two Numbers
# Take two numbers as input and print which number is greater.
# If both are equal, print "Both numbers are equal".
print('----# 5. Largest of Two Numbers--------------------')
first_number = int(input('Enter first number:'))
second_number = int (input('Enter second number:'))
if first_number > second_number:
    print('First number is greater than second number')
elif first_number < second_number:
    print('Second number is greater than first number')
else:
    print('Both numbers are equal')
# Intermediate Level (6–10)
# 6. Grade Calculator
# Take marks as input and assign grades:
# ● 90 and above → Grade A
# ● 75 to 89 → Grade B
# ● 50 to 74 → Grade C
# ● Below 50 → Fail
print('----# 6. Grade Calculator--------------------')
marks1 = int(input('Enter your marks:'))
if marks1 >= 90:
    print('Grade A')
elif 75 <= marks1 <=89:
    print('Grade B')
elif 50 <= marks1 <= 74:
    print('Grade C')
else:
    print('Fail')
# 7. Simple Calculator (Conditions Only)
# Take two numbers and an operator (+, -, *, /) as input.
# Use if-elif-else to perform the correct operation.
print('----# 7. Simple Calculator (Conditions Only)--------------------')
first_number1 = int(input('Enter first number:'))
second_number1 = int(input('Enter second number:'))
operation = str(input('Enter operation from (+, -, *, /):'))
if operation == '+':
    print(first_number1 + second_number1)
elif operation == '-':
    print(first_number1 - second_number1)
elif operation == '*':
    print(first_number1 * second_number1)
else:
    print(first_number1 / second_number1)
# 8. Temperature Check
# Take temperature in Celsius and print:
# ● "Cold" if temperature < 15
# ● "Moderate" if temperature is between 15 and 30
# ● "Hot" if temperature > 30
print('----# 8. Temperature Check--------------------')
temp = int(input('Enter temperature in Celsius:'))
if temp < 15:
    print('Cold')
elif 15 <= temp < 30:
    print('Moderate')
else:
    print('Hot')
# 9. Login Validation
# Take a username and password as input.
# ● If both match predefined values, print "Login successful"
# ● Else print "Invalid credentials"
print('----# 9. Login Validation--------------------')
username = str(input('Enter your username:'))
password = str(input('Enter your password:'))
if username == 'atiya' and password == 'parveen':
    print('Login Successful')
else:
    print('Invalid credentials')
# 10. Electricity Bill Slab
# Take the number of units consumed and calculate the bill:
# ● Up to 100 units → ₹5 per unit
# ● 101–200 units → ₹7 per unit
# ● Above 200 units → ₹10 per unit
# Use if, elif, and else.
print('----# 10. Electricity Bill Slab-------------------')
unit = int(input('Enter number of units consumed by you:'))
if unit <= 100:
    print('Your Electricity Bill is: ', 5 * unit)
elif 101 <= unit <= 200:
    print('Your Electricity Bill is: ', 7 * unit )
else:
    print('Your Electricity Bill is: ', 10 * unit )