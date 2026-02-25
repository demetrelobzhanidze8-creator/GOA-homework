#1user = 'Nika"
#2_user = "Lika'
#print(2_USer)

user1 = "Nika" # ცვლადის დასაწყისში არ3შეიება რიცხვის ან რაიმე სიმბოლოს დაწერა. ასევე ბრჭყალები უნდა იყოს ორივე ერთნაირი.
user_2 = "Lika" # ცვლადის დასაწყისში არ3შეიება რიცხვის ან რაიმე სიმბოლოს დაწერა. ასევე ბრჭყალები უნდა იყოს ორივე ერთნაირი.
print(user_2) # როდესაც ჩვენ ვქმნით ცვლადს ზუსტად იგივე სახელი უნდა გამოვიხენოთ, რადგან python-ი არის case-sensitive ენა.

# მომხმარებლისგან ინფორმაციის მიღება

name = input('what is you name ?: ')
surname = input('what is you surname ?: ')
adress = input('what is you address ?: ')
age = input('what is you age ?: ')

print(f'i am {name} {surname} and i am {age} years old. i live in {adress}.') 