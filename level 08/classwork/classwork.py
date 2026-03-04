print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False


#True and False or False or True and True and False or True = True
#    False     False    true     True     False    true


p = 4 
thief_detected = int(input('piple count: '))
thief_detected = thief_detected > p
print(thief_detected)