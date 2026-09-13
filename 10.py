""" Create a tuple of 20 employee name. Perform the following operation on the tuple:
•	Print each name and frequency of that name in the tuple.
•	Remove the duplicate items from the tuple and find the number of distinct name in the tuple.
•	Print the name of the employee having maximum frequency.
•	Sort the tuple in alphabetical order and display.
•	Input a specific employee name and find whether that name exist in the tuple or not.
"""

# Create a tuple of 20 employee names
employees = (
    "Rahul", "Priya", "Amit", "Rahul", "Sneha",
    "Amit", "Riya", "Karan", "Priya", "Rahul",
    "Anjali", "Amit", "Rohit", "Sneha", "Priya",
    "Rahul", "Karan", "Amit", "Neha", "Priya"
)

# 1. Print each name and its frequency
print("Name and Frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))

# 2. Remove duplicate items and find number of distinct names
distinct_names = tuple(set(employees))

print("\nTuple after removing duplicates:")
print(distinct_names)

print("Number of distinct names:", len(distinct_names))

# 3. Employee having maximum frequency
max_frequency = max(employees.count(name) for name in set(employees))

for name in set(employees):
    if employees.count(name) == max_frequency:
        print("\nEmployee with maximum frequency:", name)
        print("Frequency:", max_frequency)

# 4. Sort the tuple alphabetically
sorted_employees = tuple(sorted(employees))

print("\nTuple in alphabetical order:")
print(sorted_employees)

# 5. Search for a specific employee
search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple.")
else:
    print(search_name, "does not exist in the tuple.")