


password = 'python123'

user_input = input("Enter the password: ")
if user_input != password:
    while user_input != password:
        user_input = str(input("Wrong password, try again: "))
else:
    print("Access granted")


