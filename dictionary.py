## dictionary is key value pairs like json

classmates = {'sali': 'carrom specialist', 'manju': 'bowling specialist', 'gowli': 'yoga specialist'}


print(classmates['manju'])
print(classmates['sali'])
print(classmates['gowli'])

for i in classmates:
    print(i)

for k, v in classmates.items():
    print(k , 'is', v)

for i in classmates.values():
    print(i)

for i in classmates.keys():
    print(i)