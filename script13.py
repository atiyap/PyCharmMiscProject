# def lcm(a, b):
#     greater = max(a, b)
#     while True:
#         if greater % a == 0 and greater % b == 0:
#             return greater
#         greater += 1
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("LCM is:", lcm(num1, num2))



# def reverse_num(old_num):
#     new_num = 0
#     while old_num > 0:
#         last_digit = old_num % 10
#         new_num = (new_num * 10) + last_digit
#         old_num = old_num // 10
#     return new_num
#
# num = int(input('Enter any number:'))
# print(reverse_num(num))

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
