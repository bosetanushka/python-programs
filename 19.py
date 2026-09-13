import numpy as np

# 2D array: 5 students, 3 subjects
# Rows = students (ID 0 to 5)
# Columns = subjects (Subject 0, 1, 2)

marks = np.array([
    [78, 85, 90],
    [88, 76, 95],
    [92, 89, 84],
    [65, 72, 70],
    [81, 94, 88],
])

print("Marks Array:")
print(marks)

print("\nMaximum marks:", np.max(marks))

print("Minimum marks:", np.min(marks))

print("Average marks:", np.mean(marks))

# 4. Find the student ID (0 to 5) who scored maximum marks in Subject 1
student_id = np.argmax(marks[:, 1])
print("Student ID with maximum marks in Subject 1:", student_id)
print("Maximum marks in Subject 1:", marks[student_id, 1])

# 5. Find maximum marks subject-wise
max_subject_wise = np.max(marks, axis=0)
print("Maximum marks subject-wise:", max_subject_wise)

# 6. Find average marks subject-wise
avg_subject_wise = np.mean(marks, axis=0)
print("Average marks subject-wise:", avg_subject_wise)

#7. Add 10 marks for all students whose score less than 50 in subject 1.
marks[marks[:, 1] < 50, 1] += 10
print(marks)

#8. find out number of students score more than 80 in subject 2.
count = np.sum(marks[:, 2] > 80)
print("Number of students:", count)

#9. find out the minimum marks of student 2.
minimum = np.min(marks[2])
print("Minimum marks of Student 2:", minimum)

#10. find out the maximum marks of student 4.
maximum = np.max(marks[4])

print("Maximum marks of Student 4:", maximum)