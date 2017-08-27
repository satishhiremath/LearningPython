class Girl:

    gender = 'girl'    # Class variable. will be same for all the instances of class

    def __init__(self, name):
        self.name = name  # Instance Variable as it is unique for every instance of class not same.

g1 = Girl('Nandini')
g2 = Girl('Deepa')
print(g1.gender)
print(g1.name)
print('\n')
print(g2.gender)
print(g2.name)