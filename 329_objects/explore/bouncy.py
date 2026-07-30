import random

class Bouncy:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.rad = random.randint(5,20)
        self.xvel = random.randint(-6,6)
        self.yvel = random.randint(-6,6)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
    
    def draw(self):
        print("I'm drawing", self)
    
    def move(self):
        print("I'm moving", self)
    
    # TODO define the __str__ method
  
    
  