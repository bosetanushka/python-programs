#Create a class Student with attributes name, dept, roll. Initialize the attribute with the constructor.
#Display the record of student using show(). Define 5 student objects and show records of 5 students.

class Student:

    # Constructor
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    # Method to display student record
    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Roll:", self.roll)
        print("-------------------")


# Creating 5 Student objects
s1 = Student("Rahul", "CSE", 101)
s2 = Student("Priya", "ECE", 102)
s3 = Student("Amit", "IT", 103)
s4 = Student("Sneha", "CSE", 104)
s5 = Student("Riya", "ECE", 105)

# Displaying records
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()