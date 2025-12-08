import csv

employees = []

with open("./csv/employees.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)

names = []
for row in employees[1:]:
    full_name = row[1] + " " + row[2]
    names.append(full_name)

print("Full list of names: " + str(names))

names_with_e = []
for name in names:
    if "e" in name.lower():
        names_with_e.append(name)

print("\nNames that contain the letter 'e': " + str(names_with_e))
