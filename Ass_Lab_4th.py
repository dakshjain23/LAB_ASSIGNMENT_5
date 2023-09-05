employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]

def search_employee_data(parameter, value):
    results = []
    for employee in employee_data:
        if parameter == 1 and employee["Age"] == value:
            results.append(employee)
        elif parameter == 2 and employee["Name"] == value:
            results.append(employee)
        elif parameter == 3:
            operator, salary_value = value[0], int(value[1:])
            if operator == ">" and employee["Salary (PM)"] > salary_value:
                results.append(employee)
            elif operator == "<" and employee["Salary (PM)"] < salary_value:
                results.append(employee)
            elif operator == ">=" and employee["Salary (PM)"] >= salary_value:
                results.append(employee)
            elif operator == "<=" and employee["Salary (PM)"] <= salary_value:
                results.append(employee)
    
    return results



print("Employee Table Search")
print("Search Parameters:")
print("1. Age")
print("2. Name")
print("3. Salary (>, <, <=, >=)")

parameter = int(input("Enter search parameter (1/2/3): "))
value = input("Enter search value: ")

results = search_employee_data(parameter, value)

if not results:
    print("No matching records found.")
else:
    print("Matching Employee Records:")
    for result in results:
        print(f"Employee ID: {result['Employee ID']}, Name: {result['Name']}, Age: {result['Age']}, Salary (PM): {result['Salary (PM)']}")