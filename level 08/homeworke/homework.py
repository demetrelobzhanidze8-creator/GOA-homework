

# > მეტია
print(10 > 5) #True
print(5 > 10) #False

# < ნაკლებია
print(10 < 5) #False
print(5 < 10) #True

# >= მეტია ან ტოლია
print(10 >= 5) #True
print(5 >= 10) #False
print(5 >= 5) #True

# <= ნაკლებია ან ტოლია
print(10 <= 5) #False
print(5 <= 10) #True
print(5 <= 5) #True

# == ტოლია
print(10 == 5) #False
print(10 == 10) #True

# != არ ტოლია
print(10 != 5) #True
print(10 != 10) #False


# ლოგიკური ოპერატორები: and და or. and არის მკაცრი ოპერატორი და მხოლოდ მაშინ არის True, როცა ორივე მხარე Trueა. or არის რბილი ოპერატორი და მაშინ არის False, როცა ორივე მხარე Falseა.  

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False


# ეს კოდი არის False, რადგან num1-ში არის string მოცემული და num2-ში კი integer ტიპის რიცხვი ამ ორს შორის ვერ განვახორციელებთ ტოლობის ოპერაციას რაგდან num1 აღიქვება როგორც ტექსტი და num2 რიცხვი.

num1 = "21"
num2 = 21
print(num1 == num2)


print(False or True and True and False)
#         True     True     False   = False
print(True and False or False or True)
#         False    False    True   = True
print(True or True and False or True or False and True or False)
#         True     False   True    True     False    True   = True