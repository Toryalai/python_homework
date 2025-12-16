import csv

employees = []

with open("./csv/employees.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)

# List comprehension for full list of names
names = [row[1] + " " + row[2] for row in employees[1:]]
print("Full list of names: " + str(names))

# List comprehension for names containing the letter "e"
names_with_e = [name for name in names if "e" in name.lower()]
print("\nNames that contain the letter 'e': " + str(names_with_e))
