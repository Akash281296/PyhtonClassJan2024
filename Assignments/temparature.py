#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - Celsius to Fahrenheit and vice versa
"""

temperature_input = input("Enter the Temperature (e.g., 37C or 98.6F): ").strip()

# Extracting temperature value and unit
value = float(temperature_input[:-1])
unit = temperature_input[-1].upper()

if unit == "C":
    # Convert Celsius to Fahrenheit
    fahrenheit = (1.8 * value) + 32
    print(f"Temperature is {round(fahrenheit, 2)} F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    celsius = (value - 32) * 5 / 9
    print(f"Temperature is {round(celsius, 2)} C")
else:
    print("Invalid temperature unit. Please enter 'C' or 'F'.")