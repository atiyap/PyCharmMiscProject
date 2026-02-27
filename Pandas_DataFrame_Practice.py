### Practice Test
# 1. Add a new column called "`DiscountedAmount`" that is OrderAmount minus 10% discount.
# 2. Remove the "`Name`" column from the DataFrame.
# 3. Drop duplicate entries based on the "`CustomerID`" column (keep the first occurrence only).

import pandas as pd
data = {
    'CustomerID': [101, 102, 103, 101, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David'],
    'OrderAmount': [250, 450, 300, 250, 500]
}

df = pd.DataFrame(data)
print(df)
df["DiscountedAmount"] = df["OrderAmount"] * 0.9
print(df)
df.drop('Name', axis =1, inplace = True)
print(df)
df.drop_duplicates(inplace = True)
print(df)


### Problem 1: Creating a DataFrame

# Task: Create a DataFrame with the following data:
#
#
# `data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [24, 30, 35, 40],
#         'City': ['New York', 'Toronto', 'London', 'Sydney']}`
#
# Goal: Display the created DataFrame.
# ### Problem 2: Basic DataFrame Operations
#
# 1. Display only the Name and City columns.
# 2. Select and print the rows where Age is greater than 30.
#
# ### Problem 3: Adding and Deleting Columns
#
# 1. Add a new column named Salary with values [70000, 80000, 120000, 95000].
# 2. Delete the City column.
# 3. Goal: Display the updated DataFrame.
data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 30, 35, 40],
        'City': ['New York', 'Toronto', 'London', 'Sydney']}

df1 = pd.DataFrame(data1)
print(df1)
display_list = ['Name', 'City']
new_df = df1[display_list]
print(new_df)
print(df1[df1['Age'] > 30])
sal = [70000, 80000, 120000, 95000]
df1['Salary'] = sal
print(df1)
df1.drop('City', axis = 1, inplace = True)
print(df1)