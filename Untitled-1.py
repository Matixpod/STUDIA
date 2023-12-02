class test(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y 


    def add(self, z):
        return self.x + self.y + z
    
    def multiply(self, z):
        return self.x * self.y * z


test(2,4).multiply(3)