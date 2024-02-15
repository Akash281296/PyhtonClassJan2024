input_century = int(input("Enter the century: "))

start_year = input_century * 100
end_year = start_year + 100

leap_years_list = []

for year in range(start_year, end_year):
    if year % 4 != 0:
        continue
    elif year % 100 != 0:
        leap_years_list.append(year)
    elif year % 400 != 0:
        continue
    else:
        leap_years_list.append(year)

# Print the leap years in the century
print(f"Leap years in the {input_century}st century:")
print(leap_years_list)