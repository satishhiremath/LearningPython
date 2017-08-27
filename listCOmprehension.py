my_list = [1,2,3,4,5]

# give square of each number in squared list

squared_list = [num*num for num in my_list]
print(squared_list)

# # OR # #

def square(number):
    tempList = [0,0,0,0,0]
    for i in range(0, 5):
        tempList[i] = number[i] **2
    return tempList


emptyList = []
print(emptyList)
emptyList = square(my_list)
print(emptyList)


