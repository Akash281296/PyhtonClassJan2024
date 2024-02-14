num = int(input("Enter your number: "))
for b in range(10, 0, -1):
    print('{:3} * {:3} = {:3}'.format(num, b, num*b))