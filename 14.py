# Given string
s = "Python Programming"

# 1. Display "Python"
print("First word:", s[:6])

# 2. Display "Programming"
print("Second word:", s[7:])

# 3. Check whether "java" is present
if "java" not in s.lower():
    print("java is not present")

    # Add java between Python and Programming
    s = "Python Java Programming"

print("New string:", s)

# 4. Find the length of the new string
print("Length of new string:", len(s))

# 5. Count the number of words
words = s.split()
print("Number of words:", len(words))

# 6. Capitalize each word
capitalized = s.title()
print("Capitalized string:", capitalized)

# 7. Remove all spaces
no_space = s.replace(" ", "")
print("String without spaces:", no_space)

# 8. Frequency of A, P, R and M (case-sensitive)
print("Frequency of A:", s.count("A"))
print("Frequency of P:", s.count("P"))
print("Frequency of R:", s.count("R"))
print("Frequency of M:", s.count("M"))