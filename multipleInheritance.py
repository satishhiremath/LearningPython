class Parent:

    def get_last_name(self):
        print('Rachayya Hiremath')


class Child:   # Child class is inheriting the Parent class

    def get_first_name(self):
        print('Satish')

    def get_last_name(self):   # function overriding in python
        print('Hiremath')


class FullName(Parent, Child):        # multiple inheritance
    pass  # whenever we don't want to add anything in class, the writing PASS will pass it without any syntax errors


objFullName = FullName()
objFullName.get_first_name()
objFullName.get_last_name()




