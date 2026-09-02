import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced",
                       "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K",
                       "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)

print(df.loc[[0, 4, 7, 8]])

print(df.loc[3:7])

print(df.iloc[4:9, 2:5])

print(df.iloc[:, 1:4])

import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\Iris.csv")

print(df.head())

import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\Iris.csv")

# Delete row 4
df = df.drop(4)

# Delete column 3
df = df.drop(df.columns[3], axis=1)

print(df)

import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 36],
    "Salary": [50000, 70000, 65000, 55000, 68000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)

Shape
print("Shape:")
print(df.shape)

Summary including data types and non-null counts
print("\nInfo:")
df.info()

# Descriptive statistics
print(df.describe())


# First 5 rows and last 3 rows

print(df.head())

print(df.tail(3))

# Calculations

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nTotal Bonus:")
print(df["Bonus"].sum())

print("\nYoungest Employee Age:")
print(df["Age"].min())

print("\nHighest Performance Rating:")
print(df["Rating"].max())

# Sort by Salary in descending order

df = df.sort_values(by="Salary", ascending=False)

print(df)

# Add Performance Category

def category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance_Category"] = df["Rating"].apply(category)

print(df)

# Identify missing values

print(df.isnull().sum())

# Rename Employee_ID to ID

df = df.rename(columns={"Employee_ID": "ID"})

print(df)

# Employees with more than 5 years of experience

print(df[df["Years_of_Experience"] > 5])

# Employees belonging to IT department

print(df[df["Department"] == "IT"])

# Add Tax column

df["Tax"] = df["Salary"] * 0.10

print(df)

# Save modified DataFrame

df.to_csv("employees_modified.csv", index=False)

print("File saved successfully!")



