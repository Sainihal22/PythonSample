import pandas as pd
# Series
# s = pd.Series([10,20,30])
# print(s)

# DataFrame
# data = {
#     "Name" : ["Amit", "Priya", "Rohit"],
#     "Salary" : [60000, 80000, 45000]
# }

# # print(data)

# df = pd.DataFrame(data)
# print(df)

# Reading csv file
df = pd.read_csv("C:\\Users\\Sai_nihal_Kothi\\PythonSample\\employees_teaching_dataset.csv")
print(df)
# print()

# Top records
# print(df.head())

# Bottom records
# print(df.tail())

# To get information like data types, missing values
# print(df.info())

# To get statistical summary
# print(df.describe())

# Select a single column
# print(df["Salary"])

# Selecting multiple columns
# print(df[["Name", "Salary"]])

# Filter based on a condition
# print(df[df["Salary"] > 60000])

# Simple Aggregeations
# Mean
# print(df["Salary"].mean())

# Max
# print(df["Salary"].max())

# Min
# print(df["Salary"].min())

# Count
# print(df["Salary"].count())

# data = {
#     "Name": ["Amit", "Priya", "Rohit", "Neha"],
#     "Age": [25, 30, 35, 28],
#     "Salary": [60000, 70000, 80000, 65000]
# }

# df = pd.DataFrame(data)
# print(df)

# Tasks:

# Create DataFrame

# Show first 2 rows

# Find average salary

# Filter salary > 65000

# Find maximum age

# Day 2

# Creating a new column

# df["Bonus"] = df["Salary"] * 0.10
# print(df)

# df["Senior"] = df["Age"] > 30
# print(df)

# Adding rows

# 1. using loc

# older_data = {
#     "Name": ["Amit", "Priya", "Rohit", "Neha"],
#     "Age": [25, 30, 35, 28],
#     "Salary": [60000, 70000, 80000, 65000]
# }

# df = pd.DataFrame(older_data)
# print(df)

# data = {
#     "Name" : "Amit",
#     "Age" : 34,
#     "Salary" : 56000
# }

# print(len(df))

# df.loc[len(df)] = data
# print(df)

# 2. Concat

# data = {
#     "Name" : ["Amit"],
#     "Age" : [34],
#     "Salary" : [56000]
#     }

# new_df = pd.DataFrame(data)
# print(new_df)

# df = pd.concat([df, new_df], ignore_index=True)
# print(df)

# Sorting

# print(df.sort_values("Salary", ignore_index=True)) # By default sorting is ascending

# print(df.sort_values("Salary", ascending=False, ignore_index=True)) # Mention ascending = False for descending

# Group by

# print(df.groupby("Department"))
# print()
# for dept, group in df.groupby("Department"):
#     print("Department : ", dept)
#     print(group)
#     print()
# print(df.groupby("Department")["Salary"].mean())

# Multiple aggregations
# print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "count"]))

# Rename Columns
# print(df.rename(columns={"Salary" : "Monthly Salary"}))

# df = df.rename(columns={"Salary" : "Monthly Salary"})
# df.rename(columns={"Salary" : "Monthly Salary"}, inplace=True) # risky
# print(df)

# Safer side
# new_df = df.rename(columns={"Salary" : "Monthly Salary"})
# print("New Df : ")
# print(new_df)

# print("Old Df : ")
# print(df)

# Dropping Columns, rows
# df.drop("Age", axis=1) # it drops column
# print(df)

# df = df.drop(5)     # drops row
# print(df.reset_index(drop=True))

# df.drop(["Department","Salary"], axis=1, inplace=True)
# print(df)

# Handling Missing Values

# 1 Drop the rows completely

# df = df.dropna()
# print(df.reset_index(drop=True))

   # Remove only NaN from specific column
# df = df.dropna(subset=["Salary"])
# print(df)

# 2. Fill NaN values with a constant

# df = df.fillna(0)
# print(df)

# Different constant values to different columns

# df = df.fillna(
#     {
#         "Department" : "Uknown",
#         "Salary":df["Salary"].mean()
#     }
# )
# print(df)

# 3. Filling NaN values with mean, mode, median

# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
# print(df)

# Converting df into csv/excel files

# df.to_csv("Employee.csv")  # csv file
# df.to_excel("Employee.xlsx")  # excel file

# df1 = pd.DataFrame(
#     {
#         "Employee_ID" : ["E101", "E102", "E103"],
#         "Name" : ["Amit", "Priya", "Rohit"],
#         "Department" : ["IT", "HR", "Finance"]
#     }
# )

# df2 = pd.DataFrame(
#     {
#         "Employee_ID" : ["E101", "E102", "E105"],
#         "Salary" : [60000, 70000, 80000]
#     }
# )

# print(df1)
# print()
# print(df2)
# print()

# 1. Inner Join : Only Matching Ids, by default
# merged = pd.merge(df1, df2, on="Employee_ID")
# print(merged)
# print()
# merged_inner = pd.merge(df1, df2, on="Employee_ID", how="inner")
# print(merged_inner)

# 2. Left Join : prioritises left dataframe values
# merged_left = pd.merge(df1, df2, on="Employee_ID", how="left")
# print(merged_left)

# 3. Right Join : prioritises right dataframe values
# merged_right = pd.merge(df1, df2, on="Employee_ID", how="right")
# print(merged_right)

# 4. Outer Join : data from both tables
# merged_outer = pd.merge(df1, df2, on="Employee_ID", how="outer")
# print(merged_outer)

# Merging on multiple columns
# merged = pd.merge(df1, df2, on=["Employee_ID", "Department"])
# print(merged)

# Merging when column names are different

# df1 = pd.DataFrame(
#     {
#         "Employee_ID" : ["E101", "E102", "E103"],
#         "Name" : ["Amit", "Priya", "Rohit"],
#         "Department" : ["IT", "HR", "Finance"]
#     }
# )

# df2 = pd.DataFrame(
#     {
#         "Emp_Id" : ["E101", "E102", "E105"],
#         "Salary" : [60000, 70000, 80000]
#     }
# )

# print(df1)
# print()
# print(df2)
# print()

# merged = pd.merge(df1, df2, left_on="Employee_ID", right_on="Emp_Id")
# print(merged)

# drop duplicates
# print()
# print(df.drop_duplicates())