
def printName():
    print('my name is satish the coder')

def printNoName():
    print('I am not satish')

var = 0
if var:
    printName()
else:
    printNoName()

## give square of a number   #################################################################

#function definition
def squareOfaNumber(number):
    output = number * number
    print(output)

#function call
squareOfaNumber(5)
print('\n\n')

## return statement ######################################################################
def squareNumber(num):
    output = num * num
    return output

numToBeSquared = 3
squareofNumber = squareNumber(numToBeSquared)
print('square of ', numToBeSquared, "is", squareofNumber)

## Default values as arguemnts to a function################################################

def getGender(gender = "unknown"):
    if gender is 'm':
        gender = "male"
    elif gender is 'f':
        gender = "female"
    print(gender)

getGender('m')
getGender('f')
getGender()   #here default value of arguement is used
print('\n')

## default keyword arguements#################################################################

def printNames(first = "satish", second = "sali", third = "sharath"):
    print(first, second, third)

printNames()
printNames(second = 'manjunath')
printNames("gowli", "dinesh")

print('\n')

## Flexible number of  arguements using *args ##################################################

def addNumbers(*args):
    total = 0
    for i in args:
        total += i
    print(total)

addNumbers(3)
addNumbers(3,4,5)
addNumbers(2,343,5454,656,6767,454,24324,5767,3434,676)     #any number of arguements

print('\n')

## Flexible number of  arguements using *args ##################################################

def printDOB(date, month, year):
    print("DOB is ", date,'/',month, '/', year)

printDOB(20,1,1993)

DOB_Data = [27,1,1993]
printDOB(*DOB_Data)