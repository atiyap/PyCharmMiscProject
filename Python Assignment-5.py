# Easy Level (1–8)
# 1. Write a while loop to print numbers from 1 to 10.
number = 1
print("Numbers from 1 to 10 :")
while number <= 10:
    print(number)
    number +=1


# 2. Write a program to print all even numbers between 1 and 20 using a while loop.
num = 1
print("Even numbers between 1 and 20 :")
while num <= 20:
    if num % 2 == 0:
        print(num)
    num +=1


# 3. Create a list of 5 fruits and print each fruit using a while loop.
fruits = ["apple", "banana", "cherry", "grapes", "orange"]
print("Fruits :")
i= 0
while i < len(fruits):
    print(fruits[i])
    i+=1


# 4. Write a program to print the length of a list.
newList = [1, 3, 'atiya', [1,7,0], {'name': 'Alex', 'age': 10}]
print('Length of the list is:', len(newList))


# 5. Write a program to print all elements of a list using index-based access.
j = 0
while j < len(newList):
    print(newList[j])
    j+=1


# 6. Use a while loop to print numbers from 10 to 1.
number = 10
print("Numbers from 10 to 1 :")
while number >= 1:
    print(number)
    number -=1


# 7. Write a program that prints numbers from 1 to 5 and stops when the number is 3 using
# break.
print("Numbers from 1 to 5 and stops when the number is 3  :")
for number in range(1, 6):
    if number == 3:
        break
    print(number)


# 8. Given a list of integers, print only the first element of the list.
integerList = [100, 2, 31, 4, 0, 50000, 3, 7, 11]
print("First element of the list: ")
print(integerList[0])


# 🟡 Basic Level (9–17)
# 9. Write a program to print all elements of a list until a value 0 is found, using break.
print("All element of the list until 0 is found: ")
for x in integerList:
    if x == 0:
        break
    print(x)


# 10. Write a program to count how many elements are in a list using a while loop.
count = 0
while count < len(integerList):
    count += 1
print("Size of list is:",count)


# 11. Given a list of numbers, print only the odd numbers using a while loop.
count = 0
print("Odd numbers in the list are:")
while count < len(integerList):
    if integerList[count] % 2 == 1:
        print(integerList[count])
    count += 1

# 12. Write a program that prints numbers from 1 to 10, but skips 5 using continue.
print("Numbers from 1 to 10, skipping 5:")
for n in range(1, 11    ):
    if n == 5:
        continue
    else:
        print(n)


# 13. Write a program to sum all elements of a list using a while loop.
print("sum of all elements of a list ")
s = 0
x = 0
while x < len(integerList):
    s += integerList[x]
    x += 1
print(s)



# 14. Write a program to find the largest number in a list.
integerList.sort()
x = len(integerList)
print("Largest element of the list is:", integerList[x-1])


# 15. Given a list of names, print all names except "Admin" using continue.
nameList = ['Alice', 'Bob', 'Charlie', 'David','Admin', 'Atiya']
for name in nameList:
    if name == 'Admin':
        continue
    print(name)

# 16. Write a program to check whether a given number exists in a list.
x = int(input("Enter a number:"))
flag = False
for element in integerList:
    if element == x:
        flag = True
if flag:
    print("Element", x, " is present in the list")
else:
    print("Element", x, " is not present in the list")


# 17. Write a program to print all elements at even index positions in a list.
integerList = [100, 2, 31, 4, 0, 50000, 3, 7, 11]
for x in range(0, len(integerList), 2):
    print(integerList[x])


# 🔵 Medium Level (18–25)
# 18. Write a program to count how many even and odd numbers are present in a list.
integerList = [100, 2, 31, 4, 0, -50000, 3, 7, 11]
evenCount = 0
oddCount = 0
for x in integerList:
    if x % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print("Number of even integers in the list are:",evenCount," and number of odd integers are ", oddCount)

# 19. Write a program to remove all negative numbers from a list (print only positive
# numbers).
integerList = [100, -2, 31, 4, 0, -50000, 3, 7, -11]
print("All positive numbers in the list are:")
for x in integerList:
    if x < 0:
        continue
    print(x)

# 20. Given a list of numbers, stop printing elements when a number greater than 50 is
# found.
integerList = [100, -2, 31, 4, 0, -50000, 3, 7, -11]
print("All elements in the list less than 50 are:")
for x in integerList:
    if x > 50:
        break
    print(x)


# 21. Write a program to reverse a list using a while loop.
integerList = [100, -2, 31, 4, 0, -50000, 3, 7, -11]
print("Reverse list:")
reverseList = []
i = len(integerList) - 1
while i != -1:
    reverseList.append(integerList[i])
    i -= 1
print(reverseList)


# 22. Write a program to find the second-largest number in a list.
integerList = [100, -2, 31, 4, 0, -50000, 3, 7, -11]
integerList.sort()
x = len(integerList)
print("Second largest element of the list is:", integerList[x-2])


# 23. Write a program to print duplicate elements from a list.
integerList = [100, 3,-2, 31, 4, 0, -50000, 3, 7, -11, 100]
count = 0
n = 0
for x in range(0,len(integerList),1):
    for y in range(x+1,len(integerList),1):
        if integerList[x] == integerList[y]:
           count += 1
    if count > 0:
        print(integerList[x], " is duplicate element present in the list")
        n +=1
    count = 0
if n == 0:
    print("No duplicate element present in the list")



# 24. Write a program that takes user input repeatedly and stores values in a list until the
# user enters -1.
newList = []
x = 0
while x != -1:
    x = int(input("Enter a number:"))
    if x == -1:
        break
    newList.append(x)
print(newList)


# 25. Write a program to check whether a list is sorted in ascending order or not.
integerList = [1,2,3,4,5,6]
sortedList = sorted(integerList)
if integerList == sortedList:
    print("List is sorted in ascending order")
else:
    print("List is not sorted in ascending order")
