# Author: Ved Patel
# Date: 31 Jan 2025
# Purpose: Class exercise selection

print("Welcome to the validation sampler")
print("********")

print("We have Student Information Entry System")

# Validate student's full name
while True:
    name = input("Enter Student's Full Name: ")

    # Check if the name is valid (only letters and spaces, and length between 2 to 50)
    if len(name) >= 2 and len(name) <= 50 and name != "":
        student_name = name
        print("Your name is", student_name)
        break  # Exit the loop once the name is valid
    else:
        print("Invalid name. Use only letters and spaces (2-50 characters).")

# Validate student ID
while True:
    studentID = input("Please enter your student ID: ")

    if len(studentID) == 9:
        if studentID.isdigit():
            print("Your ID is", studentID)
            break  # Exit the loop if the ID is valid
        else:
            print("Your ID is invalid!")
    else:
        print("Your ID should be 9 digits long!")

# Validate age input
while True:
    age = input("Enter Age (16-100): ")
    if age.isdigit():
        if 16 <= int(age) <= 100:
            print("Your age is:", age)
            break  # Exit the loop if the age is valid
        else:
            print("Age must be between 16 and 100.")
    else:
        print("Invalid age. Please enter a number.")

# Validate email input
while True:
    email = input("Enter Email Address (example@domain.ca, no spaces): ")

    if " " in email:
        print("Email should not contain spaces.")
    elif "@" not in email or "." not in email:
        print("Invalid email format. Please include '@' and '.'")
    else:
        print("Email is valid:", email)
        break  # Exit the loop once the email is valid

import re  # Importing the re module for regular expressions

# Validate course section input
while True:
    course_section = input("Enter Course Section (e.g., COSC 1100-01): ").strip()
    
    # Check if the input matches the correct pattern (COSC 1100-XX where XX is 01-99)
    if re.match(r'^COSC 1100-(0[1-9]|[1-9][0-9])$', course_section):
        print("Course section is valid:", course_section)
        break  # Exit the loop if valid
    else:
        print("Invalid course section. Use format 'COSC 1100-XX' (XX between 01-99).")

# Display the entered information
print("\nWe have Student Information Entry System")
print(f"Student ID: {studentID}")
print(f"Age : {age}")
print(f"Email Address : {email}")
print(f"Course Section : {course_section}")

print("Thank you for playing!")
