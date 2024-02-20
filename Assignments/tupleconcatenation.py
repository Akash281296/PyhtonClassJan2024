# Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1

t1 = (1, 2)
t2 = (3, 4)

result1 = t1 + t2
result2 = t2 + t1

print(result1)  # Output: (1, 2, 3, 4)
print(result2)  # Output: (3, 4, 1, 2)
print(result1 == result2)  # Output: False