""" Create a list of 10 student name and another list of their marks. 
Find out the students having maximum and minimum marks. 
Both of the lists are unsorted and don't have any duplicate values
"""
# List of student names
students = ["Rahul", "Priya", "Amit", "Sneha", "Riya",
            "Arjun", "Karan", "Anjali", "Rohit", "Neha"]

# List of marks
marks = [85, 72, 95, 68, 90, 78, 88, 65, 92, 75]

# Find maximum and minimum marks
max_marks = max(marks)
min_marks = min(marks)

# Find the students having maximum and minimum marks
max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Student with maximum marks:", students[max_index])
print("Maximum marks:", max_marks)

print("Student with minimum marks:", students[min_index])
print("Minimum marks:", min_marks)