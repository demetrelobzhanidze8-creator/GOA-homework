num1 = input('enter first number: ')
num2 = input('enter second number: ')
if not num1.isdigit() or not num2.isdigit():
    print('you must enter numbers only!')
else:
    print(f'{num1} + {num2} = {int(num1) + int(num2)}')