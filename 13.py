student = {
    "S1": {"name": "Rahul", "dept": "CSE", "marks": 85},
    "S2": {"name": "Priya", "dept": "ECE", "marks": 72},
    "S3": {"name": "Amit", "dept": "CSE", "marks": 95},
    "S4": {"name": "Sneha", "dept": "IT", "marks": 68},
    "S5": {"name": "Riya", "dept": "ECE", "marks": 80}
}

# Sort the dictionary according to marks (highest to lowest)
sorted_student = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("Students sorted according to marks:")
for roll, details in sorted_student.items():
    print(roll, details)

# Find and print the student having maximum marks
max_student = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent having maximum marks:")
print(max_student[0], max_student[1])

# Calculate average marks
average = sum(
    details["marks"] for details in student.values()
) / len(student)

print("Average marks =", average)

# Print students scoring more than average
print("\nStudents scoring more than average:")
for roll, details in student.items():
    if details["marks"] > average:
        print(roll, details)