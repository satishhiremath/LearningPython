class Parent:

    def get_last_name(self):
        print('Rachayya Hiremath')


class Child(Parent):   # Child class is inheriting the Parent class

    def get_first_name(self):
        print('Satish')
'''
    def get_last_name(self):   # function overriding in python
        print('Hiremath')
'''

objChild = Child()
objChild.get_first_name()
objChild.get_last_name()





