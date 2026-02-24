# numbers = [10, 20, 15]
#
# largest = second_largest = numbers[0]=10
#
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
#
# print("Second largest number is:", second_largest)

def hcf(num1, num2):
    h = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            h = i
    return h

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
print('hcf is :', hcf(num1, num2))