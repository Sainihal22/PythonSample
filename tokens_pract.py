import pandas as pd
df = pd.read_csv("customers.csv")
# df = pd.read_csv("C:\\Users\\Sai_nihal_Kothi\\Downloads\\customers.csv")

# print(df)

# print(df[df["spend"]>10000])
name = df.iloc[0]["name"]
print(name)
# length_of_df = len(df)

# boolean
# is_greater = length_of_df>=10

# if else condition
# if is_greater:
#     print("Greater than 10 rows")
# else:
#     print("Less than 10 rows")

# if length_of_df >= 10:
#     print("Greater than 10 rows")
# else:
#     print("Less than 10 rows")

# Avg
# avg_spend = df["spend"].mean()
# print(avg_spend)
# spend_df = df['spend']
# print(spend_df)
# sum = 0
# for i in spend_df:
#     sum += i
#     # sum = sum + i
# length_of_df = len(df)
# # print(length_of_df)
# print(sum) 
# print(sum/length_of_df) # you take the quotient
# print(sum%length_of_df) # you take reminder


# size : len()
# length_of_df = len(df)
# print(length_of_df)

# Columns
# columns_of_df = df.columns
# print(columns_of_df)

# length_of_columns = len(columns_of_df)
# print(length_of_columns)

# Accessing a value in a list
# for i in range(length_of_columns):
#     print(i)

# for i in range(length_of_columns):
#     print(columns_of_df[i])

# for col in columns_of_df:
#     print(col)