#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is a vowel or consonant

        Vowels: aeiouAEIOU

The 'in' operator works with any iterable object.

Algorithm:
1. Take input at runtime and clean it using strip().
2. Check if the length of the character is not greater than 1.
3. Check if the character is alphabetical using isalpha().
4. Determine if it's a vowel or not.

NOTE: The logic should accommodate both upper and lower case characters.
"""

character = input("Enter the Character: ")

vowels = "aeiouAEIOU"

if character.isalpha() and len(character) == 1:
    if character in vowels:
        print(f"{character} is a Vowel")
    else:
        print(f"{character} is not a Vowel")
else:
    print("Invalid input. Please enter a single alphabetical character.")