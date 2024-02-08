#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""
balance = 0
initial_deposit = 2000
salary_credited = 4300
online_purchase = 123.13
house_rent = 1725
current_balance = balance + initial_deposit + salary_credited - online_purchase + house_rent
print("balance:", current_balance)