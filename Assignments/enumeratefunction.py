person_details = {
    "name": "Narendra Modi",
    "age": 67,
    "salary": 2_00_000,
    "role": "PM of India",
}

# Enumerate keys
print("\nEnumerating keys:")
for index, key in enumerate(person_details.keys()):
    print(f"Key {index}: {key}")

# Enumerate values
print("\nEnumerating Index:")
for index, value in enumerate(person_details.values()):
    print(f"Index {index}: {value}")

# Enumerate items
print("\nEnumerating items:")
for index, (key, value) in enumerate(person_details.items()):
    print(f"Item {index}: {key} - {value}")