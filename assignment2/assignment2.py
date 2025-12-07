import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File

def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            first_row = True 

            for row in reader:
                if first_row:
                    data["fields"] = row  
                    first_row = False
                else:
                    rows.append(row)    

        data["rows"] = rows

        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

employees = read_employees()

print(employees)

# Task 3: Find the Column Index

def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")
print("employee_id column is at index:", employee_id_column)

first_name_column = column_index("first_name")
print("first_name column is at index:", first_name_column)

last_name_column = column_index("last_name")
print("last_name column is at index:", last_name_column)

phone_column = column_index("phone")
print("phone column is at index:", phone_column)

# Task 4: Find the Employee First Name

def first_name(row_number):
    col = column_index("first_name")
    row = employees["rows"][row_number]
    return row[col]

# Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):

    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]
        )
    )
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

# Task 8: Create a dict for an Employee

def employee_dict(row):
    result = {}

    for field, value in zip(employees["fields"], row):
        if field == "employee_id":
            continue
        result[field] = value

    return result

# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        emp_id = int(row[employee_id_column])
        result[emp_id] = employee_dict(row)

    return result

# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")

print("THISVALUE is:", get_this_value())

# Task 11: Creating Your Own Module
def set_that_secret(value):
    custom_module.set_secret(value)

set_that_secret("my_secret")
print("custom_module.secret is:", custom_module.secret) 

# Task 12: Read minutes1.csv and minutes2.csv

# Helper function to read a CSV file into a dict
def read_csv_as_dict(file_path):
    result = {"fields": [], "rows": []}
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            first_row = True

            for row in reader:
                row_tuple = tuple(row) 
                if first_row:
                    result["fields"] = row_tuple
                    first_row = False
                else:
                    result["rows"].append(row_tuple)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

    return result


def read_minutes():
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


# Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1.union(set2)
    return combined_set

minutes_set = create_minutes_set()

# Task 14: Convert to datetime

def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    return minutes_list

minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List

def write_sorted_list():
    global minutes_list

    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(
        map(
            lambda x: (x[0], x[1].strftime("%B %d, %Y")),
            minutes_list
        )
    )

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list

sorted_minutes = write_sorted_list()
