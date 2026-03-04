nam1 = int(input("Enter a number: "))
nam2 = int(input("Enter second number: "))

print(nam1 + nam2)
print(nam1 - nam2)
print(nam1 * nam2)
print(nam1 / nam2)
print(nam1 // nam2)
print(nam1 % nam2)

print(bool(int(True) - int(False) + int(False)))

# print(bool(int(True) - int(False) + int(False))) გამოიტანს True რადგან int(True) არის 1 და int(False) არის 0, ამიტომ გამოთვლაში მივიღებთ 1 - 0 + 0 = 1, bool(1) არის True

#int გადაქმნის input-ში შეყვანილ მნიშვნელობას მთელ რიცხვად.
#str გადაქმნის მნიშვნელობას სტრინგად, რომელიც შეიძლება იყოს ტექსტი ან რიცხვი.
#bool გადაქმნის მნიშვნელობას ლოგიკურ ტიპად, სადაც 0 და ცარიელი სტრინგი ითვლება False-ად, ხოლო სხვა ყველა მნიშვნელობა ითვლება True-ად.