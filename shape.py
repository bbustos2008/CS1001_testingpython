class shape:
    def getarea():
        return -1
    def getperimeter():
        return -1
    
class rectangle(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def getarea(self):
        return self.length * self.width
    def getperimeter(self):
        return (self.length + self.width) * 2
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def getarea(self):
        return self.radius * self.radius * 3.14
    
    def getperimeter():
        return self.radius 
    