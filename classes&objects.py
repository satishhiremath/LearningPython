'''
This is how Games are made. Creating a Enemy template and creating Instances of it whenever required.
'''

class Enemy:
    life = 4;

    def __init__(self):    # Class initializer or constructor
        print('Init function is called')
        self.life = 5

    def attack(self):     # self means its passing itself to its functions. Hence only
        print('ouch! enemy attacked')        # the variables in class need to be used
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life) + ' life left')


enemy1 = Enemy()   # creating object of class Enemy
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.checkLife()

enemy2.checkLife() # different object. so changes in enemy1 will not be replected in enemy 2

print('size is: ' + str(enemy1.__sizeof__()))   # inbuilt function written by interpreter starts wit __function__
