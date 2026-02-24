# from collections import Counter
# integerList = [1,2, 3, 5,5, 6,6,3,4,1]
# newList = []
# counterOutput = Counter(integerList)
# print(counterOutput)
# for i, value in counterOutput.items():
#     if value > 1:
#         newList.append(i)
# print(newList)
import string
from os.path import split

# integer_list = [1,2, 3, 5,5, 6,6,3,4,1]
    # def third_element(list):
    #     return list[2]
    # print(third_element(integer_list))

# integer_list = [1,2, 3, 5,5, 6,6,3,4,1]
# def average(list):
#     return sum(list)/len(list)
# print(average(integer_list))

#list = [1,2,3] #- [1,2,4]
digits = [98] #- [1,0]
# digits = [4,3,2,1]#-[4,3,2,2]
def add_one(list_1):
    digit_str = int("".join([str(x) for x in digits]))
    print(digit_str)
    digit_str+=1
    new_digit = [int(i) for i in str(digit_str)]
    return new_digit
print(add_one(list))