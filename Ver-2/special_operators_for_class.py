'''
Defining a class special method __str__() to print class object in informative manner
Without __str__() defined, python will print object as "<__main__.Omg at 0x7f66a473d240>"
After __str__() is defined, python will print object as
"Class car is a object with data attributes x = 10 and y = 20"

isinstance(obj, class) returns 'True' if obj is instance of class else 'False'
'''


class Car(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Class car is a object with data attributes x = {} and y = {}".format(self.x, self.y)


if __name__ == "__main__":
    car = Car(10, 20)
    print(car)  # Python by default calls __str__() method of class object
    print(isinstance(car, Car))
