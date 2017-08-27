
# tells how to use for loop
for x in range(2,7,2):
    print(x)
print('\n')
constantVal = 2

# # ''' is for commenting multiple lines
'''
# tells how to use while loop
while constantVal < 5:
    print(constantVal)
    constantVal += 1
'''
print(9,"satish",10,11,1993)

# program to find magic number
magicNumber = 5

for i in range(10):
    if i is magicNumber:
        print(i, "is a magic number")
        break
    else:
        print(i)

print("\n \n")
# write a code looping through 0-100 and printtd number divided by 4

for i in range(101):
    if i%4 is 0:
        print(i)
    else:
        continue
