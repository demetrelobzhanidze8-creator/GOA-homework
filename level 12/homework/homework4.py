


positive = 0
negative = 0
zero = 0


for i in range(10):
    inp = int(input('Enter anumber: '))


    if inp > 0:
        positive += 1

    elif inp < 0:
        negative +=1

    else:
        zero += 1

print(f'positive numbers: {positive}')
print(f'negative numbers: {negative}')
print(f'zeros: {zero}')