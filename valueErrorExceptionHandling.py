value = int(input('enter your favourite number'))
print(value)    # prints number if it is number. If entered is string then it will be value error
# and code will throw error

# hence we go for handling exception using try and exception commands

while True:
    try:
        number = int(input('enter fav number'))
        print(100/number)
        break
    except ValueError:
        print('Make sure you enter a number')
    except ZeroDivisionError:
        print('Enter Non-Zero number to avoid division by zero')
    finally:
        print('This line will execute no matter what the condition is')


