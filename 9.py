"""  Create a list of 20 student marks and perform the following operations.
•	Find out the average marks from the list
•	Find out the number of students score more than the average in the in the list
•	Find the marks that maximum students scored in the list
"""

# List of 20 student marks
marks = [75, 80, 65, 90, 85, 70, 80, 95, 60, 75,
         80, 85, 70, 80, 90, 65, 75, 80, 85, 70]

# 1. Find average marks
average = sum(marks) / len(marks)

print("Average marks =", average)

# 2. Count students scoring more than average
count = 0

for mark in marks:
    if mark > average:
        count = count + 1

print("Number of students scoring more than average =", count)

# 3. Find the marks scored by maximum students
most_scored = max(set(marks), key=marks.count)

print("Marks scored by maximum students =", most_scored)