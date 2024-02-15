#!/usr/bin/python
"""
Purpose:
    break     - breaks the complete loop
    continue  - skip the current loop iteration
    pass      - does nothing, acts as a placeholder
    sys.exit  - exits the script execution
"""
import sys

student_names = ["Vikram", "Achilles", "Bruce wayne", "Dilli", "Rolex", "Ragnar Lothbrok", "."]

for name in student_names:
    if name == "Ragnar Lothbrok":
        pass  # Placeholder, do nothing
    if name == "Bruce wayne":
        print(f"{name}")
    if name == "Achilles":
        print(f"{name}")
        continue  # Skip remaining code in loop for this iteration
    if name == ".":
        sys.exit("Cannot proceed further due to '.' encountered")
        # Code below this will not be executed due to sys.exit()

# The following code won't be executed if '.' is encountered
# a = 100 / i  # This line will not be reached if '.' is encountered