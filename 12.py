# Create employee dictionary

employee = {
    "E1": {
        "emp_name": "Rahul",
        "designation": "Manager",
        "dept": "HR",
        "salary": 50000
    },
    "E2": {
        "emp_name": "Priya",
        "designation": "Developer",
        "dept": "IT",
        "salary": 60000
    },
    "E3": {
        "emp_name": "Amit",
        "designation": "Accountant",
        "dept": "Finance",
        "salary": 45000
    },
    "E4": {
        "emp_name": "Sneha",
        "designation": "Developer",
        "dept": "IT",
        "salary": 70000
    },
    "E5": {
        "emp_name": "Riya",
        "designation": "Designer",
        "dept": "Design",
        "salary": 55000
    }
}


# 1. Print record of employee E1

print("Record of E1:")
print(employee["E1"])


# 2. Print department of employee E4

print("\nDepartment of E4:")
print(employee["E4"]["dept"])


# 3. Print employee having maximum salary

max_employee = max(employee, key=lambda x: employee[x]["salary"])

print("\nEmployee having maximum salary:")
print(employee[max_employee])


# 4. Insert a new employee record

employee["E6"] = {
    "emp_name": "Karan",
    "designation": "Tester",
    "dept": "IT",
    "salary": 48000
}

print("\nAfter inserting new employee:")
print(employee)