num = int(input("Enter your number: "))
for i in range(1, 11):
    for j in range(1, num+1):
        print(f"{j:2} * {i:2} = {i*j:2}", end='\t|')
    print()  