for i in range(1, 20):
    for j in range(1, 20):
        if i+1 == j or i == j-1:
            print(f"{i} * {j} = {i * j}")
        