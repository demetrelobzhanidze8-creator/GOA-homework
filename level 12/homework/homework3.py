

num = int(input("Enter a number: "))

for i in range(0, num + 1):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")