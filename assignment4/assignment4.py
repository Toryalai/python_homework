# Import the pandas library
import pandas as pd

# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# 1.1. Create a DataFrame from a dictionary:

# Create a dictionary with employee data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary into a DataFrame
task1_data_frame = pd.DataFrame(data)

# Print the DataFrame to verify it was created correctly
print("Task 1.1 - Original DataFrame:")
print(task1_data_frame)

# 1.2. Add a new column:
# Make a copy of the original DataFrame
# Using copy() ensures the original DataFrame is not modified
task1_with_salary = task1_data_frame.copy()

# Add a new column called 'Salary'
task1_with_salary['Salary'] = [70000, 80000, 90000]

# Print the new DataFrame
print("\nTask 1.2 - DataFrame with Salary column:")
print(task1_with_salary)

# 1.3. Modify an existing column:
# Make a copy of the DataFrame with salary
task1_older = task1_with_salary.copy()

# Increment the 'Age' column by 1
task1_older['Age'] = task1_older['Age'] + 1

# Print the modified DataFrame
print("\nTask 1.3 - DataFrame with incremented Age:")
print(task1_older)

# 1.4. Save the DataFrame as a CSV file:

# Save the DataFrame to a CSV file
# index=False prevents Pandas from writing row numbers into the file
task1_older.to_csv('employees.csv', index=False)

print("\nTask 1.4 - DataFrame saved as employees.csv")


############### Task 2: Loading Data from CSV and JSON Files ###############
# 2.1. Read data from a CSV file:
# Load the CSV file created in Task 1 into a new DataFrame

task2_employees = pd.read_csv('employees.csv')

# Print the DataFrame to verify it loaded correctly
print("Task 2.1 - Employees loaded from CSV:")
print(task2_employees)

# 2.2 Read data from a JSON file
# Create a dictionary representing new employees
additional_employees = [
    {
        "Name": "Eve",
        "Age": 28,
        "City": "Miami",
        "Salary": 60000
    },
    {
        "Name": "Frank",
        "Age": 40,
        "City": "Seattle",
        "Salary": 95000
    }
]

# Convert the dictionary into a DataFrame
json_employees = pd.DataFrame(additional_employees)

# Save the DataFrame as a JSON file
json_employees.to_json('additional_employees.json', orient='records', indent=4)

# 2.3. Load the JSON file into a DataFrame
# Combine the CSV and JSON DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# Print the combined DataFrame
print("\nTask 2.3 - Combined Employees DataFrame:")
print(more_employees)

################ Task 3: Data Inspection – head(), tail(), shape, and info() ################
# 3.1 Use the head() method
# Select the first three rows of the DataFrame
first_three = more_employees.head(3)

# Print the result
print("Task 3.1 - First three rows:")
print(first_three)

# 3.2 Use the tail() method
# Select the last two rows of the DataFrame
last_two = more_employees.tail(2)

# Print the result
print("\nTask 3.2 - Last two rows:")
print(last_two)

# 3.3 Get the shape of the DataFrame
# Get the shape (rows, columns) of the DataFrame
employee_shape = more_employees.shape

# Print the shape
print("\nTask 3.3 - Shape of the DataFrame:")
print(employee_shape)

# 3.4 Use the info() method
# Print a concise summary of the DataFrame
print("\nTask 3.4 - DataFrame Info:")
more_employees.info()


####################### Task 4: Data Cleaning with Pandas #######################
# 4.1 Load the dirty CSV file
# Load the dirty data from CSV into a DataFrame
dirty_data = pd.read_csv('dirty_data.csv')

# Print the dirty data
print("Task 4.1 - Original Dirty Data:")
print(dirty_data)

# 4.2 Create a copy for cleaning
# Create a copy of the dirty data to clean
clean_data = dirty_data.copy()

# 4.3 Remove duplicate rows
# Remove duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()

# Print the DataFrame after removing duplicates
print("\nTask 4.3 - After Removing Duplicates:")
print(clean_data)

# 4.4 Convert Age to numeric and handle missing values
# Convert Age column to numeric
# Errors are turned into NaN (missing values)
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# Print the updated DataFrame
print("\nTask 4.4 - Age Converted to Numeric:")
print(clean_data)

# 4.5 Convert Salary to numeric and replace placeholders
# Replace known placeholders with NaN
clean_data['Salary'] = clean_data['Salary'].replace(
    ['unknown', 'n/a', 'N/A'], pd.NA
)

# Convert Salary column to numeric
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# Print the updated DataFrame
print("\nTask 4.5 - Salary Converted to Numeric:")
print(clean_data)

# 4.6 Fill missing numeric values
# Fill missing Age values with the mean age
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())

# Fill missing Salary values with the median salary
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

# Print the updated DataFrame
print("\nTask 4.6 - Missing Values Filled:")
print(clean_data)

# 4.7 Convert Hire Date to datetime
# Convert Hire Date column to datetime format
clean_data['Hire Date'] = pd.to_datetime(
    clean_data['Hire Date'],
    format='mixed',
    errors='coerce'
)

# Print the updated DataFrame
print("\nTask 4.7 - Hire Date Converted to Datetime:")
print(clean_data)

# 4.8 Strip whitespace and standardize text columns
# Strip extra whitespace and convert Name to uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()

# Strip extra whitespace and convert Department to uppercase
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

# Print the final cleaned DataFrame
print("\nTask 4.8 - Text Standardized:")
print(clean_data)
