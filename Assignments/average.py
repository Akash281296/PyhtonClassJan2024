"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""
number_list = []
 
number_of_elements = int(input("Enter number of elements: "))
 
counter = 0
while counter < number_of_elements:
    element = int(input())
    number_list.append(element)
    counter += 1

numbers_tuple = tuple(number_list)

average = sum(numbers_tuple) / len(numbers_tuple)
print(f"Average of given numbers is: {average}")
