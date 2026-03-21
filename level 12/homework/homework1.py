

temp = int(input("Enter the temperature in Celsius: "))

num = {15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ,26, 27, 28, 29, 30}

if temp > 30:
    print("It's Hot.")

elif temp in num:
    print("It's Warm.")

elif temp < 15:
    print("It's Cold.")

else:
    print("Invalid input.")