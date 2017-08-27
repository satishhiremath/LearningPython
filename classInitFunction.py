class Enemy:
    def __init__(self, x):  # passing value to initialise any variable once object is created
        self.energy = x     # variable created inside init function will be the class variable

    def getEnergy(self):
        print(self.energy)

'''
Creating different type of enemies with different energies
'''
soldier = Enemy(54)
soldier.getEnergy()

archer = Enemy(80)
archer.getEnergy()

king = Enemy(99)
king.getEnergy()
