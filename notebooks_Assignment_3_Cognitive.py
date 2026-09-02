import pandas as pd

# -------------------- PART 1 --------------------

records = {
    "Tid": range(1, 11),
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": [
        "Single", "Married", "Single", "Married", "Divorced",
        "Married", "Divorced", "Single", "Married", "Single"
    ],
    "Taxable Income": [
        "125K", "100K", "70K", "120K", "95K",
        "60K", "220K", "85K", "75K", "90K"
    ],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

table = pd.DataFrame(records)

print(table)

# Selected rows
print(table.loc[[0, 4, 7, 8]])

# Rows from index 3 to 7
print(table.loc[3:7])

# Rows 4 to 8 and columns 2 to 4
print(table.iloc[4:9, 2:5])

# Columns 1 to 3
print(table.iloc[:, 1:4])


# -------------------- PART 2 --------------------

iris_data = pd.read_csv(r"C:\Users\HP\Downloads\Iris.csv")

print(iris_data.head())


# -------------------- PART 3 --------------------

iris_data = pd.read_csv(r"C:\Users\HP\Downloads\Iris.csv")

# Remove row with index 4
iris_data.drop(index=4, inplace=True)

# Remove the fourth column
iris_data.drop(columns=iris_data.columns[3], inplace=True)

print(iris_data)


# -------------------- PART 4 --------------------

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 36],
    "Salary": [50000, 70000, 65000, 55000, 68000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15", "2017-07-19", "2013-06-01",
        "2021-02-10", "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

employee_df = pd.DataFrame(employees)


# Shape of DataFrame
print("Shape:", employee_df.shape)


# Information about the DataFrame
print("\nDataFrame Information:")
employee_df.info()


# Statistical summary
print("\nStatistical Summary:")
print(employee_df.describe())


# Display first 5 records
print("\nFirst 5 Records:")
print(employee_df.head())


# Display last 3 records
print("\nLast 3 Records:")
print(employee_df.tail(3))


# -------------------- CALCULATIONS --------------------

print("\nAverage Salary:")
print(employee_df["Salary"].mean())

print("\nTotal Bonus:")
print(employee_df["Bonus"].sum())

print("\nMinimum Age:")
print(employee_df["Age"].min())

print("\nMaximum Rating:")
print(employee_df["Rating"].max())


employee_df = employee_df.sort_values(
    "Salary",
    ascending=False
)

print("\nEmployees Sorted by Salary:")
print(employee_df)




def get_performance(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    return "Average"


employee_df["Performance_Category"] = (
    employee_df["Rating"].apply(get_performance)
)

print("\nPerformance Category Added:")
print(employee_df)




print("\nMissing Values:")
print(employee_df.isna().sum())




employee_df.rename(
    columns={"Employee_ID": "ID"},
    inplace=True
)

print("\nAfter Renaming Employee_ID:")
print(employee_df)



experienced = employee_df[
    employee_df["Years_of_Experience"] > 5
]

print("\nEmployees with More Than 5 Years Experience:")
print(experienced)




it_employees = employee_df[
    employee_df["Department"].eq("IT")
]

print("\nIT Department Employees:")
print(it_employees)



employee_df["Tax"] = employee_df["Salary"].mul(0.10)

print("\nTax Added:")
print(employee_df)




employee_df.to_csv(
    "employees_modified.csv",
    index=False
)

print("\nModified employee data has been saved.")
