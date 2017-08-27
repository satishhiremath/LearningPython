[date, month, year] = ['wednesday', 'january', 1993]

fistName, middleName, lastName = ['satish', 'rachayya','hiremath']

print(month)
print(middleName)

'''
There are grades, We have to leave first and last grades and calculate average of the middle one's using unpacking 
tuple method
'''

def avg_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/ len(middle)
    print('avg of middle grades is: ' + str(avg))

gradesList = [10, 90, 20, 30, 80, 40]

avg_first_last(gradesList)
