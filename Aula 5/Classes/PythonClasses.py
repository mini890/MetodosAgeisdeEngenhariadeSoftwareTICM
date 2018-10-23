class Ponto():
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        # pass #Instrução vazia

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getZ(self):
        return self.z

    def setZ(self, z):
        self.z = z


p1 = Ponto(10, 20, 14)
p2 = Ponto(8, 0, -1)

print(p1.getZ())
print(p2.getX())
print(p2.x)
