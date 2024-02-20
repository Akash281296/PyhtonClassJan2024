#  Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1

t1 = (1, 2)

result1 = t1 * 3
result2 = 3 * t1

print(result1)  # Output: (1, 2, 1, 2, 1, 2)
print(result2)  # Output: (1, 2, 1, 2, 1, 2)
print(result1 == result2)  # Output: True