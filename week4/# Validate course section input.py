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
