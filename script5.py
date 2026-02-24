# myList = [0,1,0,3,12]
# tempList1 = []
# tempList2 = []
# for x in myList:
#     if x == 0:
#         tempList1.append(x)
#     else:
#         tempList2.append(x)
# tempList2.extend(tempList1)
# print(tempList2)
# nums = [1,2,3,4,5,6,7,89,34,12,35,12]
# newNum = []
# newNum = [number for number in nums if (number % 5== 0) and (number % 7 == 0)]
# print(newNum)
nums = [0, 1, 0, 3, 12]

index = 0  # position for next non-zero

for x in nums:
    if x != 0:
        nums[index] = x
        index += 1

print(nums)
# fill remaining positions with 0
while index < len(nums):
    nums[index] = 0
    index += 1

print(nums)